'use strict';

// Retry only the observed transient HTTP 529 response. The source comparison,
// browser context, URL, and returned response are unchanged.
const fs = require('node:fs');
const {chromium} = require('playwright');
const delays = [3000, 7000, 15000];

async function retry529(goto, url, options, pause, log) {
  for (let attempt = 0; ; attempt++) {
    const response = await goto(url, options);
    if (response?.status() !== 529) return response;
    const body = await response.text().catch(() => '');
    const denied = /blocked by (?:an? )?administrator|access denied|permission denied|not authori[sz]ed|policy (?:denied|violation)|captcha/i.test(body);
    const retry = !denied && attempt < delays.length;
    log({url, status:529, attempt:attempt+1, retry,
      observed_at:new Date().toISOString(),
      response_excerpt:body.replace(/\s+/g,' ').slice(0,1200)});
    if (!retry) return response;
    await pause(delays[attempt]);
  }
}

const launch = chromium.launch.bind(chromium);
chromium.launch = async (...args) => {
  const browser = await launch(...args);
  const newContext = browser.newContext.bind(browser);
  browser.newContext = async (...contextArgs) => {
    const context = await newContext(...contextArgs);
    const newPage = context.newPage.bind(context);
    context.newPage = async (...pageArgs) => {
      const page = await newPage(...pageArgs);
      const goto = page.goto.bind(page);
      page.goto = (url, options) => retry529(goto, url, options,
        delay => new Promise(resolve => setTimeout(resolve, delay)),
        event => {
          const line = JSON.stringify(event);
          console.log('HOSTED_HTTP_529 '+line);
          if (process.env.HOSTED_RETRY_LOG) fs.appendFileSync(process.env.HOSTED_RETRY_LOG, line+'\n');
        });
      return page;
    };
    return context;
  };
  return browser;
};

module.exports = {retry529};

const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://cas.webcollege.seinesaintdenis.fr/login?');
  await page.screenshot({ path: 'example1234.png' });
  await page.goto('https://cas.webcollege.seinesaintdenis.fr/login?');
  await page.screenshot({ path: 'example123456.png' });

  await browser.close();
})();
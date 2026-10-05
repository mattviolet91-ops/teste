const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + __dirname + '/carrousel.html'); await p.waitForTimeout(1500);
  const secs = await p.$$('section');
  for (let i = 0; i < secs.length; i++) await secs[i].screenshot({ path: `slide-${String(i + 1).padStart(2, '0')}.png` });
  await b.close();
})();

// PDF 출력: node render_pdf.js $PWD/workbook.html $PWD/workbook.pdf  (배경색 인쇄 + 쪽 번호. Noto Sans CJK KR 글꼴 필요)
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.argv[2]);
  await p.pdf({ path: process.argv[3], preferCSSPageSize: true, printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;text-align:center;font-size:8pt;color:#333;font-family:\'Noto Sans CJK KR\';"><span class="pageNumber"></span></div>' });
  await b.close();
})();

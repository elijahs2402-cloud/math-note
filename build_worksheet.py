"""5학년 2학기 '2. 분수의 곱셈' 오답 문제지(A4) HTML 생성기.

python3 build_worksheet.py  ->  worksheet.html  (Chromium으로 worksheet.pdf 출력)
"""


def fr(n, d):
    return f'<span class="fr"><span>{n}</span><span>{d}</span></span>'


def mx(w, n, d):
    return f'<span class="mx">{w}{fr(n, d)}</span>'


BOX = '<span class="box"></span>'


# ---------- SVG helpers ----------
def svg_frac(x, y, n, d, size=15, anchor="middle"):
    """(x, y) = 분수 막대 중심."""
    w = max(len(str(n)), len(str(d))) * size * 0.62 + 6
    return (
        f'<text x="{x}" y="{y - 4}" font-size="{size}" text-anchor="middle">{n}</text>'
        f'<line x1="{x - w / 2}" y1="{y}" x2="{x + w / 2}" y2="{y}" stroke="#000" stroke-width="1.2"/>'
        f'<text x="{x}" y="{y + size + 1}" font-size="{size}" text-anchor="middle">{d}</text>'
    )


def number_line(parts, end_n, end_d, target):
    W, x0, x1, y = 330, 20, 310, 30
    step = (x1 - x0) / parts
    s = [f'<svg viewBox="0 0 {W} 150" width="{W}" height="150">']
    s.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#000" stroke-width="1.6"/>')
    for i in range(parts + 1):
        x = x0 + i * step
        s.append(f'<line x1="{x}" y1="{y - 9}" x2="{x}" y2="{y + 9}" stroke="#000" stroke-width="1.6"/>')
        if i < parts:
            s.append(
                f'<path d="M{x},{y + 4} Q{x + step / 2},{y + 22} {x + step},{y + 4}" '
                f'fill="none" stroke="#666" stroke-width="1"/>'
            )
    s.append(f'<text x="{x0}" y="{y + 32}" font-size="15" text-anchor="middle">0</text>')
    s.append(svg_frac(x1, y + 40, end_n, end_d))
    tx = x0 + target * step
    s.append(f'<line x1="{tx}" y1="{y + 78}" x2="{tx}" y2="{y + 14}" stroke="#000" stroke-width="1.4"/>')
    s.append(f'<path d="M{tx - 5},{y + 22} L{tx},{y + 13} L{tx + 5},{y + 22}" fill="none" stroke="#000" stroke-width="1.4"/>')
    s.append(f'<rect x="{tx - 22}" y="{y + 78}" width="44" height="40" fill="#fff" stroke="#000" stroke-width="1.4"/>')
    s.append("</svg>")
    return "".join(s)


def fig09():
    W, x0, x1, y = 340, 25, 315, 70
    step = (x1 - x0) / 8
    s = [f'<svg viewBox="0 0 {W} 130" width="{W}" height="130">']
    # 전체 길이 호 + 4 2/3 m
    s.append(f'<path d="M{x0},{y - 6} Q{(x0 + x1) / 2},{y - 50} {x1},{y - 6}" fill="none" stroke="#555" stroke-width="1.1"/>')
    cx = (x0 + x1) / 2
    s.append(f'<text x="{cx - 20}" y="{y - 46}" font-size="18" text-anchor="middle">4</text>')
    s.append(svg_frac(cx - 6, y - 53, 2, 3, size=13))
    s.append(f'<text x="{cx + 14}" y="{y - 46}" font-size="16" text-anchor="middle">m</text>')
    s.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#000" stroke-width="1.8"/>')
    for i in range(9):
        x = x0 + i * step
        s.append(f'<line x1="{x}" y1="{y - 7}" x2="{x}" y2="{y + 7}" stroke="#000" stroke-width="1.5"/>')
        if i < 8:
            s.append(
                f'<path d="M{x},{y + 3} Q{x + step / 2},{y + 18} {x + step},{y + 3}" '
                f'fill="none" stroke="#777" stroke-width="0.9"/>'
            )
    for i, lab in ((0, "ㄱ"), (3, "ㄴ")):
        x = x0 + i * step
        s.append(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#000"/>')
        s.append(f'<text x="{x}" y="{y + 32}" font-size="16" text-anchor="middle" font-weight="bold">{lab}</text>')
    s.append("</svg>")
    return "".join(s)


def fig10():
    W, x0, y, h = 340, 20, 15, 34
    cell = 30
    s = [f'<svg viewBox="0 0 {W} 110" width="{W}" height="110">']
    for i in range(10):
        fill = "#9fc3e6" if i < 9 else "#fff"
        s.append(f'<rect x="{x0 + i * cell}" y="{y}" width="{cell}" height="{h}" fill="{fill}" stroke="#000" stroke-width="1.3"/>')
    xe = x0 + 10 * cell
    yb = y + h + 8
    s.append(
        f'<path d="M{x0},{yb} Q{x0},{yb + 12} {x0 + 12},{yb + 12} L{(x0 + xe) / 2 - 8},{yb + 12} '
        f'Q{(x0 + xe) / 2},{yb + 12} {(x0 + xe) / 2},{yb + 22} Q{(x0 + xe) / 2},{yb + 12} {(x0 + xe) / 2 + 8},{yb + 12} '
        f'L{xe - 12},{yb + 12} Q{xe},{yb + 12} {xe},{yb}" fill="none" stroke="#000" stroke-width="1.2"/>'
    )
    s.append(f'<text x="{(x0 + xe) / 2}" y="{yb + 40}" font-size="15" text-anchor="middle">30 cm</text>')
    s.append("</svg>")
    return "".join(s)


# ---------- 문제 ----------
P = []

P.append(("01", f"진수는 동화책을 어제는 28쪽을 읽었고, 오늘은 어제 읽은 것의 {mx(1, 4, 7)}를 읽었습니다. 어제와 오늘 읽은 동화책은 모두 몇 쪽입니까?", "", "쪽"))
P.append(("03", f"케이크 한 개의 무게는 {fr(4, 9)} kg입니다. 현수, 용진, 수민이가 이 케이크의 {fr(5, 6)}를 똑같이 나누어 먹었다면, 수민이가 먹은 케이크의 무게는 몇 kg입니까?", "", "kg"))
P.append(("05", "바르게 말한 학생을 찾아 이름을 쓰시오.",
          f'<div class="opts">송화: 1m의 {fr(1, 5)}은 50cm야.<br>익준: 1kg의 {fr(1, 4)}은 250g이야.<br>정원: 1시간의 {fr(1, 2)}은 40분이야.</div>', ""))
P.append(("06", "바르게 말한 학생은 누구인지 번호를 쓰시오.",
          f'<div class="opts">① 모모: 1m의 {fr(1, 5)}은 20cm입니다.<br>② 지효: 1km의 {fr(1, 2)}은 200m입니다.<br>③ 연희: 1L의 {fr(3, 10)}은 500mL입니다.</div>', ""))
P.append(("08", f"미영이는 한 시간에 {mx(2, 2, 7)} km를 걷는다고 합니다. 같은 빠르기로 하루에 2시간 10분씩 2주일 동안 걷는다면 몇 km를 걷겠습니까?", "", "km"))
P.append(("09", "그림에서 선분 ㄱㄴ의 길이를 구하시오.", f'<div class="fig">{fig09()}</div>', "m"))
P.append(("10", "색 테이프를 10등분한 것입니다. 색칠한 부분의 가로는 몇 cm인지 구하시오.", f'<div class="fig">{fig10()}</div>', "cm"))
P.append(("11", "그림을 보고, 빈칸에 알맞은 수를 써넣으시오.", f'<div class="fig">{number_line(8, 4, 15, 3)}</div>', None))
P.append(("12", "다음은 선분을 7등분한 그림입니다. 빈칸에 알맞은 수를 써넣으시오.", f'<div class="fig">{number_line(7, 7, 18, 3)}</div>', None))
P.append(("13", f"40km를 가는 데 전체의 {fr(3, 8)}은 전철을 타고, 나머지의 {fr(3, 5)}는 버스를 타고, 그 나머지는 걸어갔습니다. 걸어간 거리를 구하시오.", "", "km"))
P.append(("14", f"현빈이는 길이가 90cm인 철사를 가지고 있습니다. 그중 {fr(2, 5)}는 미술 시간에 사용하고, 나머지의 {fr(2, 3)}는 서진이에게 주었습니다. 남은 철사의 길이는 몇 cm입니까?", "", "cm"))
P.append(("15", f"어떤 수에서 {fr(5, 9)}를 빼고 9를 곱해야 할 것을 잘못하여 {fr(5, 9)}를 빼고 9를 더하였더니 {mx(9, 7, 15)}이 되었습니다. 바르게 계산하면 얼마입니까?", "", ""))
P.append(("16", f"어떤 수에 {fr(2, 5)}를 곱해야 할 것을 잘못하여 더했더니 {fr(28, 55)}이 되었습니다. 바르게 계산한 값은 얼마입니까?",
          f'<div class="choices"><span>① {fr(2, 11)}</span><span>② {fr(4, 11)}</span><span>③ {fr(6, 11)}</span><span>④ {fr(8, 11)}</span><span>⑤ {fr(10, 11)}</span></div>', ""))
P.append(("17", f"빵집에 빵이 진열되어 있습니다. 하루 동안 처음 있던 빵의 {fr(3, 4)}을 팔고, 남은 빵의 개수를 세어 보니 모두 15개였습니다. 처음에 진열되어 있던 빵은 모두 몇 개입니까?", "", "개"))
P.append(("18", f"윤서네 반은 한 묶음에 12장씩 들어 있는 색종이 다섯 묶음을 샀습니다. 반 학생들이 한 장씩 나누어 가졌더니 전체의 {fr(1, 5)}이 남았다면, 윤서네 반 학생 수는 모두 몇 명입니까?", "", "명"))
P.append(("19", "□ 안에 들어갈 수 있는 자연수는 모두 몇 개입니까?",
          f'<div class="ineq"><span class="mx">{BOX}{fr(2, 5)}</span> &lt; {mx(2, 5, 9)} × {mx(1, 4, 5)}</div>', "개"))

PAGES = [P[0:6], P[6:12], P[12:16]]


def render_problem(num, text, extra, unit, top=False):
    ans = "" if unit is None else f'<div class="ans">(&nbsp;<span class="blank"></span>{unit}&nbsp;)</div>'
    return (
        f'<div class="prob{" top" if top else ""}"><div class="q"><span class="num">{num}</span>'
        f'<div class="txt">{text}</div></div>{extra}<div class="work"></div>{ans}</div>'
    )


CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: 'WenQuanYi Zen Hei', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif; color: #000; }
.page { width: 210mm; height: 297mm; padding: 12mm 12mm 10mm; page-break-after: always; display: flex; flex-direction: column; }
.page:last-child { page-break-after: auto; }
header { border-bottom: 2.5px solid #1d6b4f; padding-bottom: 3mm; margin-bottom: 4mm; display: flex; justify-content: space-between; align-items: flex-end; }
header .t1 { font-size: 11pt; color: #1d6b4f; font-weight: bold; }
header .t2 { font-size: 18pt; font-weight: bold; margin-top: 1mm; }
header .info { font-size: 11pt; white-space: nowrap; }
header .info span { display: inline-block; border-bottom: 1px solid #000; width: 28mm; margin-left: 2mm; }
.small-head { font-size: 10pt; color: #1d6b4f; font-weight: bold; border-bottom: 1.5px solid #1d6b4f; padding-bottom: 2mm; margin-bottom: 4mm; display: flex; justify-content: space-between; }
.grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: repeat(3, 1fr); column-gap: 8mm; }
.grid.r2 { grid-template-rows: repeat(2, 1fr); }
.prob { border-top: 1px dashed #bbb; padding: 3mm 0 2mm; display: flex; flex-direction: column; position: relative; }
.grid { grid-auto-flow: column; }
.prob.top { border-top: none; padding-top: 0; }
.q { display: flex; gap: 2.5mm; align-items: flex-start; }
.num { font-size: 17pt; font-weight: bold; color: #1d6b4f; line-height: 1; min-width: 9mm; }
.txt { font-size: 11.5pt; line-height: 2.05; word-break: keep-all; }
.fr { display: inline-flex; flex-direction: column; align-items: center; vertical-align: middle; font-size: 0.9em; line-height: 1.1; margin: 0 0.12em; }
.fr > span:first-child { border-bottom: 1.2px solid #000; padding: 0 0.15em; }
.fr > span:last-child { padding: 0 0.15em; }
.mx { white-space: nowrap; }
.box { display: inline-block; width: 1.1em; height: 1.25em; border: 1.4px solid #000; vertical-align: middle; }
.opts { font-size: 11.5pt; line-height: 2.1; margin: 1.5mm 0 0 11.5mm; padding: 1.5mm 3mm; border: 1px solid #999; border-radius: 2mm; display: inline-block; }
.choices { margin: 2mm 0 0 11.5mm; font-size: 11.5pt; display: flex; gap: 5mm; flex-wrap: wrap; }
.ineq { margin: 3mm 0 0 11.5mm; font-size: 13pt; padding: 2mm 4mm; border: 1px solid #999; border-radius: 2mm; display: inline-block; align-self: flex-start; }
.opts { align-self: flex-start; }
.fig { margin: 2mm 0 0 8mm; }
.fig svg text { font-family: 'WenQuanYi Zen Hei', sans-serif; }
.work { flex: 1; }
.ans { text-align: right; font-size: 12pt; }
.blank { display: inline-block; width: 28mm; }
footer { text-align: center; font-size: 9pt; color: #777; margin-top: 2mm; }
"""


def main():
    pages = []
    for i, probs in enumerate(PAGES):
        if i == 0:
            head = (
                '<header><div><div class="t1">5학년 2학기 · 2. 분수의 곱셈</div>'
                '<div class="t2">오답 다시 풀기</div></div>'
                '<div class="info">날짜<span></span>&nbsp;&nbsp;이름<span></span></div></header>'
            )
        else:
            head = '<div class="small-head"><span>5학년 2학기 · 2. 분수의 곱셈 — 오답 다시 풀기</span></div>'
        cls = "grid r2" if len(probs) == 4 else "grid"
        rows = len(probs) // 2
        body = "".join(render_problem(*p, top=(k % rows == 0)) for k, p in enumerate(probs))
        pages.append(f'<section class="page">{head}<div class="{cls}">{body}</div><footer>{i + 1} / {len(PAGES)}</footer></section>')
    html = (
        '<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        f'<title>분수의 곱셈 오답 문제지</title><style>{CSS}</style></head><body>'
        + "".join(pages)
        + "</body></html>"
    )
    with open("worksheet.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()

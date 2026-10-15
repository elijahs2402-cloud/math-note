"""분수의 곱셈 개념 다지기 문제집(A4) HTML 생성기.

python3 build_workbook.py  ->  workbook.html  (Chromium으로 workbook.pdf 출력)
오답 문제지(worksheet)에서 틀린 유형을 개념부터 차근차근 익히도록 구성.
"""

from build_worksheet import BOX, fr, mx, svg_frac

X = '<span class="op">×</span>'
EQ = '<span class="op">=</span>'
LT = '<span class="op">&lt;</span>'
BL = '<span class="bl"></span>'      # 빈칸(숫자 하나 이상)
SB = '<span class="sb"></span>'      # 분수 안 작은 빈칸


def bfr(n=None, d=None):
    """분자/분모 중 None 인 곳을 빈칸으로."""
    return fr(SB if n is None else n, SB if d is None else d)


# ---------- SVG ----------
BLUE, BLUE_D, ORANGE, GRAY = "#9cc3e8", "#3f78b5", "#f6c38b", "#e8e8e8"
# 흑백 인쇄에서도 구분되도록 파랑 칸에 빗금
HATCH = ('<defs><pattern id="wbh" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<rect width="6" height="6" fill="{BLUE}"/><line x1="0" y1="0" x2="0" y2="6" stroke="#2f5f94" stroke-width="1.6"/>'
         '</pattern></defs>')


def bar(parts, shade, total=None, shade2=0, cell_labels=None, w=330, h=34, note=None):
    """parts칸 막대: 앞 shade칸 파랑, 다음 shade2칸 주황. total은 아래 괄호 라벨."""
    cw = w / parts
    top = 20 if cell_labels else 6
    H = top + h + (40 if total else 8)
    s = [f'<svg viewBox="0 0 {w + 20} {H}" width="{w + 20}" height="{H}">', HATCH]
    for i in range(parts):
        fill = "url(#wbh)" if i < shade else ORANGE if i < shade + shade2 else "#fff"
        s.append(f'<rect x="{10 + i * cw}" y="{top}" width="{cw}" height="{h}" fill="{fill}" stroke="#000" stroke-width="1.2"/>')
        if cell_labels:
            s.append(f'<text x="{10 + i * cw + cw / 2}" y="{top - 6}" font-size="12" text-anchor="middle">{cell_labels[i]}</text>')
        if note and i < len(note) and note[i]:
            s.append(f'<text x="{10 + i * cw + cw / 2}" y="{top + h / 2 + 5}" font-size="13" text-anchor="middle">{note[i]}</text>')
    if total:
        y = top + h + 6
        x0, x1 = 10, 10 + w
        m = (x0 + x1) / 2
        s.append(
            f'<path d="M{x0},{y} Q{x0},{y + 10} {x0 + 10},{y + 10} L{m - 7},{y + 10} Q{m},{y + 10} {m},{y + 18} '
            f'Q{m},{y + 10} {m + 7},{y + 10} L{x1 - 10},{y + 10} Q{x1},{y + 10} {x1},{y}" fill="none" stroke="#000" stroke-width="1.1"/>'
        )
        s.append(f'<text x="{m}" y="{y + 33}" font-size="14" text-anchor="middle">{total}</text>')
    s.append("</svg>")
    return "".join(s)


def area(a, b, c, d, size=150):
    """(a/b) × (c/d) 넓이 모델: 세로로 b칸 중 a칸(연한 파랑), 가로로 d칸 중 c칸(진한 파랑)."""
    cw, rh = size / b, size / d
    ox, oy = 46, 34
    s = [f'<svg viewBox="0 0 {size + 60} {size + 44}" width="{size + 60}" height="{size + 44}">']
    for i in range(b):
        for j in range(d):
            fill = BLUE_D if (i < a and j < c) else BLUE if i < a else "#fff"
            s.append(f'<rect x="{ox + i * cw}" y="{oy + j * rh}" width="{cw}" height="{rh}" fill="{fill}" stroke="#555" stroke-width="0.8"/>')
    s.append(f'<rect x="{ox}" y="{oy}" width="{size}" height="{size}" fill="none" stroke="#000" stroke-width="1.6"/>')
    s.append(svg_frac(ox + a * cw / 2, 13, a, b, size=11))
    s.append(svg_frac(22, oy + c * rh / 2 - 6, c, d, size=11))
    s.append("</svg>")
    return "".join(s)


def nl(parts, end, target=None, box_at=None, w=330):
    """0부터 end까지 parts칸 수직선. end = (n, d) 또는 정수. box_at 눈금에 화살표+빈칸."""
    x0, x1, y = 20, w - 20, 22
    step = (x1 - x0) / parts
    H = 112 if box_at is not None else 70
    s = [f'<svg viewBox="0 0 {w} {H}" width="{w}" height="{H}">']
    s.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#000" stroke-width="1.6"/>')
    for i in range(parts + 1):
        x = x0 + i * step
        s.append(f'<line x1="{x}" y1="{y - 8}" x2="{x}" y2="{y + 8}" stroke="#000" stroke-width="1.5"/>')
        if i < parts:
            s.append(f'<path d="M{x},{y + 4} Q{x + step / 2},{y + 20} {x + step},{y + 4}" fill="none" stroke="#777" stroke-width="1"/>')
    s.append(f'<text x="{x0}" y="{y + 30}" font-size="14" text-anchor="middle">0</text>')
    if isinstance(end, tuple):
        s.append(svg_frac(x1, y + 36, end[0], end[1], size=13))
    else:
        s.append(f'<text x="{x1}" y="{y + 30}" font-size="14" text-anchor="middle">{end}</text>')
    if box_at is not None:
        tx = x0 + box_at * step
        s.append(f'<line x1="{tx}" y1="{y + 50}" x2="{tx}" y2="{y + 12}" stroke="#000" stroke-width="1.3"/>')
        s.append(f'<path d="M{tx - 5},{y + 20} L{tx},{y + 11} L{tx + 5},{y + 20}" fill="none" stroke="#000" stroke-width="1.3"/>')
        s.append(f'<rect x="{tx - 18}" y="{y + 50}" width="36" height="34" fill="#fff" stroke="#000" stroke-width="1.3"/>')
    s.append("</svg>")
    return "".join(s)


def segment(parts, total_html_svg, labels, w=330):
    """선분 parts등분. labels = {눈금번호: 글자}."""
    x0, x1, y = 20, w - 20, 62
    step = (x1 - x0) / parts
    s = [f'<svg viewBox="0 0 {w} 112" width="{w}" height="112">']
    s.append(f'<path d="M{x0},{y - 6} Q{(x0 + x1) / 2},{y - 34} {x1},{y - 6}" fill="none" stroke="#555" stroke-width="1.1"/>')
    s.append(total_html_svg((x0 + x1) / 2, 12))
    s.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#000" stroke-width="1.7"/>')
    for i in range(parts + 1):
        x = x0 + i * step
        s.append(f'<line x1="{x}" y1="{y - 7}" x2="{x}" y2="{y + 7}" stroke="#000" stroke-width="1.4"/>')
        if i < parts:
            s.append(f'<path d="M{x},{y + 3} Q{x + step / 2},{y + 17} {x + step},{y + 3}" fill="none" stroke="#777" stroke-width="0.9"/>')
        if i in labels:
            s.append(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#000"/>')
            s.append(f'<text x="{x}" y="{y + 32}" font-size="15" text-anchor="middle">{labels[i]}</text>')
    s.append("</svg>")
    return "".join(s)


def total_mixed(w, n, d, unit):
    def f(cx, y):
        return (
            f'<text x="{cx - 18}" y="{y + 12}" font-size="17" text-anchor="middle">{w}</text>'
            + svg_frac(cx - 4, y + 6, n, d, size=12)
            + f'<text x="{cx + 14}" y="{y + 12}" font-size="15" text-anchor="middle">{unit}</text>'
        )
    return f


def total_text(t):
    def f(cx, y):
        return f'<text x="{cx}" y="{y + 12}" font-size="15" text-anchor="middle">{t}</text>'
    return f


# ---------- 블록 ----------
def concept(title, body):
    return f'<div class="concept blk"><div class="ct">{title}</div>{body}</div>'


def rule(body):
    return f'<div class="rule blk"><span class="rt">기억해요</span>{body}</div>'


def follow(body):
    return f'<div class="follow blk"><div class="ft">따라 해 봐요 <span class="hint">빈칸을 채워요</span></div>{body}</div>'


def careful(body):
    return f'<div class="careful blk"><b>조심!</b> {body}</div>'


def drills(items, cols=2):
    cells = "".join(f'<div class="dr"><span class="qn">({i})</span>{q}</div>' for i, q in enumerate(items, 1))
    return f'<div class="drills c{cols} blk"><div class="pt">연습해요</div><div class="grid">{cells}</div></div>'


def words(items, start=1, title="연습해요", space=26):
    out = []
    for i, (q, unit) in enumerate(items, start):
        ans = f'<div class="wans">(<span class="u">{unit}&nbsp;)</span></div>'
        out.append(f'<div class="wp blk"><div class="wq"><span class="qn">({i})</span><div>{q}</div></div>'
                   f'<div class="ws" style="height:{space}mm"></div>{ans}</div>')
    head = f'<div class="pt">{title}</div>' if title else ""
    return head + "".join(out)


def lesson(no, title, sub, linked, body):
    tag = f'<span class="linked">오답 {linked}번과 연결</span>' if linked else ""
    return (f'<section class="lesson"><div class="lh"><span class="ln">{no}</span>'
            f'<div><div class="lt">{title}</div><div class="ls">{sub}</div></div>{tag}</div>{body}</section>')


def eq(*parts):
    return f'<div class="eq">{" ".join(parts)}</div>'


# ---------- 차시 ----------
L = []
ANS = []

# 1
L.append(lesson("1", "'~의 ~'는 곱셈이에요", "분수만큼은 얼마일까?", "10", "".join([
    concept("사탕 12개의 " + fr(1, 3) + "은 몇 개일까요?",
            f'<div class="row"><div>{bar(12, 4, "사탕 12개", cell_labels=None, note=["●"] * 12)}</div>'
            f'<div class="side">12개를 <b>3묶음</b>으로 똑같이 나누면 한 묶음은 4개예요.<br>'
            f'그중 <b>1묶음</b>이니까 4개!<br>12의 {fr(1, 3)} {EQ} 12 {X} {fr(1, 3)} {EQ} <b>4</b></div></div>'
            f'<div class="row"><div>{bar(12, 8, "사탕 12개", note=["●"] * 12)}</div>'
            f'<div class="side">12의 {fr(2, 3)}은 <b>2묶음</b>이에요.<br>4 + 4 = 8개<br>12 {X} {fr(2, 3)} {EQ} <b>8</b></div></div>'),
    rule(f"<b>■의 {fr('▲', '●')}</b> {EQ} ■ {X} {fr('▲', '●')}　→　■를 ●묶음으로 나누고(÷●), 그중 ▲묶음(×▲)"),
    follow(f'<div class="row"><div>{bar(10, 9, "30 cm")}</div><div class="side">'
           f'30cm의 {fr(9, 10)}<br>① 10묶음으로 나누면 한 묶음: 30 ÷ 10 {EQ} {BL}<br>'
           f'② 9묶음이니까: {BL} {X} 9 {EQ} {BL} cm</div></div>'),
    drills([f"20의 {fr(1, 4)} {EQ} {BL}", f"20의 {fr(3, 4)} {EQ} {BL}", f"18의 {fr(2, 3)} {EQ} {BL}",
            f"40의 {fr(3, 8)} {EQ} {BL}", f"90의 {fr(2, 5)} {EQ} {BL}", f"60의 {fr(5, 6)} {EQ} {BL}"]),
    words([(f"길이가 30cm인 색 테이프를 10칸으로 똑같이 나누고 9칸을 색칠했어요. 색칠한 부분은 몇 cm일까요?", "cm")],
          start=7, title=None, space=18),
])))
ANS.append(("1", ["따라 해 봐요: 3, 3 × 9 = 27", "(1) 5", "(2) 15", "(3) 12", "(4) 15", "(5) 36", "(6) 50", "(7) 27cm"]))

# 2
L.append(lesson("2", "단위를 바꾸면 쉬워요", "1m의 1/5은 몇 cm?", "05, 06", "".join([
    concept("먼저 작은 단위로 바꿔요",
            '<table class="units"><tr><td>1m = <b>100</b>cm</td><td>1km = <b>1000</b>m</td><td>1kg = <b>1000</b>g</td></tr>'
            '<tr><td>1L = <b>1000</b>mL</td><td>1시간 = <b>60</b>분</td><td>1일 = <b>24</b>시간</td></tr></table>'
            f'<div class="ex">1m의 {fr(1, 5)} → 100cm의 {fr(1, 5)} → 100 {X} {fr(1, 5)} {EQ} <b>20cm</b></div>'),
    careful(f"1시간은 100분이 아니라 <b>60분</b>이에요! 1시간의 {fr(1, 2)}은 30분이에요."),
    follow(f'1kg의 {fr(1, 4)} → {BL}g의 {fr(1, 4)} → {BL} {X} {fr(1, 4)} {EQ} {BL}g<br>'
           f'1시간의 {fr(1, 3)} → {BL}분의 {fr(1, 3)} → {BL} {X} {fr(1, 3)} {EQ} {BL}분'),
    drills([f"1m의 {fr(3, 4)} {EQ} {BL}cm", f"1km의 {fr(1, 2)} {EQ} {BL}m", f"1L의 {fr(3, 10)} {EQ} {BL}mL",
            f"1kg의 {fr(2, 5)} {EQ} {BL}g", f"1시간의 {fr(1, 4)} {EQ} {BL}분", f"1시간의 {fr(5, 6)} {EQ} {BL}분"]),
    f'<div class="ox blk"><div class="pt">맞으면 ○, 틀리면 ×</div>'
    f'<div>(7) 1m의 {fr(1, 5)}은 50cm야. (　　)　　(8) 1kg의 {fr(1, 4)}은 250g이야. (　　)</div>'
    f'<div>(9) 1시간의 {fr(1, 2)}은 40분이야. (　　)　(10) 1km의 {fr(1, 2)}은 200m야. (　　)</div></div>',
    words([
        (f"1시간의 {fr(1, 4)} 동안 책을 읽었어요. 책을 읽은 시간은 몇 분일까요?", "분"),
        (f"물 1L의 {fr(3, 5)}를 마셨어요. 마신 물은 몇 mL일까요?", "mL"),
    ], start=11, title=None, space=12),
])))
ANS.append(("2", ["따라 해 봐요: 1000, 1000 × 1/4 = 250g / 60, 60 × 1/3 = 20분", "(1) 75", "(2) 500", "(3) 300",
                  "(4) 400", "(5) 15", "(6) 50", "(7) × (20cm)", "(8) ○", "(9) × (30분)", "(10) × (500m)", "(11) 60 × 1/4 = 15분", "(12) 1000 × 3/5 = 600mL"]))

# 3
L.append(lesson("3", "'분'을 '시간'으로 바꿔요", "10분은 몇 시간일까?", "08", "".join([
    concept("1시간(60분)을 막대로 그려 봐요",
            f'<div class="row"><div>{bar(6, 1, "1시간 = 60분", cell_labels=["10분"] * 6)}</div>'
            f'<div class="side">60분을 10분씩 나누면 <b>6칸</b>이에요.<br>10분은 6칸 중 1칸 → <b>{fr(1, 6)}시간</b><br>'
            f'식으로: 10분 {EQ} {fr(10, 60)}시간 {EQ} {fr(1, 6)}시간</div></div>'
            f'<div class="ex">2시간 10분 {EQ} 2시간 + {fr(1, 6)}시간 {EQ} <b>{mx(2, 1, 6)}시간</b></div>'),
    rule(f"<b>■분 {EQ} {fr('■', 60)}시간</b>　(분모는 항상 <b>60</b>, 그다음 약분해요)"),
    careful(f"10분을 {fr(10, 100)}시간으로 쓰면 틀려요. 1시간은 <b>60분</b>!"),
    follow(f"20분 {EQ} {bfr(20, None)}시간 {EQ} {bfr()}시간<br>1시간 30분 {EQ} 1시간 + {bfr(30, None)}시간 {EQ} 1{bfr()}시간"),
    drills([f"30분 {EQ} {bfr()}시간", f"15분 {EQ} {bfr()}시간", f"40분 {EQ} {bfr()}시간",
            f"45분 {EQ} {bfr()}시간", f"1시간 20분 {EQ} {BL}{bfr()}시간", f"2시간 10분 {EQ} {BL}{bfr()}시간"]),
    words([
        ("한 시간에 3km를 걷는 빠르기로 1시간 20분 동안 걸으면 몇 km를 걸을까요?", "km"),
        (f"한 시간에 {mx(1, 1, 2)}km를 걷는 빠르기로 40분 동안 걸으면 몇 km를 걸을까요?", "km"),
    ], start=7, title=None, space=11),
])))
ANS.append(("3", ["따라 해 봐요: 20/60 = 1/3시간 / 30/60 → 1과 1/2시간", "(1) 1/2", "(2) 1/4", "(3) 2/3",
                  "(4) 3/4", "(5) 1과 1/3", "(6) 2와 1/6",
                  "(7) 1과 1/3 × 3 = 4/3 × 3 = 4km", "(8) 40분 = 2/3시간, 3/2 × 2/3 = 1km"]))

# 4
L.append(lesson("4", "(자연수) × (분수)는 약분 먼저!", "큰 수도 쉽게 계산해요", "01, 13, 14", "".join([
    concept(f"28 {X} {fr(11, 7)}을 계산해 봐요",
            f'<div class="steps"><div>① 28과 분모 7을 <b>7로 약분</b>해요. 28 → 4, 7 → 1</div>'
            f'<div>② 4 {X} {fr(11, 1)} {EQ} 4 {X} 11 {EQ} <b>44</b></div></div>'
            f'<div class="ex">약분을 먼저 하면 28 {X} 11 = 308 같은 큰 계산을 안 해도 돼요.</div>'),
    rule("<b>자연수와 분모를 같은 수로 나눌 수 있으면 먼저 약분</b>하고, 남은 수끼리 곱해요."),
    follow(f"24 {X} {fr(5, 6)} → 24와 6을 {BL}로 약분 → {BL} {X} 5 {EQ} {BL}"),
    drills([f"14 {X} {fr(3, 7)} {EQ} {BL}", f"24 {X} {fr(5, 6)} {EQ} {BL}", f"36 {X} {fr(7, 9)} {EQ} {BL}",
            f"15 {X} {fr(4, 5)} {EQ} {BL}", f"60 {X} {fr(3, 4)} {EQ} {BL}", f"25 {X} {fr(3, 5)} {EQ} {BL}"]),
    words([
        (f"40km를 가는 데 전체의 {fr(3, 8)}은 전철을 탔어요. 전철을 타고 간 거리는 몇 km일까요?", "km"),
        (f"길이가 90cm인 철사의 {fr(2, 5)}를 미술 시간에 썼어요. 쓴 철사는 몇 cm일까요?", "cm"),
    ], start=7, title=None, space=11),
])))
ANS.append(("4", ["따라 해 봐요: 6으로 약분 → 4 × 5 = 20", "(1) 6", "(2) 20", "(3) 28", "(4) 12", "(5) 45", "(6) 15", "(7) 40 × 3/8 = 15km", "(8) 90 × 2/5 = 36cm"]))

# 5
L.append(lesson("5", "대분수는 가분수로 바꿔서 곱해요", f"{mx(1, 4, 7)}은 7조각짜리가 몇 조각?", "01, 08, 19", "".join([
    concept(f"{mx(1, 4, 7)}을 그림으로 봐요",
            f'<div class="row"><div>{bar(7, 7, "1 (7조각)", w=200)}{bar(7, 4, f"4조각", w=200)}</div>'
            f'<div class="side">1은 7조각, 거기에 4조각을 더하면<br>모두 7 + 4 = <b>11조각</b><br>'
            f'→ {mx(1, 4, 7)} {EQ} <b>{fr(11, 7)}</b></div></div>'),
    rule(f"{mx('●', '▲', '■')} {EQ} {fr('■ × ● + ▲', '■')}　　예) {mx(2, 2, 7)} {EQ} {fr('7 × 2 + 2', 7)} {EQ} {fr(16, 7)}"),
    follow(f"28 {X} {mx(1, 4, 7)} {EQ} 28 {X} {bfr(None, 7)} {EQ} {BL}<br>"
           f"{mx(2, 5, 9)} {X} {mx(1, 4, 5)} {EQ} {bfr(None, 9)} {X} {bfr(None, 5)} {EQ} {bfr()} {EQ} {BL}{bfr()}"),
    drills([f"{mx(2, 2, 7)} {EQ} {bfr()}", f"{mx(2, 1, 6)} {EQ} {bfr()}", f"{mx(4, 2, 3)} {EQ} {bfr()}",
            f"21 {X} {mx(2, 2, 7)} {EQ} {BL}", f"12 {X} {mx(1, 3, 4)} {EQ} {BL}", f"{mx(1, 1, 2)} {X} {mx(2, 2, 3)} {EQ} {BL}"]),
    careful("문제에서 <b>'모두'</b>를 물으면 마지막에 꼭 더해요!"),
    words([(f"어제는 28쪽을 읽었고, 오늘은 어제의 {mx(1, 4, 7)}을 읽었어요. ① 오늘은 몇 쪽? ② 어제와 오늘 <u>모두</u> 몇 쪽?", "쪽")],
          start=7, title=None, space=16),
])))
ANS.append(("5", ["따라 해 봐요: 11/7 → 44 / 23/9 × 9/5 = 23/5 = 4와 3/5", "(1) 16/7", "(2) 13/6", "(3) 14/3",
                  "(4) 48", "(5) 21", "(6) 4", "(7) ① 44쪽 ② 72쪽"]))

# 6
L.append(lesson("6", "(분수) × (분수)를 그림으로", "분자는 분자끼리, 분모는 분모끼리", "03, 16", "".join([
    concept(f"{fr(2, 3)} {X} {fr(3, 4)}는 얼마일까요?",
            f'<div class="row"><div>{area(2, 3, 3, 4)}</div>'
            f'<div class="side">① 세로로 3칸 중 <b>2칸</b>을 연하게 칠해요. ({fr(2, 3)})<br>'
            f'② 그중 가로로 4칸 중 <b>3칸</b>을 진하게 칠해요. ({fr(3, 4)})<br>'
            f'③ 전체 12칸 중 진한 칸은 6칸 → {fr(6, 12)} {EQ} <b>{fr(1, 2)}</b><br>'
            f'식으로: {fr("2 × 3", "3 × 4")} {EQ} {fr(6, 12)} {EQ} {fr(1, 2)}</div></div>'),
    rule("분자는 분자끼리, 분모는 분모끼리 곱해요. <b>곱하기 전에 위·아래로 약분</b>하면 더 쉬워요."),
    follow(f"{fr(4, 9)} {X} {fr(5, 6)} → 4와 6을 {BL}로 약분 → {fr(2, 9)} {X} {fr(5, 3)} {EQ} {bfr()}"),
    drills([f"{fr(1, 2)} {X} {fr(1, 4)} {EQ} {bfr()}", f"{fr(2, 3)} {X} {fr(1, 5)} {EQ} {bfr()}",
            f"{fr(3, 4)} {X} {fr(2, 3)} {EQ} {bfr()}", f"{fr(5, 6)} {X} {fr(3, 10)} {EQ} {bfr()}",
            f"{fr(10, 11)} {X} {fr(2, 5)} {EQ} {bfr()}", f"{fr(4, 15)} {X} {fr(3, 8)} {EQ} {bfr()}"]),
    words([(f"케이크 {fr(4, 9)}kg의 {fr(5, 6)}을 세 사람이 똑같이 나누어 먹었어요. ① 세 사람이 먹은 양은? ② 한 사람이 먹은 양은?", "kg")],
          start=7, title=None, space=16),
])))
ANS.append(("6", ["따라 해 봐요: 2로 약분 → 10/27", "(1) 1/8", "(2) 2/15", "(3) 1/2", "(4) 1/4", "(5) 4/11",
                  "(6) 1/10", "(7) ① 10/27kg ② 10/27 × 1/3 = 10/81kg"]))

# 7
L.append(lesson("7", "똑같이 나눈 선분과 수직선", "한 칸은 얼마일까?", "09, 10, 11, 12", "".join([
    concept("전체를 ●칸으로 똑같이 나누면 한 칸은 전체의 " + fr(1, "●"),
            f'<div class="row"><div>{segment(6, total_mixed(4, 2, 3, "m"), {0: "ㄱ", 1: "ㄴ", 2: "ㄷ", 3: "ㄹ", 6: "ㅁ"})}</div>'
            f'<div class="side">전체 {mx(4, 2, 3)}m를 6칸으로 나눴어요.<br>ㄱㄴ은 1칸 → 전체의 {fr(1, 6)}<br>'
            f'{fr(14, 3)} {X} {fr(1, 6)} {EQ} {fr(14, 18)} {EQ} <b>{fr(7, 9)}m</b></div></div>'),
    rule(f"<b>▲칸의 크기 {EQ} 전체 {X} {fr('▲', '●')}</b>　(칸은 눈금과 눈금 <b>사이</b>, 0부터 세요)"),
    follow(f'<div class="row"><div>{nl(8, (4, 15), box_at=3)}</div><div class="side">'
           f'0부터 {fr(4, 15)}까지 8칸<br>한 칸: {fr(4, 15)} {X} {fr(1, 8)} {EQ} {bfr()}<br>'
           f'화살표는 3칸: {bfr()} {X} 3 {EQ} {bfr()} {EQ} {bfr()}</div></div>'),
    '<div class="pt">연습해요</div>',
    f'<div class="figq blk"><div class="dr"><span class="qn">(1)</span>빈칸에 알맞은 수는?</div>{nl(4, 1, box_at=3)}</div>'
    f'<div class="figq blk"><div class="dr"><span class="qn">(2)</span>빈칸에 알맞은 수는?</div>{nl(7, (7, 18), box_at=3)}</div>'
    f'<div class="figq blk"><div class="dr"><span class="qn">(3)</span>빈칸에 알맞은 수는?</div>{nl(4, (2, 3), box_at=1)}</div>'
    f'<div class="figq blk"><div class="dr"><span class="qn">(4)</span>선분 ㄱㄷ의 길이는?</div>{segment(3, total_text("6 m"), {0: "ㄱ", 1: "ㄴ", 2: "ㄷ", 3: "ㄹ"})}</div>',
])))
ANS.append(("7", ["따라 해 봐요: 1/30, 1/30 × 3 = 3/30 = 1/10", "(1) 3/4", "(2) 1/6 (3/18)", "(3) 1/6 (2/12)", "(4) 4m (2칸)"]))

# 8
L.append(lesson("8", "'나머지의 ~'는 차례차례", "먼저 나머지를 구해요", "13, 14", "".join([
    concept("40km 중 " + fr(3, 8) + "은 전철, 나머지의 " + fr(3, 5) + "은 버스, 그 나머지는 걸었어요",
            f'<div class="row"><div>{bar(8, 3, "40 km", note=["전철"] * 3 + [""] * 5)}</div>'
            f'<div class="side">① 전철: 40 {X} {fr(3, 8)} {EQ} 15km<br>② 나머지: 40 − 15 {EQ} <b>25km</b></div></div>'
            f'<div class="row"><div>{bar(5, 3, "나머지 25 km", note=["버스"] * 3 + ["걸음"] * 2)}</div>'
            f'<div class="side">③ 버스: <b>25</b> {X} {fr(3, 5)} {EQ} 15km<br>④ 걸어간 거리: 25 − 15 {EQ} <b>10km</b></div></div>'),
    careful(f"버스는 40km의 {fr(3, 5)}이 아니라 <b>나머지 25km</b>의 {fr(3, 5)}이에요."),
    follow(f"철사 90cm 중 {fr(2, 5)}를 쓰고, 나머지의 {fr(2, 3)}를 친구에게 줬어요. 남은 철사는?<br>"
           f"① 쓴 철사: 90 {X} {fr(2, 5)} {EQ} {BL}　② 나머지: 90 − {BL} {EQ} {BL}<br>"
           f"③ 준 철사: {BL} {X} {fr(2, 3)} {EQ} {BL}　④ 남은 철사: {BL} − {BL} {EQ} {BL}cm"),
    words([
        (f"60쪽짜리 책의 {fr(1, 3)}을 어제 읽고, 나머지의 {fr(1, 2)}을 오늘 읽었어요. 남은 쪽수는?", "쪽"),
        (f"사과 24개 중 {fr(1, 4)}을 먹고, 나머지의 {fr(2, 3)}를 이웃에게 주었어요. 남은 사과는?", "개"),
        (f"리본 100cm 중 {fr(3, 10)}을 쓰고, 나머지의 {fr(4, 7)}를 또 썼어요. 남은 리본은?", "cm"),
    ], space=14),
])))
ANS.append(("8", ["따라 해 봐요: 36, 36, 54, 54 × 2/3 = 36, 54 − 36 = 18cm", "(1) 20 → 40 → 20 → 20쪽",
                  "(2) 6 → 18 → 12 → 6개", "(3) 30 → 70 → 40 → 30cm"]))

# 9
L.append(lesson("9", "남은 양으로 처음 양 구하기", "남은 것이 전체의 얼마인지 먼저!", "17, 18", "".join([
    concept(f"빵의 {fr(3, 4)}을 팔고 15개가 남았어요. 처음 빵은?",
            f'<div class="row"><div>{bar(4, 0, "처음 빵 ?개", shade2=3, note=["판 빵"] * 3 + ["15개"])}</div>'
            f'<div class="side">① 남은 빵은 1 − {fr(3, 4)} {EQ} <b>{fr(1, 4)}</b><br>'
            f'② 4칸 중 1칸이 15개<br>③ 4칸은 15 {X} 4 {EQ} <b>60개</b></div></div>'),
    careful("15개는 판 빵이 아니라 <b>남은 빵</b>이에요."),
    follow(f"색종이 60장을 학생들이 한 장씩 가졌더니 전체의 {fr(1, 5)}이 남았어요. 학생은 몇 명?<br>"
           f"① 남은 색종이: 60 {X} {fr(1, 5)} {EQ} {BL}장<br>② 가져간 색종이: 60 − {BL} {EQ} {BL}장<br>③ 학생 수: {BL}명"),
    words([
        (f"사탕의 {fr(2, 3)}를 먹었더니 10개가 남았어요. 처음 사탕은 몇 개?", "개"),
        (f"스티커의 {fr(3, 5)}를 썼더니 8장이 남았어요. 처음 스티커는 몇 장?", "장"),
        (f"구슬 40개를 친구들에게 한 개씩 나누어 주었더니 전체의 {fr(1, 4)}이 남았어요. 친구는 몇 명?", "명"),
    ], space=20),
])))
ANS.append(("9", ["따라 해 봐요: 12, 12, 48, 48명", "(1) 남은 1/3이 10개 → 30개", "(2) 남은 2/5가 8장 → 1/5은 4장 → 20장",
                  "(3) 남은 구슬 10개, 나눠 준 30개 → 30명"]))

# 10
L.append(lesson("10", "어떤 수를 잘못 계산했을 때", "거꾸로 생각해서 어떤 수부터!", "15, 16", "".join([
    concept("먼저 쉬운 수로 연습해요",
            f'<div class="ex">어떤 수에 3을 <b>곱해야</b> 할 것을 잘못하여 <b>더했더니</b> 10이 되었어요.</div>'
            f'<div class="steps"><div>① 잘못한 식: 어떤 수 + 3 {EQ} 10</div>'
            f'<div>② 거꾸로: 어떤 수 {EQ} 10 − 3 {EQ} <b>7</b>　(더했으면 빼고, 뺐으면 더해요)</div>'
            f'<div>③ 바른 계산: 7 {X} 3 {EQ} <b>21</b></div></div>'),
    rule("① 잘못한 식 쓰기 → ② 거꾸로 어떤 수 구하기 → ③ 바르게 계산하기"),
    concept("분수도 똑같아요",
            f'<div class="ex">어떤 수에 {fr(2, 5)}를 곱해야 할 것을 잘못하여 <b>뺐더니</b> {fr(28, 55)}이 되었어요.</div>'
            f'<div class="steps"><div>① 어떤 수 − {fr(2, 5)} {EQ} {fr(28, 55)}</div>'
            f'<div>② 어떤 수 {EQ} {fr(28, 55)} + {fr(2, 5)} {EQ} {fr(28, 55)} + {fr(22, 55)} {EQ} {fr(50, 55)} {EQ} <b>{fr(10, 11)}</b>　(통분: 분모를 55로)</div>'
            f'<div>③ {fr(10, 11)} {X} {fr(2, 5)} {EQ} <b>{fr(4, 11)}</b></div></div>'),
    words([
        (f"어떤 수에 {fr(1, 2)}을 곱해야 할 것을 잘못하여 더했더니 {fr(5, 6)}이 되었어요. 바르게 계산하면?", ""),
        (f"어떤 수에 {fr(3, 4)}을 곱해야 할 것을 잘못하여 뺐더니 {fr(1, 8)}이 되었어요. 바르게 계산하면?", ""),
        (f"어떤 수에서 {fr(1, 3)}을 빼고 6을 곱해야 할 것을 잘못하여 {fr(1, 3)}을 빼고 6을 더했더니 {mx(6, 2, 5)}가 되었어요. 바르게 계산하면?<br>"
         f'<span class="hint">힌트: (어떤 수 − {fr(1, 3)})를 한 덩어리로 생각해요.</span>', ""),
    ], space=14),
])))
ANS.append(("10", ["(1) 어떤 수 = 5/6 − 1/2 = 1/3 → 1/3 × 1/2 = 1/6", "(2) 어떤 수 = 1/8 + 3/4 = 7/8 → 7/8 × 3/4 = 21/32",
                   "(3) 덩어리 = 6과 2/5 − 6 = 2/5 → 2/5 × 6 = 12/5 = 2와 2/5"]))

# 11
L.append(lesson("11", "□ 안에 들어갈 자연수", "대분수 크기 비교", "19", "".join([
    concept("대분수는 자연수 부분부터 비교해요",
            f'<div class="steps"><div>① 자연수 부분이 크면 더 커요. {mx(4, 1, 5)} {LT} {mx(5, 1, 5)}</div>'
            f'<div>② 자연수 부분이 같으면 <b>분수 부분</b>을 비교해요. {mx(4, 2, 5)} {LT} {mx(4, 3, 5)}</div></div>'
            f'<div class="ex"><span class="mx">{BOX}{fr(1, 3)}</span>{LT}{mx(3, 2, 3)} → □에 1, 2를 넣으면 당연히 작아요.<br>'
            f'□ = 3이면 {mx(3, 1, 3)}와 {mx(3, 2, 3)}: 분수 부분 {fr(1, 3)} {LT} {fr(2, 3)}이니까 <b>된다!</b> → 1, 2, 3 → <b>3개</b></div>'),
    careful("□가 오른쪽 자연수와 <b>같을 때</b>를 꼭 확인해요. 가장 많이 빠뜨려요."),
    follow(f"<span class=\"mx\">{BOX}{fr(2, 5)}</span>{LT}{mx(2, 5, 9)} {X} {mx(1, 4, 5)}<br>"
           f"① 오른쪽 계산: {fr(23, 9)} {X} {fr(9, 5)} {EQ} {bfr()} {EQ} {BL}{bfr()}<br>"
           f"② □ = 4일 때: {mx(4, 2, 5)}와 {mx(4, 3, 5)} 비교 → (된다 / 안 된다)　③ 답: {BL}개"),
    words([
        (f"<span class=\"mx\">{BOX}{fr(3, 4)}</span>{LT}{mx(2, 1, 4)}　□ 안에 들어갈 수 있는 자연수는 몇 개?", "개"),
        (f"<span class=\"mx\">{BOX}{fr(1, 5)}</span>{LT}{mx(3, 4, 5)}　□ 안에 들어갈 수 있는 자연수는 몇 개?", "개"),
        (f"<span class=\"mx\">{BOX}{fr(1, 2)}</span>{LT}{mx(1, 1, 2)} {X} 3　□ 안에 들어갈 수 있는 자연수는 몇 개?", "개"),
    ], space=18),
])))
ANS.append(("11", ["따라 해 봐요: 23/5 = 4와 3/5, 된다, 4개", "(1) □=2이면 2와 3/4 > 2와 1/4 → 1만 → 1개",
                   "(2) 1, 2, 3 → 3개", "(3) 오른쪽 = 9/2 = 4와 1/2, □=4이면 같아서 안 됨 → 1, 2, 3 → 3개"]))

# 실력 확인
CHECK = [
    (f"민호는 어제 21쪽을 읽었고, 오늘은 어제의 {mx(1, 2, 3)}을 읽었어요. 어제와 오늘 읽은 쪽수는 모두 몇 쪽?", "쪽"),
    (f"한 시간에 {mx(1, 1, 5)}km를 걷는 빠르기로 하루에 1시간 40분씩 3일 동안 걸으면 모두 몇 km?", "km"),
    (f"50km를 가는 데 전체의 {fr(2, 5)}는 기차를 타고, 나머지의 {fr(1, 3)}은 버스를 타고, 그 나머지는 걸었어요. 걸어간 거리는?", "km"),
    (f"가게에서 처음 있던 빵의 {fr(2, 3)}를 팔았더니 12개가 남았어요. 처음 빵은 몇 개?", "개"),
    (f"어떤 수에 {fr(3, 4)}을 곱해야 할 것을 잘못하여 뺐더니 {fr(1, 12)}이 되었어요. 바르게 계산하면?", ""),
    (f"<span class=\"mx\">{BOX}{fr(1, 4)}</span>{LT}{mx(1, 1, 2)} {X} {mx(2, 1, 3)}　□ 안에 들어갈 수 있는 자연수는 몇 개?", "개"),
]
L.append('<section class="lesson"><div class="lh"><span class="ln">✓</span><div><div class="lt">실력 확인</div>'
         '<div class="ls">오답 문제와 비슷한 문제예요. 배운 대로 풀어 봐요!</div></div></div>'
         + words(CHECK, title=None, space=22) + "</section>")
ANS.append(("실력 확인", ["(1) 21 × 5/3 = 35, 21 + 35 = 56쪽", "(2) 1시간 40분 = 1과 2/3시간, 6/5 × 5/3 = 2km, 2 × 3 = 6km",
                         "(3) 기차 20 → 나머지 30 → 버스 10 → 걸음 20km", "(4) 남은 1/3이 12개 → 36개",
                         "(5) 어떤 수 = 1/12 + 9/12 = 5/6 → 5/6 × 3/4 = 5/8",
                         "(6) 3/2 × 7/3 = 7/2 = 3과 1/2, □=3이면 3과 1/4 < 3과 1/2 → 1, 2, 3 → 3개"]))


TOC = [("1", "'~의 ~'는 곱셈이에요", "10"), ("2", "단위를 바꾸면 쉬워요", "05, 06"), ("3", "'분'을 '시간'으로 바꿔요", "08"),
       ("4", "(자연수) × (분수)는 약분 먼저", "01, 13, 14"), ("5", "대분수는 가분수로 바꿔서", "01, 08, 19"),
       ("6", "(분수) × (분수)를 그림으로", "03, 16"), ("7", "똑같이 나눈 선분과 수직선", "09~12"),
       ("8", "'나머지의 ~'는 차례차례", "13, 14"), ("9", "남은 양으로 처음 양 구하기", "17, 18"),
       ("10", "어떤 수를 잘못 계산했을 때", "15, 16"), ("11", "□ 안에 들어갈 자연수", "19"), ("✓", "실력 확인", "전체")]


CSS = """
@page { size: A4; margin: 12mm 13mm 14mm; }
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif; color: #000; font-size: 11.5pt; word-break: keep-all; }
.fr { display: inline-flex; flex-direction: column; align-items: center; vertical-align: middle; font-size: 1em; line-height: 1.05; margin: 0 0.15em; }
.fr > span:first-child { border-bottom: 1.2px solid #000; padding: 0 0.15em; }
.fr > span:last-child { padding: 0 0.15em; }
.mx { white-space: nowrap; }
.mx > .fr { margin-left: 0.02em; }
.op { font-family: 'DejaVu Sans', sans-serif; font-size: 0.95em; margin: 0 0.25em; }
.box { display: inline-block; width: 1.1em; height: 1.25em; border: 1.4px solid #000; vertical-align: middle; }
.bl { display: inline-block; min-width: 2.4em; height: 1.45em; border: 1.3px solid #555; border-radius: 1mm; vertical-align: middle; margin: 0 0.15em; }
.sb { display: inline-block; width: 1.5em; height: 1.2em; border: 1.1px solid #555; border-radius: 0.8mm; margin: 0.08em 0; }
.blk { break-inside: avoid; }
.cover { text-align: left; }
.cover .t1 { font-size: 12pt; color: #1d6b4f; font-weight: bold; }
.cover .t2 { font-size: 24pt; font-weight: bold; margin: 2mm 0 1mm; }
.cover .t3 { font-size: 12pt; color: #444; border-bottom: 2.5px solid #1d6b4f; padding-bottom: 4mm; margin-bottom: 6mm; }
.how { background: #f2f8f5; border-radius: 2mm; padding: 4mm 5mm; margin-bottom: 6mm; line-height: 1.9; }
.how b { color: #1d6b4f; }
table.toc { width: 100%; border-collapse: collapse; }
table.toc td { padding: 2.2mm 2mm; border-bottom: 1px dotted #bbb; }
table.toc td.n { width: 12mm; color: #1d6b4f; font-weight: bold; font-size: 13pt; }
table.toc td.l { width: 32mm; color: #777; font-size: 10pt; text-align: right; }
table.toc td.c { width: 22mm; }
.lesson { break-before: page; }
.lh { display: flex; align-items: center; gap: 4mm; border-bottom: 2.5px solid #1d6b4f; padding-bottom: 3mm; margin-bottom: 4mm; }
.ln { background: #1d6b4f; color: #fff; font-weight: bold; font-size: 15pt; min-width: 11mm; height: 11mm; border-radius: 2mm; display: inline-flex; align-items: center; justify-content: center; padding: 0 2mm; }
.lt { font-size: 17pt; font-weight: bold; }
.ls { font-size: 10.5pt; color: #555; }
.linked { margin-left: auto; font-size: 9.5pt; color: #1d6b4f; border: 1px solid #1d6b4f; border-radius: 3mm; padding: 0.5mm 3mm; white-space: nowrap; }
.concept { border: 1.5px solid #3f78b5; border-radius: 2mm; padding: 3mm 4mm; margin-bottom: 3.5mm; }
.ct { font-weight: bold; color: #24548a; margin-bottom: 2mm; font-size: 12pt; }
.row { display: flex; align-items: center; gap: 5mm; margin: 1.5mm 0; }
.side { line-height: 1.9; flex: 1; }
.row > div:first-child { flex: none; }
.ex { margin-top: 2mm; line-height: 2; }
.steps > div { line-height: 2.1; }
.rule { background: #d6ebe0; border-left: 4px solid #1d6b4f; border-radius: 2mm; padding: 2.5mm 4mm; margin-bottom: 3.5mm; line-height: 2; }
.rt { display: inline-block; background: #1d6b4f; color: #fff; font-size: 9.5pt; font-weight: bold; border-radius: 1mm; padding: 0 2mm; margin-right: 3mm; }
.careful { background: #fff7e0; border-left: 3px solid #e0a800; padding: 2mm 4mm; margin-bottom: 3.5mm; line-height: 1.9; }
.careful b:first-child { color: #9a6b00; }
.follow { border: 1.5px dashed #1d6b4f; border-radius: 2mm; padding: 3mm 4mm; margin-bottom: 4mm; line-height: 2.5; }
.ft { font-weight: bold; color: #1d6b4f; line-height: 1.6; margin-bottom: 1mm; }
.hint { font-weight: normal; color: #777; font-size: 9.5pt; margin-left: 2mm; }
.pt { font-weight: bold; color: #1d6b4f; font-size: 12pt; margin: 2mm 0 2mm; }
.drills .grid { display: grid; grid-template-columns: 1fr 1fr; column-gap: 8mm; row-gap: 1mm; }
.dr { line-height: 2.6; }
.qn { color: #1d6b4f; font-weight: bold; margin-right: 2mm; }
.units { border-collapse: collapse; margin-bottom: 1mm; }
.units td { border: 1px solid #aac; padding: 1mm 4mm; }
.ox > div { line-height: 2.4; }
.wp { border-top: 1px dashed #ccc; padding-top: 2mm; margin-top: 1mm; }
.wq { display: flex; line-height: 2; }
.wans { text-align: right; }
.wans .u { display: inline-block; width: 38mm; text-align: right; }
.figq { display: inline-block; width: 49%; vertical-align: top; margin-bottom: 2mm; }
.answers { break-before: page; }
.answers h2 { font-size: 17pt; border-bottom: 2.5px solid #1d6b4f; padding-bottom: 3mm; margin: 0 0 4mm; }
.abody { columns: 2; column-gap: 9mm; }
.ag { display: inline-block; width: 100%; break-inside: avoid; margin-bottom: 4mm; }
.ag .h { font-weight: bold; color: #1d6b4f; }
.ag .items { line-height: 2.2; font-size: 10.5pt; padding-left: 4mm; }
"""


def fmt(t):
    """정답 텍스트의 'A와 B/C', 'B/C', '×'를 본문과 같은 수식 모양으로."""
    import re
    t = re.sub(r"(\d+)[와과] (\d+)/(\d+)", lambda m: mx(*m.groups()), t)
    t = re.sub(r"(?<![\d<])(\d+)/(\d+)", lambda m: fr(*m.groups()), t)
    return t.replace("×", X).replace("□", BOX)


def main():
    toc = "".join(f'<tr><td class="n">{n}</td><td>{t}</td><td class="l">오답 {l}번</td></tr>' for n, t, l in TOC)
    cover = (
        '<div class="cover"><div class="t1">5학년 2학기 · 2. 분수의 곱셈</div>'
        '<div class="t2">개념부터 차근차근</div>'
        '<div class="t3">틀렸던 문제 유형을 아주 쉬운 것부터 다시 익혀요</div>'
        '<div class="how"><b>이렇게 공부해요</b><br>'
        '① <b>개념</b> 상자의 그림을 보며 왜 그런지 이해해요.<br>'
        '② <b>기억해요</b>의 규칙을 소리 내어 읽어요.<br>'
        '③ <b>따라 해 봐요</b>의 빈칸을 채워요. 막히면 개념 상자를 다시 봐요.<br>'
        '④ <b>연습해요</b>를 혼자 풀고, 맨 뒤 정답으로 채점해요.<br>'
        '⑤ 다 끝나면 <b>실력 확인</b>을 풀고, 오답 문제지를 다시 풀어 봐요.</div>'
        f'<table class="toc">{toc}</table></div>'
    )
    ans = '<section class="answers"><h2>정답</h2><div class="abody">' + "".join(
        f'<div class="ag"><div class="h">{("" if n == "실력 확인" else "")}{n if n == "실력 확인" else n + "차시"}</div>'
        f'<div class="items">{"<br>".join(fmt(t) for t in items)}</div></div>' for n, items in ANS) + "</div></section>"
    html = (
        '<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        f'<title>분수의 곱셈 개념 문제집</title><style>{CSS}</style></head><body>'
        + cover + "".join(L) + ans + "</body></html>"
    )
    with open("workbook.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()

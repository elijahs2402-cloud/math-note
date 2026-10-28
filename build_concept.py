"""2026.10.27 오답노트 개념 문제집(A4) HTML 생성기.

오답노트 9문제(수학 4, 사회 5)의 개념을 처음부터 쉽게 익히도록 8차시로 묶었다.
사회는 차시마다 '이야기로 풀어 보기'가 들어간다.
python3 build_concept.py  ->  concept.html  (Chromium으로 concept.pdf 출력)
"""

X = '<span class="op">×</span>'
CIRC = "①②③④⑤"


# ---------- SVG ----------
def numline(lo, hi, left=None, right=None, ray=None, width=330, label_every=1, blank=False):
    """lo~hi 수직선. left/right = (값, 색칠 여부). ray='right'면 left부터 오른쪽 끝까지."""
    n = hi - lo
    x0, x1, y = 15, width - 15, 18
    step = (x1 - x0) / n
    X_ = lambda v: x0 + (v - lo) * step
    s = [f'<svg viewBox="0 0 {width} 44" width="{width}" height="44">',
         f'<line x1="0" y1="{y}" x2="{width}" y2="{y}" stroke="#000" stroke-width="1.3"/>']
    for i in range(n + 1):
        v = lo + i
        s.append(f'<line x1="{X_(v)}" y1="{y - 6}" x2="{X_(v)}" y2="{y + 6}" stroke="#000" stroke-width="1.3"/>')
        if not blank and i % label_every == 0:
            s.append(f'<text x="{X_(v)}" y="{y + 22}" font-size="13" text-anchor="middle">{v}</text>')
    a = X_(left[0]) if left else 0
    b = X_(right[0]) if right else width
    if ray == "right":
        b = width - 2
    if ray == "left":
        a = 2
    if left or right:
        s.append(f'<line x1="{a}" y1="{y}" x2="{b}" y2="{y}" stroke="#1d6b4f" stroke-width="5"/>')
    for p in (left, right):
        if p:
            fill = "#1d6b4f" if p[1] else "#fff"
            s.append(f'<circle cx="{X_(p[0])}" cy="{y}" r="5.5" fill="{fill}" stroke="#1d6b4f" stroke-width="2"/>')
    s.append("</svg>")
    return "".join(s)


def thousands_line():
    """1000~4000, 2000 초과 3000 이하가 3000이 된다."""
    W, x0, x1, y = 330, 20, 310, 18
    step = (x1 - x0) / 3
    s = [f'<svg viewBox="0 0 {W} 44" width="{W}" height="44">',
         f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#000" stroke-width="1.3"/>']
    for i, v in enumerate([1000, 2000, 3000, 4000]):
        x = x0 + i * step
        s.append(f'<line x1="{x}" y1="{y - 6}" x2="{x}" y2="{y + 6}" stroke="#000" stroke-width="1.3"/>')
        s.append(f'<text x="{x}" y="{y + 22}" font-size="13" text-anchor="middle">{v}</text>')
    a, b = x0 + step, x0 + 2 * step
    s.append(f'<line x1="{a}" y1="{y}" x2="{b}" y2="{y}" stroke="#1d6b4f" stroke-width="5"/>')
    s.append(f'<circle cx="{a}" cy="{y}" r="5.5" fill="#fff" stroke="#1d6b4f" stroke-width="2"/>')
    s.append(f'<circle cx="{b}" cy="{y}" r="5.5" fill="#1d6b4f" stroke="#1d6b4f" stroke-width="2"/>')
    s.append("</svg>")
    return "".join(s)


def buses(n, cap, full, caption):
    """버스 n대. full=True면 모두 꽉 찬 색."""
    W = 34 * n + 8
    s = [f'<svg viewBox="0 0 {W} 40" width="{W}" height="40">']
    for i in range(n):
        x = 4 + i * 34
        fill = "#d6ebe0" if full else "#fff"
        s.append(f'<rect x="{x}" y="4" width="30" height="20" fill="{fill}" stroke="#000" stroke-width="1.2"/>')
        s.append(f'<circle cx="{x + 7}" cy="26" r="3.5" fill="#000"/><circle cx="{x + 23}" cy="26" r="3.5" fill="#000"/>')
        s.append(f'<text x="{x + 15}" y="18" font-size="10" text-anchor="middle">{cap}</text>')
    s.append("</svg>")
    return f'<div class="stage">{"".join(s)}<div class="cap">{caption}</div></div>'


def stages(*items):
    return '<div class="stages">' + '<div class="arr">→</div>'.join(items) + "</div>"


def pair(*items):
    return '<div class="stages" style="gap: 12mm">' + "".join(items) + "</div>"


def stage(svg, caption):
    return f'<div class="stage">{svg}<div class="cap">{caption}</div></div>'


# ---------- 블록 ----------
def lesson(no, subj, title, sub, linked, body):
    return (
        f'<section class="lesson"><div class="lh"><span class="ln">{no}차시</span>'
        f'<div><div class="lt">{title}</div><div class="ls">{subj} · {sub}</div></div>'
        f'<span class="linked">오답노트 {linked}</span></div>{body}</section>'
    )


def concept(title, body):
    return f'<div class="concept blk"><div class="ct">{title}</div>{body}</div>'


def rule(body):
    return f'<div class="rule blk"><span class="rt">기억해요</span>{body}</div>'


def careful(body):
    return f'<div class="careful blk"><b>조심!</b> {body}</div>'


def picture(no, caption):
    """img/social{no}.jpg (Higgsfield로 만든 그림)이 있으면 넣는다."""
    import os
    path = f"img/social{no}.jpg"
    if not os.path.exists(path):
        return ""
    return f'<figure class="pic blk"><img src="{path}"><figcaption>{caption}</figcaption></figure>'


def story(title, scenes, pic=""):
    rows = "".join(f'<div class="scene"><span class="sn">장면 {i + 1}</span><div>{t}</div></div>'
                   for i, t in enumerate(scenes))
    return f'<div class="story blk"><div class="st">이야기로 풀어 보기 · {title}</div>{pic}{rows}</div>'


def timeline(points):
    """[(연도, 사건)] 가로 연표."""
    cells = "".join(f'<div class="tp"><div class="ty">{y}</div><div class="te">{e}</div></div>' for y, e in points)
    return f'<div class="tl blk">{cells}</div>'


def practice(title, qs, cols=1):
    """qs: 문제 HTML 목록. 번호는 자동."""
    cls = "grid2" if cols == 2 else "grid1"
    body = "".join(f'<div class="dr"><span class="qn">{i + 1}</span>{q}</div>' for i, q in enumerate(qs))
    return f'<div class="pt">{title}</div><div class="{cls}">{body}</div>'


PAREN = '<span class="paren">(&emsp;&emsp;&emsp;&emsp;)</span>'
LINE = '<div class="wline"></div>'


def blank(w=20):
    return f'<span class="u" style="width:{w}mm"></span>'


def pick(nums):
    return '<div class="picks">' + "".join(f"<span>{v}</span>" for v in nums) + "</div>"


# ---------- 수학 ----------
L1 = lesson(1, "수학", "이상과 이하", "그 수가 들어가요", "수학 2번", "".join([
    concept("놀이공원에서 생각해 봐요", (
        '<div class="side">롤러코스터 앞에 <b>"키 130 cm 이상만 탈 수 있어요"</b>라고 쓰여 있어요. '
        '키가 딱 130 cm인 친구도 탈 수 있을까요? <b>네, 탈 수 있어요.</b> '
        '130과 같거나 130보다 큰 수를 <b>130 이상</b>인 수라고 해요.</div>'
        + stages(
            stage(numline(126, 134, left=(130, True), width=260), "① 130에 색칠한 동그라미"),
            stage(numline(126, 134, left=(130, True), ray="right", width=260), "② 큰 쪽(오른쪽)으로 선"),
        )
        + '<div class="side">엘리베이터에 <b>"10명 이하"</b>라고 쓰여 있으면 딱 10명까지 탈 수 있어요. '
        '10과 같거나 10보다 작은 수를 <b>10 이하</b>인 수라고 해요.</div>'
        + stages(stage(numline(6, 14, right=(10, True), ray="left"), "10 이하: 10에 색칠, 작은 쪽(왼쪽)으로 선"))
    )),
    rule("<b>이상</b>, <b>이하</b>는 그 수가 <b>들어가요</b>. 수직선에는 <b>색칠한 동그라미(●)</b>로 나타내요."),
    practice("따라 해 봐요", [
        "15 이상인 수에 모두 ○ 하세요." + pick(["13", "15", "14.9", "20", "16.5"]),
        "30 이하인 수에 모두 ○ 하세요." + pick(["31", "30", "29.5", "18", "30.1"]),
        "수직선에 나타낸 수의 범위를 쓰세요.<div class='fig'>" + numline(20, 28, left=(24, True), ray="right", width=290)
        + "</div><div class='wans'>( " + blank(14) + " 이상 )</div>",
        "수직선에 나타낸 수의 범위를 쓰세요.<div class='fig'>" + numline(4, 12, right=(7, True), ray="left", width=290)
        + "</div><div class='wans'>( " + blank(14) + " 이하 )</div>",
        "40 이상 45 이하인 자연수를 모두 쓰세요.<div class='wans'>( " + blank(50) + " )</div>",
    ], cols=2),
]))

L2 = lesson(2, "수학", "초과와 미만", "그 수는 빠져요", "수학 8번", "".join([
    concept("동그라미 모양을 먼저 봐요", (
        '<div class="side"><b>초과</b>는 그 수보다 <b>큰</b> 수, <b>미만</b>은 그 수보다 <b>작은</b> 수예요. '
        '이때 그 수 자신은 <b>빠져요</b>. 그래서 수직선에는 속이 빈 동그라미(○)를 그려요.</div>'
        + pair(
            stage(numline(16, 25, left=(19, False), ray="right", width=250), "19 초과: 19는 빠져요"),
            stage(numline(16, 25, right=(23, False), ray="left", width=250), "23 미만: 23은 빠져요"),
        )
        + '<div class="side">두 조건을 합치면 <b>범위</b>가 돼요. 오답노트 8번 수직선을 순서대로 읽어 봐요.</div>'
        + stages(
            stage(numline(17, 24, left=(19, False), width=188), "① 왼쪽 끝 ○ → 19 초과"),
            stage(numline(17, 24, right=(23, True), width=188), "② 오른쪽 끝 ● → 23 이하"),
            stage(numline(17, 24, left=(19, False), right=(23, True), width=188), "③ 19 초과 23 이하"),
        )
    )),
    rule("● 색칠 = 이상·이하 = 그 수가 <b>들어가요</b>&emsp;&emsp;○ 빈칸 = 초과·미만 = 그 수가 <b>빠져요</b>"),
    careful("19 초과 23 이하에 19는 들어가지 않지만, 19.1이나 22.5처럼 <b>소수</b>도 범위 안이면 들어가요."),
    practice("따라 해 봐요", [
        "19 초과 23 이하인 수에 모두 ○ 하세요." + pick(["19", "19.1", "23", "23.5", "21"]),
        "수직선에 나타낸 수의 범위를 쓰세요.<div class='fig'>" + numline(10, 18, left=(12, True), right=(16, False))
        + "</div><div class='wans'>( " + blank(60) + " )</div>",
        "수직선에 나타낸 수의 범위를 쓰세요.<div class='fig'>" + numline(30, 38, left=(31, False), right=(35, True))
        + "</div><div class='wans'>( " + blank(60) + " )</div>",
        "8 초과 12 미만인 자연수를 모두 쓰세요.<div class='wans'>( " + blank(40) + " )</div>",
    ]),
]))

L3 = lesson(3, "수학", "버스 문제로 범위 구하기", "몇 대가 필요할까요", "수학 2번, 9번", "".join([
    concept("정원 40명 버스가 5대 필요하다면?", (
        '<div class="side">"5대가 필요하다"는 말에는 두 가지 뜻이 숨어 있어요. '
        '<b>4대로는 모자라고</b>, <b>5대면 모두 탈 수 있다</b>는 뜻이에요.</div>'
        + stages(
            buses(4, "40", True, f"① 4대: 40{X}4 = 160명<br>이걸로는 모자라요<br>→ <b>160명 초과</b>"),
            buses(5, "40", True, f"② 5대: 40{X}5 = 200명<br>모두 탈 수 있어요<br>→ <b>200명 이하</b>"),
        )
        + '<div class="side">그래서 학생 수는 <b>160명 초과 200명 이하</b>예요. '
        '사람 수는 자연수이니까 <b>161명 이상 200명 이하</b>라고 말해도 같아요.</div>'
    )),
    rule("버스가 □대 필요하면&emsp;(□보다 1 작은 대수) × 정원 <b>초과</b>,&emsp;□대 × 정원 <b>이하</b>"),
    careful("문제에서 <b>이상과 이하</b>로 나타내라고 하면 초과 쪽에 1을 더해요. 160 초과 → <b>161 이상</b>."),
    practice("따라 해 봐요", [
        "정원이 30명인 버스가 4대 필요해요. 학생 수의 범위를 초과와 이하로 쓰세요."
        "<div class='wans'>( " + blank(14) + "명 초과 " + blank(14) + "명 이하 )</div>",
        "정원이 45명인 버스가 3대 필요해요. 학생 수의 범위를 이상과 이하로 쓰세요."
        "<div class='wans'>( " + blank(14) + "명 이상 " + blank(14) + "명 이하 )</div>",
        "사과를 한 상자에 10개씩 담으면 상자가 최소 6개 필요해요. 사과 수의 범위를 이상과 이하로 쓰세요."
        "<div class='wans'>( " + blank(14) + "개 이상 " + blank(14) + "개 이하 )</div>",
    ]),
]))

L4 = lesson(4, "수학", "올림", "모자라면 하나 더", "수학 13번", "".join([
    concept("1000원짜리 지폐로만 낸다면?", (
        '<div class="side">2763원짜리 물건을 1000원짜리 지폐로만 사려면 몇 장이 필요할까요? '
        '2장(2000원)으로는 모자라니 <b>3장(3000원)</b>을 내야 해요. '
        '이렇게 구하려는 자리 아래에 수가 조금이라도 있으면 <b>그 자리 수를 1 올리고</b> 아래를 0으로 만드는 것을 <b>올림</b>이라고 해요.</div>'
        + '<table class="tbl"><tr><th>수</th><th>천의 자리 아래</th><th>올림하여 천의 자리까지</th></tr>'
        '<tr><td>2763</td><td>763 (있어요)</td><td><b>3000</b></td></tr>'
        '<tr><td>2002</td><td>2 (있어요)</td><td><b>3000</b></td></tr>'
        '<tr><td>3000</td><td>0 (없어요)</td><td><b>3000</b> 그대로</td></tr>'
        '<tr><td>3005</td><td>5 (있어요)</td><td><b>4000</b></td></tr>'
        '<tr><td>1980</td><td>980 (있어요)</td><td><b>2000</b></td></tr></table>'
        + '<div class="side">올림하여 3000이 되는 수를 수직선에 나타내면 <b>2000 초과 3000 이하</b>예요.</div>'
        + stages(stage(thousands_line(), "2000은 그대로 2000, 3000은 그대로 3000"))
    )),
    rule("올림하여 천의 자리까지 나타내서 <b>3000</b>이 되는 수는 <b>2001부터 3000까지</b>예요."),
    careful("3005처럼 3000보다 조금만 커도 올림하면 <b>4000</b>이 돼요. 버림, 반올림과 헷갈리지 않게 해요."),
    practice("따라 해 봐요", [
        "올림하여 천의 자리까지 나타내세요.<div class='row4'><span>4120 → " + blank(14) + "</span><span>5000 → "
        + blank(14) + "</span><span>6001 → " + blank(14) + "</span><span>7999 → " + blank(14) + "</span></div>",
        "올림하여 백의 자리까지 나타내세요.<div class='row4'><span>351 → " + blank(14) + "</span><span>600 → "
        + blank(14) + "</span><span>1208 → " + blank(14) + "</span><span>99 → " + blank(14) + "</span></div>",
        "올림하여 천의 자리까지 나타내면 5000이 되는 수에 모두 ○ 하세요." + pick(["4001", "4999", "5001", "3999", "5000"]),
    ]),
]))

# ---------- 사회 ----------
L5 = lesson(5, "사회", "통일 신라 말의 혼란과 고려의 건국", "왜 새 나라가 생겼을까요", "사회 1번", "".join([
    story("왕 자리를 둘러싼 싸움", pic=picture(5, "진골 귀족들이 왕 자리를 두고 다투는 사이, 지방에서는 호족이 힘을 키웠어요."), scenes=[
        "삼국을 통일한 신라는 처음에는 평화로웠어요. 그런데 시간이 지나자 서울(경주)의 진골 귀족들이 "
        "<b>서로 왕이 되겠다고 싸우기</b> 시작했어요. 왕이 바뀌고 또 바뀌어서, 약 150년 동안 왕이 20명이나 바뀌었어요.",
        "귀족들이 싸움에 정신이 팔린 사이 나라 살림은 엉망이 되었어요. 세금을 더 걷으려 하자 "
        "농민들은 살기 힘들어 곳곳에서 들고일어났어요. <b>나라가 몹시 혼란해졌어요.</b>",
        "그러자 지방에서 성을 쌓고 군사를 거느린 세력이 나타났어요. 이들은 스스로 '성주', '장군'이라 부르며 "
        "자기 지역을 다스렸어요. 이들을 <b>호족</b>이라고 해요.",
        "호족 가운데 견훤은 <b>후백제</b>를, 궁예는 <b>후고구려</b>를 세웠어요. 신라까지 세 나라가 다시 생겼으니 "
        "이때를 <b>후삼국 시대</b>라고 해요. 궁예의 신하였던 <b>왕건</b>이 918년에 <b>고려</b>를 세우고, 936년에 후삼국을 통일했어요.",
    ]),
    timeline([("신라 말", "귀족 다툼, 호족 성장"), ("900년쯤", "후백제·후고구려"), ("918년", "왕건, 고려 건국"),
              ("936년", "후삼국 통일")]),
    rule("통일 신라 말 = <b>지배층의 권력 다툼</b>으로 나라가 혼란 + 지방에서 <b>호족</b>이 성장"),
    careful("'왕권이 강했다', '모두 잘 살았다', '모두 평등했다'는 통일 신라 말과 반대예요."),
    practice("이야기를 떠올리며 풀어요", [
        "통일 신라 말에 지방에서 성을 쌓고 군사를 거느린 세력을 무엇이라고 하나요? " + PAREN,
        "맞으면 ○, 틀리면 × 하세요. <span class='ox'>통일 신라 말에는 왕권이 강해 나라가 안정되었다. ( &emsp; )</span>",
        "고려를 세운 사람은 누구인가요? " + PAREN,
        "통일 신라 말에 나라가 혼란해진 까닭을 한 문장으로 써 보세요." + LINE,
    ]),
]))

L6 = lesson(6, "사회", "왕건의 뒤를 이은 왕들", "왕의 힘을 키워요", "사회 5번", "".join([
    story("힘센 호족을 어떻게 할까?", pic=picture(6, "광종은 시험(과거제)으로 관리를 뽑고, 억울한 노비를 풀어 주었어요."), scenes=[
        "왕건은 나라를 세울 때 호족들의 도움을 많이 받았어요. 그래서 호족의 딸들과 결혼하고 벼슬도 주었어요. "
        "그런데 왕건이 죽고 나니 <b>호족의 힘이 너무 세서</b> 왕이 마음대로 나라를 다스리기 어려웠어요.",
        "넷째 왕 <b>광종</b>은 생각했어요. \"억울하게 노비가 된 사람을 풀어 주자!\" 호족들은 전쟁 포로나 빚진 사람을 "
        "노비로 많이 거느렸는데, 이들을 풀어 주니 백성은 기뻐하고 호족의 힘은 약해졌어요(<b>노비안검법</b>).",
        "광종은 또 \"집안이 아니라 <b>실력</b>으로 관리를 뽑자!\"며 시험을 보게 했어요. 이것이 <b>과거제</b>예요. "
        "공부를 잘한 사람이 관리가 되니 왕에게 충성하는 신하가 늘었어요.",
        "여섯째 왕 <b>성종</b>은 \"지방도 왕이 직접 다스리자!\"며 <b>주요 지방에 관청을 두고 관리를 보냈어요</b>. "
        "이제 호족 마음대로 하던 지방까지 나라의 손길이 닿게 되었어요.",
    ]),
    '<table class="tbl blk"><tr><th>왕</th><th>한 일</th><th>결과</th></tr>'
    '<tr><td>광종</td><td>억울한 노비를 풀어 줌, 과거제 실시</td><td>호족 힘 약해지고 왕권 강해짐</td></tr>'
    '<tr><td>성종</td><td>주요 지방에 관청을 두고 관리를 보냄</td><td>지방까지 나라가 다스림</td></tr></table>',
    careful("<b>신분에 따라 오를 수 있는 관직을 정해 둔 것</b>은 신라의 <b>골품제</b>예요. 고려 왕들의 정책이 아니에요. "
            "고려는 오히려 시험(과거제)으로 관리를 뽑았어요."),
    practice("이야기를 떠올리며 풀어요", [
        "시험을 보아 실력으로 관리를 뽑는 제도는 무엇인가요? " + PAREN,
        "억울하게 노비가 된 사람을 풀어 준 왕은 누구인가요? " + PAREN,
        "맞으면 ○, 틀리면 × 하세요. <span class='ox'>고려의 왕들은 신분에 따라 오를 수 있는 관직을 정해 두었다. ( &emsp; )</span>",
        "광종이 과거제를 실시한 까닭을 '호족'이라는 낱말을 넣어 써 보세요." + LINE,
    ]),
]))

L7 = lesson(7, "사회", "거란의 침입을 물리친 고려", "말로 막고, 싸워서 이기다", "사회 9번, 11번", "".join([
    story("북쪽에서 온 거란", pic=picture(7, "강감찬이 귀주에서 거란군을 크게 물리쳤어요(귀주 대첩)."), scenes=[
        "고려 북쪽에는 <b>거란</b>이라는 나라가 있었어요. 거란은 926년에 <b>발해를 멸망시켰어요</b>. "
        "발해는 고구려를 이은 나라였고, 고려도 고구려를 이었다고 생각했어요. 그래서 고려는 형제 같은 나라를 무너뜨린 "
        "<b>거란을 적으로 여겼어요</b>. 왕건은 거란이 보낸 낙타를 다리 밑에 매어 굶겨 버리기도 했대요.",
        "<b>1차 침입(993년)</b>: 거란 장수 소손녕이 80만 대군이라며 쳐들어왔어요. 이때 <b>서희</b>가 적진으로 직접 찾아가 "
        "\"고려는 고구려를 이은 나라다. 여진이 길을 막아 거란과 사귀지 못했을 뿐이다\"라고 말했어요. "
        "서희는 싸우지 않고 말로 거란군을 돌려보내고, 오히려 <b>강동 6주</b> 땅까지 얻었어요(<b>외교 담판</b>).",
        "<b>2차 침입(1010년)</b>: 거란이 다시 쳐들어와 수도 개경까지 불탔어요. 하지만 고려군이 돌아가는 거란군을 끈질기게 공격했어요.",
        "<b>3차 침입(1018년)</b>: 거란이 10만 대군으로 또 쳐들어오자 <b>강감찬</b>이 고려군을 이끌었어요. "
        "강감찬은 <b>귀주</b>에서 거란군을 크게 물리쳤어요. 살아 돌아간 거란군이 몇천 명뿐이었대요. 이 싸움이 <b>귀주 대첩</b>이에요.",
    ]),
    '<table class="tbl blk"><tr><th>침입</th><th>누가</th><th>어떻게</th></tr>'
    '<tr><td>1차</td><td>서희</td><td>외교 담판으로 거란군을 돌려보내고 강동 6주를 얻음</td></tr>'
    '<tr><td>3차</td><td>강감찬</td><td>귀주에서 거란군을 크게 물리침(귀주 대첩)</td></tr></table>',
    careful("'어떻게 대응했는지 쓰시오'에는 <b>누가</b>(강감찬), <b>어디서</b>(귀주), <b>어떻게</b>(크게 물리침)가 모두 들어가야 해요."),
    practice("이야기를 떠올리며 풀어요", [
        "고려가 거란을 적으로 여긴 까닭은 거란이 어떤 나라를 멸망시켰기 때문인가요? " + PAREN,
        "거란의 1차 침입 때 말로 거란군을 돌려보낸 사람과, 그때 얻은 땅을 쓰세요."
        "<div class='wans'>사람 ( " + blank(22) + " )&emsp;땅 ( " + blank(22) + " )</div>",
        "거란의 3차 침입에 누가 중심이 되어 어떻게 대응했는지 쓰세요." + LINE + LINE,
    ]),
]))

L8 = lesson(8, "사회", "금속 활자와 『직지』", "남아 있는 가장 오래된 책", "사회 19번", "".join([
    story("글자를 하나하나 만들다", pic=picture(8, "글자를 하나씩 금속으로 만들어 모아 찍는 금속 활자 인쇄"), scenes=[
        "옛날에는 책을 찍으려면 나무판에 한 쪽을 통째로 새겼어요(<b>목판 인쇄</b>). 『팔만대장경』이 바로 목판이에요. "
        "그런데 다른 책을 찍으려면 판을 처음부터 다시 새겨야 했어요.",
        "고려 사람들은 꾀를 냈어요. \"글자를 <b>하나씩 따로</b> 만들어 두고 필요할 때 모아 찍자!\" "
        "쇠붙이를 녹여 글자를 만든 것이 <b>금속 활자</b>예요. 글자를 바꿔 끼우면 여러 가지 책을 찍을 수 있었어요.",
        "고려는 1234년쯤 금속 활자로 『상정고금예문』을 찍었다는 기록이 있어요. <b>가장 먼저 만든 금속 활자 책</b>이지만, "
        "안타깝게도 <b>지금 남아 있지 않아요</b>.",
        "1377년 청주 흥덕사에서 찍은 『<b>직지</b>』는 지금도 남아 있어요. <b>오늘날 남아 있는 세계에서 가장 오래된 금속 활자 인쇄본</b>이에요. "
        "조선 말에 프랑스로 건너가 지금은 <b>프랑스 국립 도서관</b>에 있고, 유네스코 세계 기록 유산이에요.",
    ]),
    '<table class="tbl blk"><tr><th></th><th>『상정고금예문』</th><th>『직지』</th></tr>'
    '<tr><td>만든 때</td><td>1234년쯤</td><td>1377년</td></tr>'
    '<tr><td>지금 남아 있나요?</td><td>없어요</td><td>있어요 (프랑스)</td></tr>'
    '<tr><td>특징</td><td>가장 먼저 만든 금속 활자 책(기록)</td><td>남아 있는 가장 오래된 금속 활자 책</td></tr></table>',
    careful("『직지』는 '세계 <b>최초</b>'가 아니라 '남아 있는 것 중 <b>가장 오래된</b>' 금속 활자 인쇄본이에요. 그리고 지금 우리나라가 아닌 <b>프랑스</b>에 있어요."),
    practice("이야기를 떠올리며 풀어요", [
        "글자를 하나씩 쇠로 만들어 모아 찍는 인쇄 방법은 무엇인가요? " + PAREN,
        "맞으면 ○, 틀리면 × 하세요.<div class='ox2'>『직지』는 현재 우리나라에 있다. ( &emsp; )<br>"
        "『직지』는 세계 최초로 만들어진 목판 인쇄본이다. ( &emsp; )<br>"
        "『직지』는 오늘날 남아 있는 세계에서 가장 오래된 금속 활자 인쇄본이다. ( &emsp; )</div>",
        "목판 인쇄보다 금속 활자가 좋은 점을 한 가지 쓰세요." + LINE,
    ]),
]))

# ---------- 정답 ----------
ANS = [
    ("1차시 이상과 이하", ["1. 15, 20, 16.5", "2. 30, 29.5, 18", "3. 24 이상", "4. 7 이하", "5. 40, 41, 42, 43, 44, 45"]),
    ("2차시 초과와 미만", ["1. 19.1, 23, 21", "2. 12 이상 16 미만", "3. 31 초과 35 이하", "4. 9, 10, 11"]),
    ("3차시 버스 문제로 범위 구하기", [f"1. 90명 초과 120명 이하 (30{X}3=90, 30{X}4=120)",
                                f"2. 91명 이상 135명 이하 (45{X}2=90 초과 → 91 이상, 45{X}3=135)",
                                f"3. 51개 이상 60개 이하 (10{X}5=50 초과 → 51 이상, 10{X}6=60)"]),
    ("4차시 올림", ["1. 5000, 5000, 7000, 8000", "2. 400, 600, 1300, 100", "3. 4001, 4999, 5000"]),
    ("5차시 통일 신라 말의 혼란과 고려의 건국", ["1. 호족", "2. ×", "3. 왕건",
                                     "4. 예) 귀족들이 서로 왕이 되려고 다투어서 나라가 혼란해졌습니다."]),
    ("6차시 왕건의 뒤를 이은 왕들", ["1. 과거제", "2. 광종", "3. × (신라의 골품제예요)",
                             "4. 예) 집안이 좋은 호족 대신 실력 있는 사람을 관리로 뽑아 호족의 힘을 줄이고 왕권을 강하게 하려고"]),
    ("7차시 거란의 침입을 물리친 고려", ["1. 발해", "2. 서희, 강동 6주",
                                "3. 예) 강감찬이 중심이 되어 귀주에서 거란군을 크게 물리쳤습니다(귀주 대첩)."]),
    ("8차시 금속 활자와 『직지』", ["1. 금속 활자 (인쇄)", "2. ×, ×, ○",
                             "3. 예) 글자를 바꿔 끼워 여러 가지 책을 찍을 수 있다. / 나무보다 단단해 오래 쓸 수 있다."]),
]


CSS = """
@page { size: A4; margin: 12mm 14mm 14mm; }
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif; color: #000; font-size: 11pt; word-break: keep-all; }
.op { font-family: 'DejaVu Sans', sans-serif; font-size: 0.95em; margin: 0 0.2em; }
.blk { break-inside: avoid; }
.cover .t1 { font-size: 12pt; color: #1d6b4f; font-weight: bold; }
.cover .t2 { font-size: 24pt; font-weight: bold; margin: 2mm 0 1mm; }
.cover .t3 { font-size: 11.5pt; color: #444; border-bottom: 2.5px solid #1d6b4f; padding-bottom: 4mm; margin-bottom: 6mm; display: flex; justify-content: space-between; }
.cover .t3 span.f { display: inline-block; border-bottom: 1px solid #000; width: 26mm; margin-left: 2mm; }
.how { border: 1px solid #1d6b4f; padding: 4mm 5mm; margin-bottom: 6mm; line-height: 1.9; }
.how b { color: #1d6b4f; }
table.toc { width: 100%; border-collapse: collapse; }
table.toc td { padding: 2.4mm 2mm; border-bottom: 1px dotted #bbb; }
table.toc td.n { width: 16mm; color: #1d6b4f; font-weight: bold; }
table.toc td.s { width: 14mm; color: #555; font-size: 10pt; }
table.toc td.l { width: 34mm; color: #777; font-size: 9.5pt; text-align: right; }
.lesson { break-before: page; }
.lh { display: flex; align-items: center; gap: 4mm; border-bottom: 2.5px solid #1d6b4f; padding-bottom: 2.5mm; margin-bottom: 3.5mm; }
.ln { background: #1d6b4f; color: #fff; font-weight: bold; font-size: 12pt; padding: 1.5mm 3mm; white-space: nowrap; }
.lt { font-size: 16pt; font-weight: bold; }
.ls { font-size: 10pt; color: #555; }
.linked { margin-left: auto; font-size: 9pt; color: #1d6b4f; border: 1px solid #1d6b4f; padding: 0.5mm 2.5mm; white-space: nowrap; }
.concept { border: 1.5px solid #3f78b5; padding: 3mm 4mm; margin-bottom: 3mm; }
.ct { font-weight: bold; color: #24548a; margin-bottom: 1.5mm; font-size: 12pt; }
.side { line-height: 1.85; margin: 1mm 0; }
.stages { display: flex; align-items: center; justify-content: center; gap: 3mm; margin: 2mm 0; flex-wrap: wrap; }
.stage { text-align: center; }
.stage svg text { font-family: 'Noto Sans CJK KR', sans-serif; }
.cap { font-size: 9.5pt; color: #333; line-height: 1.5; }
.arr { color: #1d6b4f; font-size: 14pt; }
.rule { background: #d6ebe0; padding: 2.5mm 4mm; margin-bottom: 3mm; line-height: 1.9; }
.rt { display: inline-block; background: #1d6b4f; color: #fff; font-size: 9.5pt; font-weight: bold; padding: 0 2mm; margin-right: 3mm; }
.careful { background: #fff7e0; padding: 2mm 4mm; margin-bottom: 3mm; line-height: 1.85; }
.careful b:first-child { color: #9a6b00; }
.pic { float: right; width: 62mm; margin: 0.5mm 0 1.5mm 4mm; }
.pic img { width: 100%; display: block; border: 1px solid #ccc; border-radius: 1.5mm; }
.pic figcaption { font-size: 8.5pt; line-height: 1.4; color: #555; margin-top: 0.8mm; }
.story { border: 1.5px solid #8a5a2b; padding: 3mm 4mm; margin-bottom: 3mm; }
.st { font-weight: bold; color: #8a5a2b; font-size: 12pt; margin-bottom: 1.5mm; }
.scene { display: grid; grid-template-columns: 15mm 1fr; gap: 2mm; line-height: 1.8; margin-bottom: 1.2mm; font-size: 10.8pt; }
.sn { color: #8a5a2b; font-weight: bold; font-size: 9.5pt; padding-top: 0.6mm; }
.tl { display: flex; border-top: 2px solid #8a5a2b; margin: 1mm 0 3.5mm; }
.tp { flex: 1; padding: 1.5mm 1mm 0; text-align: center; position: relative; }
.tp::before { content: ""; position: absolute; top: -2.2mm; left: 50%; width: 3mm; height: 3mm; margin-left: -1.5mm; background: #8a5a2b; border-radius: 50%; }
.ty { font-weight: bold; font-size: 10pt; }
.te { font-size: 9.5pt; color: #333; }
.tbl { width: 100%; border-collapse: collapse; margin: 1.5mm 0 3mm; font-size: 10.5pt; }
.tbl th, .tbl td { border: 1px solid #999; padding: 1.2mm 2.5mm; text-align: center; }
.tbl th { background: #eef3f0; }
.pt { font-weight: bold; color: #1d6b4f; font-size: 12pt; margin: 2.5mm 0 1.5mm; border-top: 1px solid #1d6b4f; padding-top: 2mm; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; column-gap: 6mm; }
.grid2 > .dr { line-height: 2.1; margin-bottom: 1.5mm; break-inside: avoid; }
.grid2 .picks { gap: 6mm; margin-left: 4mm; }
.grid2 .fig { margin-left: 0; }
.grid1 > .dr { line-height: 2.1; margin-bottom: 1.5mm; break-inside: avoid; }
.qn { color: #1d6b4f; font-weight: bold; margin-right: 2mm; }
.picks { display: flex; gap: 10mm; margin: 0.5mm 0 0 7mm; font-size: 12pt; }
.fig { margin: 1mm 0 0 7mm; }
.wans { text-align: right; }
.u { display: inline-block; border-bottom: 1px solid #000; height: 1.3em; vertical-align: bottom; }
.paren { float: right; }
.wline { border-bottom: 1px solid #000; height: 9mm; margin-left: 7mm; }
.row4 { display: flex; justify-content: space-between; margin-left: 7mm; }
.ox2 { margin-left: 7mm; line-height: 2.1; }
.answers { break-before: page; }
.answers h2 { font-size: 16pt; border-bottom: 2.5px solid #1d6b4f; padding-bottom: 2.5mm; margin: 0 0 4mm; }
.answers .cols { columns: 2; column-gap: 8mm; }
.ag { break-inside: avoid; margin-bottom: 4mm; }
.ag .h { font-weight: bold; color: #1d6b4f; margin-bottom: 1mm; }
.ag .items { line-height: 1.9; font-size: 10.5pt; padding-left: 4mm; }
"""

LESSONS = [L1, L2, L3, L4, L5, L6, L7, L8]
TOC = [
    (1, "수학", "이상과 이하", "수학 2번"), (2, "수학", "초과와 미만", "수학 8번"),
    (3, "수학", "버스 문제로 범위 구하기", "수학 2번, 9번"), (4, "수학", "올림", "수학 13번"),
    (5, "사회", "통일 신라 말의 혼란과 고려의 건국", "사회 1번"), (6, "사회", "왕건의 뒤를 이은 왕들", "사회 5번"),
    (7, "사회", "거란의 침입을 물리친 고려", "사회 9번, 11번"), (8, "사회", "금속 활자와 『직지』", "사회 19번"),
]


def main():
    toc = "".join(f'<tr><td class="n">{n}차시</td><td class="s">{s}</td><td>{t}</td><td class="l">오답노트 {l}</td></tr>'
                  for n, s, t, l in TOC)
    cover = (
        '<section class="cover"><div class="t1">2026년 10월 27일 시험 오답노트와 함께 보는</div>'
        '<div class="t2">개념부터 차근차근</div>'
        '<div class="t3"><span>수학 · 수의 범위와 어림하기&emsp;사회 · 고려의 성립과 발전</span>'
        '<span>이름<span class="f"></span></span></div>'
        '<div class="how"><b>이렇게 공부해요</b><br>'
        '① 수학은 <b>그림</b>을 먼저 보고, 사회는 <b>이야기</b>를 먼저 소리 내어 읽어요.<br>'
        '② <b>기억해요</b>를 보지 않고 말해 본 뒤, 맞았는지 확인해요.<br>'
        '③ <b>조심!</b>은 오답노트에서 틀린 바로 그 부분이에요.<br>'
        '④ 문제를 다 풀면 마지막 쪽에서 채점하고, 오답노트 문제를 다시 풀어 봐요.</div>'
        f'<table class="toc">{toc}</table></section>'
    )
    ans = "".join(
        f'<div class="ag"><div class="h">{h}</div><div class="items">{"<br>".join(items)}</div></div>' for h, items in ANS)
    answers = f'<section class="answers"><h2>정답</h2><div class="cols">{ans}</div></section>'
    html = (
        '<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        f'<title>개념부터 차근차근</title><style>{CSS}</style></head><body>'
        f'{cover}{"".join(LESSONS)}{answers}</body></html>'
    )
    with open("concept.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()

"""오답 문제지 정답·풀이(A4) HTML 생성기.

python3 build_answers.py  ->  answers.html  (Chromium으로 answers.pdf 출력)
"""

from build_worksheet import BOX, fr, mx

X = '<span class="op">×</span>'
LT = '<span class="op">&lt;</span>'
GT = '<span class="op">&gt;</span>'

# (번호, 정답, [풀이 단계], 주의/포인트)
A = []

A.append(("01", "72쪽", [
    f"오늘 읽은 쪽수는 어제 읽은 28쪽의 {mx(1, 4, 7)}이에요. '~의'는 곱하기로 바꿔요. → 28 {X} {mx(1, 4, 7)}",
    f"대분수를 가분수로 바꿔요. {mx(1, 4, 7)} = {fr(11, 7)} (7 {X} 1 + 4 = 11)",
    f"28 {X} {fr(11, 7)} 에서 28과 7을 7로 약분하면 4 {X} 11 = <b>44쪽</b> (오늘 읽은 쪽수)",
    "어제와 오늘 읽은 쪽수를 더해요. 28 + 44 = <b>72쪽</b>",
], "오늘 읽은 44쪽만 답으로 쓰면 안 돼요. 문제는 '어제와 오늘 모두'를 물었어요."))

A.append(("03", f"{fr(10, 81)} kg", [
    f"세 사람이 먹은 양은 케이크 {fr(4, 9)} kg의 {fr(5, 6)}이에요. → {fr(4, 9)} {X} {fr(5, 6)}",
    f"4와 6을 2로 약분하면 {fr(2, 9)} {X} {fr(5, 3)} = {fr(10, 27)} kg (세 사람이 먹은 양 전체)",
    f"세 사람이 <b>똑같이</b> 나누어 먹었으니 수민이는 그중 {fr(1, 3)}을 먹었어요.",
    f"{fr(10, 27)} {X} {fr(1, 3)} = <b>{fr(10, 81)} kg</b>",
], f"{fr(10, 27)} kg은 세 사람이 먹은 양을 모두 더한 거예요. 한 사람 몫을 구하려면 한 번 더 {fr(1, 3)}을 곱해야 해요."))

A.append(("05", "익준", [
    "먼저 큰 단위를 작은 단위로 바꾼 다음 분수를 곱해요.",
    f"송화: 1m = 100cm → 100 {X} {fr(1, 5)} = 20cm. 50cm가 아니므로 <b>틀림</b>",
    f"익준: 1kg = 1000g → 1000 {X} {fr(1, 4)} = 250g. <b>맞음</b>",
    f"정원: 1시간 = 60분 → 60 {X} {fr(1, 2)} = 30분. 40분이 아니므로 <b>틀림</b>",
], "1시간은 100분이 아니라 60분이에요. 시간 문제에서 가장 많이 틀리는 부분이에요."))

A.append(("06", "①", [
    f"① 모모: 1m = 100cm → 100 {X} {fr(1, 5)} = 20cm. <b>맞음</b>",
    f"② 지효: 1km = 1000m → 1000 {X} {fr(1, 2)} = 500m. 200m가 아니므로 <b>틀림</b>",
    f"③ 연희: 1L = 1000mL → 1000 {X} {fr(3, 10)} = 300mL. 500mL가 아니므로 <b>틀림</b>",
], "1km = 1000m, 1L = 1000mL를 꼭 기억해요."))

A.append(("08", f"{mx(69, 1, 3)} km", [
    f"2시간 10분을 '시간'으로 바꿔요. 1시간 = 60분이니까 10분 = {fr(10, 60)}시간 = {fr(1, 6)}시간 → 2시간 10분 = {mx(2, 1, 6)}시간",
    f"하루에 걷는 거리: {mx(2, 2, 7)} {X} {mx(2, 1, 6)} = {fr(16, 7)} {X} {fr(13, 6)}",
    f"16과 6을 2로 약분하면 {fr(8, 7)} {X} {fr(13, 3)} = {fr(104, 21)} km",
    f"2주일 = 14일이에요. {fr(104, 21)} {X} 14 에서 21과 14를 7로 약분하면 {fr(104, 3)} {X} 2 = {fr(208, 3)}",
    f"{fr(208, 3)} = <b>{mx(69, 1, 3)} km</b> (208 ÷ 3 = 69 나머지 1)",
], f"10분을 {fr(10, 100)}시간으로 바꾸면 틀려요. 1시간은 60분이므로 10분은 {fr(10, 60)}시간이에요. 2주일도 2일이 아니라 14일!"))

A.append(("09", f"{fr(7, 9)} m", [
    f"ㄱ부터 ㅁ까지 전체 길이가 {mx(4, 2, 3)} m이고, 똑같이 6칸으로 나뉘어 있어요.",
    f"선분 ㄱㄴ은 6칸 중 1칸이에요. → 전체의 {fr(1, 6)}",
    f"{mx(4, 2, 3)} {X} {fr(1, 6)} = {fr(14, 3)} {X} {fr(1, 6)} = {fr(14, 18)}",
    f"2로 약분하면 <b>{fr(7, 9)} m</b>",
], "ㄷ, ㄹ 같은 다른 점에 헷갈리지 말고, 구하는 선분이 몇 칸인지 먼저 세어요."))

A.append(("10", "27 cm", [
    f"색 테이프 30cm를 10칸으로 나누었고, 그중 9칸에 색칠했어요. → 전체의 {fr(9, 10)}",
    f"30 {X} {fr(9, 10)} 에서 30과 10을 10으로 약분하면 3 {X} 9 = <b>27cm</b>",
], "한 칸은 30 ÷ 10 = 3cm예요. 3cm짜리가 9칸이니까 27cm라고 생각해도 돼요."))

A.append(("11", f"{fr(1, 10)} ({fr(3, 30)})", [
    f"0부터 {fr(4, 15)}까지를 똑같이 8칸으로 나누었어요.",
    f"한 칸의 크기: {fr(4, 15)} {X} {fr(1, 8)} = {fr(4, 120)} = {fr(1, 30)}",
    f"화살표는 0에서 3칸 간 곳이에요. {fr(1, 30)} {X} 3 = {fr(3, 30)} = <b>{fr(1, 10)}</b>",
], f"{fr(4, 15)} {X} {fr(3, 8)}처럼 한 번에 계산해도 같은 답이 나와요."))

A.append(("12", f"{fr(1, 6)} ({fr(3, 18)})", [
    f"0부터 {fr(7, 18)}까지를 똑같이 7칸으로 나누었어요.",
    f"한 칸의 크기: {fr(7, 18)} {X} {fr(1, 7)} = {fr(1, 18)}",
    f"화살표는 0에서 3칸 간 곳이에요. {fr(1, 18)} {X} 3 = {fr(3, 18)} = <b>{fr(1, 6)}</b>",
], "눈금 수가 아니라 칸 수를 세어야 해요. 0은 칸을 세기 시작하는 곳이에요."))

A.append(("13", "10 km", [
    f"전철로 간 거리: 40 {X} {fr(3, 8)} = 15km",
    "전철을 타고 남은 거리: 40 − 15 = 25km",
    f"버스로 간 거리는 <b>나머지 25km</b>의 {fr(3, 5)}이에요. 25 {X} {fr(3, 5)} = 15km",
    "걸어간 거리: 25 − 15 = <b>10km</b>",
], f"버스는 '40km의 {fr(3, 5)}'이 아니라 '나머지의 {fr(3, 5)}'이에요. 무엇의 분수인지 꼭 확인해요."))

A.append(("14", "18 cm", [
    f"미술 시간에 쓴 철사: 90 {X} {fr(2, 5)} = 36cm",
    "남은 철사: 90 − 36 = 54cm",
    f"서진이에게 준 철사는 <b>나머지 54cm</b>의 {fr(2, 3)}이에요. 54 {X} {fr(2, 3)} = 36cm",
    "남은 철사의 길이: 54 − 36 = <b>18cm</b>",
], "13번과 같은 유형이에요. '나머지의 ~'가 나오면 먼저 나머지를 구해요."))

A.append(("15", f"{mx(4, 1, 5)}", [
    f"잘못한 계산을 식으로 써요. (어떤 수 − {fr(5, 9)}) + 9 = {mx(9, 7, 15)}",
    f"거꾸로 생각하면 (어떤 수 − {fr(5, 9)}) = {mx(9, 7, 15)} − 9 = {fr(7, 15)}",
    f"바른 계산은 (어떤 수 − {fr(5, 9)}) {X} 9 예요. 괄호 안이 {fr(7, 15)}이니까 {fr(7, 15)} {X} 9",
    f"15와 9를 3으로 약분하면 {fr(7, 5)} {X} 3 = {fr(21, 5)} = <b>{mx(4, 1, 5)}</b>",
], f"어떤 수를 꼭 구하지 않아도 돼요. '어떤 수 − {fr(5, 9)}'의 값만 알면 바로 9를 곱할 수 있어요."))

A.append(("16", f"② {fr(4, 11)}", [
    f"잘못한 계산을 식으로 써요. 어떤 수 − {fr(2, 5)} = {fr(28, 55)}",
    f"거꾸로 더해서 어떤 수를 구해요. 어떤 수 = {fr(28, 55)} + {fr(2, 5)} = {fr(28, 55)} + {fr(22, 55)} = {fr(50, 55)} = {fr(10, 11)}",
    f"바른 계산: {fr(10, 11)} {X} {fr(2, 5)} 에서 10과 5를 5로 약분하면 {fr(2, 11)} {X} 2 = <b>{fr(4, 11)}</b>",
    "보기에서 찾으면 <b>②</b>",
], f"{fr(2, 5)}를 {fr(22, 55)}로 통분할 때 분모와 분자에 똑같이 11을 곱해요. 어떤 수({fr(10, 11)})를 답으로 고르지 않게 조심해요."))

A.append(("17", "60개", [
    f"하루 동안 처음 빵의 {fr(3, 4)}을 팔았으니 남은 빵은 처음의 1 − {fr(3, 4)} = {fr(1, 4)}이에요.",
    f"처음 빵의 {fr(1, 4)}이 15개예요.",
    "4칸 중 1칸이 15개이니까 4칸은 15 × 4 = <b>60개</b>",
    f"확인: 60 {X} {fr(3, 4)} = 45개 팔고, 60 − 45 = 15개 남아요. ✓",
], f"15개는 판 빵이 아니라 남은 빵이에요. 남은 빵이 처음의 몇 분의 몇인지 먼저 구해요."))

A.append(("18", "48명", [
    "색종이는 모두 12 × 5 = 60장이에요.",
    f"남은 색종이: 60 {X} {fr(1, 5)} = 12장",
    "학생들이 나누어 가진 색종이: 60 − 12 = 48장",
    "한 명이 한 장씩 가졌으니 학생 수는 <b>48명</b>",
], f"남은 12장을 답으로 쓰지 않게 조심해요. 다른 방법: 나누어 가진 것은 전체의 {fr(4, 5)} → 60 {X} {fr(4, 5)} = 48"))

A.append(("19", "4개", [
    f"오른쪽을 먼저 계산해요. {mx(2, 5, 9)} {X} {mx(1, 4, 5)} = {fr(23, 9)} {X} {fr(9, 5)}",
    f"9끼리 약분하면 {fr(23, 5)} = {mx(4, 3, 5)} → 식은 <span class=\"mx\">{BOX}{fr(2, 5)}</span>{LT}{mx(4, 3, 5)}",
    f"□ = 4일 때: {mx(4, 2, 5)}와 {mx(4, 3, 5)}는 자연수가 같으니 분수끼리 비교해요. {fr(2, 5)} {LT} {fr(3, 5)} 이므로 <b>된다</b>",
    f"□ = 5일 때: {mx(5, 2, 5)}는 {mx(4, 3, 5)}보다 커서 <b>안 된다</b>",
    "□에 들어갈 수 있는 자연수는 1, 2, 3, 4 → <b>4개</b>",
], "□ = 4일 때를 빠뜨리기 쉬워요. 자연수 부분이 같으면 분수 부분까지 비교해요."))


CSS = """
@page { size: A4; margin: 13mm 13mm 15mm; }
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Noto Sans CJK KR', 'Noto Sans KR', 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif; color: #000; }
header { border-bottom: 2.5px solid #1d6b4f; padding-bottom: 3mm; margin-bottom: 5mm; }
header .t1 { font-size: 11pt; color: #1d6b4f; font-weight: bold; }
header .t2 { font-size: 18pt; font-weight: bold; margin-top: 1mm; }
.fr { display: inline-flex; flex-direction: column; align-items: center; vertical-align: middle; font-size: 1em; line-height: 1.05; margin: 0 0.15em; }
.fr > span:first-child { border-bottom: 1.2px solid #000; padding: 0 0.15em; }
.fr > span:last-child { padding: 0 0.15em; }
.mx { white-space: nowrap; }
.mx > .fr { margin-left: 0.02em; }
.op { font-family: 'DejaVu Sans', sans-serif; font-size: 0.95em; margin: 0 0.25em; }
.box { display: inline-block; width: 1.1em; height: 1.25em; border: 1.4px solid #000; vertical-align: middle; }
.quick { border: 1.5px solid #1d6b4f; border-radius: 2mm; padding: 3mm 4mm; margin-bottom: 6mm; break-inside: avoid; }
.quick h2 { font-size: 12pt; color: #1d6b4f; margin: 0 0 2mm; }
.quick table { width: 100%; border-collapse: collapse; font-size: 11pt; }
.quick td { padding: 0.8mm 2mm; border-bottom: 1px dotted #bbb; vertical-align: middle; }
.quick td.n { color: #1d6b4f; font-weight: bold; width: 9mm; }
.sol { display: inline-block; width: 100%; vertical-align: top; border-top: 1px dashed #bbb; padding: 3.5mm 0 2.5mm; }
.head { display: flex; align-items: center; gap: 3mm; margin-bottom: 2mm; }
.num { font-size: 17pt; font-weight: bold; color: #1d6b4f; line-height: 1; min-width: 9mm; }
.ans { font-size: 12pt; font-weight: bold; background: #e6f2ec; border: 1.2px solid #1d6b4f; border-radius: 1.5mm; padding: 0.5mm 3mm; }
ol { margin: 0 0 0 11.5mm; padding-left: 5mm; font-size: 11.5pt; line-height: 1.9; }
ol li { padding-left: 1mm; }
.tip { margin: 2mm 0 0 11.5mm; font-size: 10.5pt; line-height: 1.8; background: #fff7e0; border-left: 3px solid #e0a800; padding: 1mm 3mm; }
.tip b.k { color: #9a6b00; }
"""


def main():
    quick_rows = []
    for i in range(0, len(A), 2):
        cells = ""
        for num, ans, _, _ in A[i:i + 2]:
            cells += f'<td class="n">{num}</td><td>{ans}</td>'
        quick_rows.append(f"<tr>{cells}</tr>")
    sols = []
    for num, ans, steps, tip in A:
        lis = "".join(f"<li>{s}</li>" for s in steps)
        sols.append(
            f'<div class="sol"><div class="head"><span class="num">{num}</span>'
            f'<span class="ans">정답 {ans}</span></div><ol>{lis}</ol>'
            f'<div class="tip"><b class="k">이것만은 조심!</b> {tip}</div></div>'
        )
    html = (
        '<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        f'<title>분수의 곱셈 오답 정답지</title><style>{CSS}</style></head><body>'
        '<header><div class="t1">5학년 2학기 · 2. 분수의 곱셈</div><div class="t2">오답 다시 풀기 — 정답과 풀이</div></header>'
        f'<div class="quick"><h2>빠른 정답</h2><table>{"".join(quick_rows)}</table></div>'
        + "".join(sols)
        + "</body></html>"
    )
    with open("answers.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()

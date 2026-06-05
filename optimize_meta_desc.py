"""
WooaColor KO 페이지 메타 디스크립션 CTR 최적화
- 최우선: "온라인 색상 추출" 89 + "색상추출" 22 + "색상 추출" 28 = 139 노출 → color-picker.html
- 핵심: 색상 비율(11) → color-mixer / cmyk rgb 변환(4) → color-converter-full / 웹접근성 색상 대비(4) → contrast-checker
- 공통: "설치 없이 브라우저에서 무료로 사용 가능합니다" 보일러플레이트 제거
"""
import re, os

BASE = 'C:/개인/wooahouse/ColorKit'

PAGES = {
    # ── index: 색상 추출·컬러피커·변환 등 총망라 ─────────────────────────
    'index.html': (
        'HEX·RGB·HSL 변환, 색상 추출',
        '색상 추출·변환·팔레트·그라디언트·WCAG 대비 검사·CSS 그림자까지 무료! 이미지 색상 추출, HEX·RGB·HSL·CMYK 변환, 온라인 컬러피커 — 설치·로그인 없이 바로 사용. 우아컬러(WooaColor)'
    ),
    # ── 최우선: 색상 추출 139 노출 ──────────────────────────────────────
    'color-picker.html': (
        '이미지를 업로드하고 원하는 위치를 클릭해 색상을 추출',
        '이미지 색상 추출 무료 — 이미지 클릭 한 번으로 픽셀 색상을 HEX·RGB로 즉시 추출. 온라인 색상 추출·이미지 색상 피커, 설치·로그인 없이 바로 사용.'
    ),
    'image-palette.html': (
        '이미지를 업로드하면 주요 색상을 자동으로 추출',
        '이미지 색상 팔레트 추출 무료 — 사진을 업로드하면 주요 색상을 자동 추출, HEX·RGB 코드 즉시 복사. 브랜드·디자인 색상 추출에 최적, 설치·로그인 없이 바로 사용.'
    ),
    # ── 색상 비율 11 노출 ─────────────────────────────────────────────
    'color-mixer.html': (
        '두 색상을 원하는 비율로 혼합한',
        '색상 혼합기 무료 — 두 색상을 원하는 비율로 혼합, 결과 색상 HEX·RGB를 즉시 복사. 색상 비율 조절 슬라이더, 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    # ── CMYK RGB 변환 4 노출 ─────────────────────────────────────────
    'color-converter-full.html': (
        'HEX, RGB, HSL, CMYK, HSV 5가지',
        'CMYK·RGB·HEX·HSL·HSV 색상 변환기 무료 — 5가지 색상 코드를 즉시 상호 변환. 인쇄용 CMYK까지 지원, 설치·로그인 없이 바로 사용.'
    ),
    'color-converter.html': (
        'HEX, RGB, HSL 세 가지 색상 코드를 상호 변환',
        'HEX·RGB·HSL 색상 변환기 무료 — 입력 즉시 실시간 변환, CSS에서 바로 사용 가능한 코드로 즉시 복사. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    # ── 웹접근성 색상 대비 4 노출 ────────────────────────────────────
    'contrast-checker.html': (
        '전경색과 배경색의 WCAG 색상 대비율을 검사',
        '웹접근성 색상 대비 검사기 무료 — 전경색·배경색의 WCAG 대비율 즉시 측정, AA·AAA 기준 합격/불합격 표시. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    # ── CSS 그림자 키워드 ────────────────────────────────────────────
    'box-shadow.html': (
        '슬라이더로 CSS box-shadow 코드를 즉시 생성',
        'CSS 박스 그림자 생성기 무료 — 슬라이더로 box-shadow 코드를 즉시 생성. Blur·Spread·색상·투명도·inset 설정, 실시간 미리보기·코드 복사. 설치·로그인 없이 바로 사용.'
    ),
    'text-shadow.html': (
        '슬라이더로 CSS text-shadow 코드를 즉시 생성',
        'CSS 텍스트 그림자 생성기 무료 — 슬라이더로 text-shadow 코드를 즉시 생성. H-offset·V-offset·Blur·색상 설정, 실시간 미리보기·코드 복사. 설치·로그인 없이 바로 사용.'
    ),
    # ── 나머지 전체 ────────────────────────────────────────────────────
    'color-blindness.html': (
        '이미지를 업로드하면 적록색맹',
        '색맹 시뮬레이터 무료 — 이미지를 업로드하면 적록색맹·녹색맹·청황색맹·전색맹 유형별 시뮬레이션을 즉시 확인. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'color-harmony.html': (
        '기준 색상을 입력하면 보색, 유사색, 삼색',
        '색상 조화 생성기 무료 — 보색·유사색·삼색·분보색 팔레트를 자동 생성. 클릭 한 번으로 HEX 코드 복사, 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'color-name.html': (
        'HEX 또는 RGB 색상 코드를 입력하면 가장 가까운 색상 이름',
        '색상 이름 찾기 무료 — HEX·RGB 코드 입력 시 가장 가까운 색상 이름(한국어+영어)을 즉시 표시. 유사 색상 5개 함께 확인, 설치·로그인 없이 바로 사용.'
    ),
    'css-variables.html': (
        '색상 팔레트를 입력하면 CSS Custom Properties',
        'CSS 색상 변수 생성기 무료 — 색상 팔레트 입력 시 CSS Custom Properties·SCSS·Tailwind 코드를 자동 생성. 디자인 시스템 색상 토큰 제작, 설치·로그인 없이 바로 사용.'
    ),
    'gradient-gallery.html': (
        '트렌디한 CSS 그라디언트 50가지',
        'CSS 그라디언트 갤러리 무료 — 트렌디한 그라디언트 50가지 모음, 클릭 한 번으로 CSS 코드 복사. 자연·파스텔·비비드·다크 카테고리별 선택, 설치·로그인 없이 바로 사용.'
    ),
    'gradient-generator.html': (
        'CSS linear-gradient, radial-gradient 코드를 실시간으로',
        'CSS 그라디언트 생성기 무료 — linear·radial gradient 코드를 실시간 생성. 색상 정지점·방향 설정, 클릭 한 번으로 CSS 코드 복사. 설치·로그인 없이 바로 사용.'
    ),
    'opacity-converter.html': (
        'HEX 색상에 투명도를 설정해',
        '불투명도 변환기 무료 — HEX 색상에 투명도 설정 시 rgba()·8자리 HEX·hsla() 코드를 즉시 생성. 미리보기 제공, 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'palette-contrast.html': (
        '여러 색상 조합의 WCAG 접근성 대비율을 한눈에 매트릭스',
        '팔레트 대비 검사기 무료 — 여러 색상 조합의 WCAG 대비율을 매트릭스로 한눈에 확인. AA/AAA 통과 즉시 표시, 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'palette-generator.html': (
        '기준 색상에서 보색, 유사색, 트라이어드',
        '색상 팔레트 생성기 무료 — 보색·유사색·트라이어드·단색 팔레트를 자동 생성, HEX 코드 복사 지원. 설치·로그인 없이 브라우저에서 바로 사용.'
    ),
    'random-color.html': (
        '버튼 클릭 한 번으로 랜덤 색상을 생성',
        '랜덤 색상 생성기 무료 — 버튼 클릭 한 번으로 랜덤 색상을 생성, HEX·RGB·HSL 코드 즉시 복사. 최근 10개 히스토리 제공, 설치·로그인 없이 바로 사용.'
    ),
    'tints-shades.html': (
        '색상 코드를 입력하면 밝은(Tints) 10단계',
        'Tints Shades 생성기 무료 — 색상 코드 입력 시 밝은 10단계·어두운 10단계를 자동 생성. Tailwind CSS 변수로 복사 가능, 설치·로그인 없이 바로 사용.'
    ),
}

ok_count = 0
fail_count = 0

for fname, (match_prefix, new_desc) in PAGES.items():
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f'  SKIP (없음): {fname}')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<meta name="description" content=")[^"]*(")'
    def desc_replacer(m):
        if match_prefix in m.group(0):
            return m.group(1) + new_desc + m.group(2)
        return m.group(0)

    new_content = re.sub(pattern, desc_replacer, content)

    if new_content == content:
        print(f'  MISS: {fname} — "{match_prefix[:35]}"')
        fail_count += 1
        continue

    new_content = re.sub(
        r'(<meta property="og:description" content=")[^"]*(")',
        lambda x: x.group(1) + new_desc + x.group(2), new_content
    )
    new_content = re.sub(
        r'(<meta name="twitter:description" content=")[^"]*(")',
        lambda x: x.group(1) + new_desc + x.group(2), new_content
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'  OK: {fname}')
    ok_count += 1

print(f'\n완료: {ok_count}개 교체, {fail_count}개 실패')

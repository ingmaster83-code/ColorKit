# ColorKit 프로젝트 지침

## 프로젝트 개요
- **사이트명:** 컬러킷 (ColorKit)
- **URL:** https://colorkit.wooahouse.com
- **GitHub:** https://github.com/ingmaster83-code/ColorKit
- **배포:** GitHub Pages (main 브랜치 → root)

## 기술 스택
- 순수 HTML / CSS / JS (프레임워크 없음)
- 색상 처리: 브라우저 Canvas API + 순수 JS 색상 계산
- PWA: manifest.json + sw.js + js/pwa-install.js

## 서비스 목적
색상 변환·팔레트 생성·그라디언트·CSS 도구를 브라우저에서 무료로 제공.

## 도구 목록 (12개)
HEX↔RGB↔HSL변환, 색상추출(color-picker), 그라디언트생성기, 팔레트생성기, 랜덤색상,
색상대비검사(WCAG), 색상혼합기, 박스그림자, 텍스트그림자, 불투명도변환기,
**이미지팔레트추출**(color-thief), **CSS그라디언트갤러리**(50개+)
*굵은 글씨 = 최근 추가*

## 작업 규칙
- 새 도구 추가 시 index.html 카드, sitemap.xml 업데이트 필수
- SEO 키워드: 색상 변환, 컬러 팔레트, 그라디언트 생성기, 색상 코드 변환

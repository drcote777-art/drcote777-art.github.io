#!/usr/bin/env bash
# 가상 서울 공개용 사이트 만들기 (Cloudflare Pages: seoul-rehearsal.pages.dev)
#   Cloudflare 설정 — 빌드 명령: bash tools/build_seoul_public.sh / 빌드 출력 디렉터리: dist-seoul
#   seoul.html 을 고치고 main 에 올리면 Cloudflare 가 이 스크립트로 다시 만들어 자동 반영합니다.
#   가족용 연결(config.js: 함께 걷기·AI 중계, claude-web.js)은 공개용에서 뺍니다.
#   방문자 통계: Cloudflare Web Analytics 사용 중 (Pages 프로젝트 메트릭에서 켬, 배포할 때 Cloudflare가 자동으로 붙임).
#   측정 코드가 붙으려면 페이지에 <html><head>…</head><body>…</body></html> 틀이 있어야 함 (아래에서 확인).
#   지역 페이지: 서울 = index.html, 부산·경남 = busan.html, 동해안 = east.html, 전남·광주 = jnm.html. 첫 화면 '지역 고르기'의 서울 링크는 공개용에서 ./ 로 바꿉니다.
set -euo pipefail
OUT=dist-seoul
REGIONS="busan east jnm"
rm -rf "$OUT"
mkdir -p "$OUT"
cp -R assets3d "$OUT/"
cp seoul-config.js "$OUT/"
pub(){ sed -e 's#<script src="config.js"></script>##' -e 's#<script src="claude-web.js"></script>##' -e "s#\['seoul','seoul.html'#['seoul','./'#" "$1" > "$2"; }
pub seoul.html "$OUT/index.html"
for r in $REGIONS; do pub "$r.html" "$OUT/$r.html"; done
sed -e 's#"start_url": "seoul.html"#"start_url": "index.html"#' seoul.webmanifest > "$OUT/seoul.webmanifest"
for f in "$OUT"/index.html $(for r in $REGIONS; do echo "$OUT/$r.html"; done); do
  if grep -q 'src="config.js"\|src="claude-web.js"' "$f"; then echo "family scripts are still referenced in $f" >&2; exit 1; fi
  if ! grep -q '</head>' "$f" || ! grep -q '</body>' "$f"; then echo "$f has no <head>/<body>: Web Analytics cannot be injected" >&2; exit 1; fi
  if grep -q "\['seoul','seoul.html'" "$f"; then echo "region link to seoul.html not rewritten in $f" >&2; exit 1; fi
done
if grep -rqi 'drcote777' "$OUT"; then echo "personal name found in public files" >&2; grep -rli 'drcote777' "$OUT" >&2; exit 1; fi
if ! grep -q '"start_url": "index.html"' "$OUT/seoul.webmanifest"; then echo "manifest start_url not updated" >&2; exit 1; fi
echo "built $OUT: $(find "$OUT" -type f | wc -l) files, $(du -sh "$OUT" | cut -f1)"

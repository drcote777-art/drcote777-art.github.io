# 시험 스크립트 (Playwright)

- `busan_tour.js`: 장면마다 이동해 화면을 찍고 오류를 모읍니다. `PAGE=east.html SC='gyp:.05,ojk:.5' node busan_tour.js`
- `east_flow.js`, `jnm_flow.js`: 3일 일정을 처음부터 끝까지 눌러 보는 시험(탈것·퀴즈·가게·스탬프·호텔·케이블카·여행 마치기).
- `busan_fare_check.js`: 부산 KTX 요금(54,400원)과 퀴즈 확인.

먼저 `bash tools/build_seoul_public.sh`로 `dist-seoul`을 만든 뒤 돌립니다.
스크립트 안의 경로(`/opt/npm-tools/node_modules/playwright`, `/root/cruise/node_modules/three/build/three.min.js`)는 만들던 컴퓨터 기준이라, 다른 곳에서는 맞게 바꿔야 합니다.
- `cbk_flow.js`: 가상 충북 3일 일정 전체를 눌러 보는 시험 (LOC=en-US 로 영어 화면). `cbk_probe.js`: 충북 장면별 화면·스팟 확인.

# 지역 페이지 만드는 곳 (가상 서울 · 가상 부산·경남 …)

`seoul.html`, `busan.html`은 여기 있는 생성기로 만듭니다. 손으로 고치지 말고 생성기를 고친 뒤 다시 만드세요.

```bash
GEN_DIR=tools/regions/ python3 tools/regions/patch_seoul.py   # → tools/regions/seoul.html
GEN_DIR=tools/regions/ python3 tools/regions/patch_busan.py   # → tools/regions/busan.html (서울 생성기를 먼저 돌린 뒤 부산 자료로 바꿈)
cp tools/regions/seoul.html tools/regions/busan.html .
bash tools/build_seoul_public.sh                              # 공개용(dist-seoul) 확인
```

- `cruise_new.html`: 바탕 엔진(가상 크루즈) · `K_seoul.js` 등: 서울 장면·기능
- `K_busan_top.js`(부산 3D 소품) · `K_busan_br.js`(부산 장소별 장면) · `patch_busan.py`(일정·요금·사실·퀴즈, 출처는 파일 맨 위)
- 새 지역을 만들 때는 `patch_busan.py`처럼 `patch_<지역>.py`를 만들고, 첫 화면 '지역 고르기'(`patch_seoul.py`의 REGIONS)에 파일 이름을 넣습니다.

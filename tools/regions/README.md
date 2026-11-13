# 지역 페이지 만드는 곳 (가상 서울 · 가상 부산·경남 · 가상 동해안 …)

`seoul.html`, `busan.html`, `east.html`은 여기 있는 생성기로 만듭니다. 손으로 고치지 말고 생성기를 고친 뒤 다시 만드세요.

```bash
GEN_DIR=tools/regions/ python3 tools/regions/patch_seoul.py   # → tools/regions/seoul.html
GEN_DIR=tools/regions/ python3 tools/regions/patch_busan.py   # → tools/regions/busan.html
GEN_DIR=tools/regions/ python3 tools/regions/patch_east.py    # → tools/regions/east.html
cp tools/regions/seoul.html tools/regions/busan.html tools/regions/east.html .
bash tools/build_seoul_public.sh                              # 공개용(dist-seoul) 확인
```

- `cruise_new.html`: 바탕 엔진(가상 크루즈) · `K_seoul.js` 등: 서울 장면·기능
- `region_base.py`: 지역 공통 생성기. 서울 생성기를 돌린 뒤 지역 자료(일정·장소·사실·사진·퀴즈)로 바꿔 끼웁니다.
- `K_region_top.js` · `K_region_br.js`: 모든 지역이 함께 쓰는 3D 소품, 서울역(출발)·서울 버스터미널(도착) 장면
- 지역마다: `K_<지역>_top.js`(3D 소품) · `K_<지역>_br.js`(장소별 장면) · `patch_<지역>.py`(일정·요금·사실·퀴즈, 출처는 파일 맨 위) · `ph/PH_<지역>.json`(위키미디어 공용 사진)
- 새 지역: `patch_east.py`를 본떠 `patch_<지역>.py`를 만들고, 첫 화면 '지역 고르기'(`patch_seoul.py`의 REGIONS)와 `tools/build_seoul_public.sh`의 REGIONS에 넣습니다.

# TikTok promo videos (Virtual Seoul / Virtual Busan)

Vertical 1080×1920, 24 fps, about 27 s. Made by recording the real pages with Playwright, then encoding with ffmpeg.

How it works
- `base.js` opens a page from `dist-seoul/` (serves it as `http://site.test/`), maps Wikimedia photos to local files, installs a fake clock and a stepped `requestAnimationFrame`, so every recorded frame is exactly 1/24 s of page time.
- `vcap_seoul.js` and `vcap_busan.js` are the storyboards: captions (`#vcap`), tap circles (`#vtap`) and the end card (`#vend`) are overlaid on the page, then one JPEG per frame is saved (405×720 at device scale 2).
- `vcss.css` hides the game UI and styles the overlays. `dl_busan.py` downloads the Busan photos (960 px) for the photo boards.
- Paths at the top of `base.js` (scratch folder, repo) and the music file are from the session where the videos were made; adjust them before running again.

Encode (Busan)
```
ffmpeg -framerate 24 -i frames_busan/f%05d.jpg -ss 65.325 -t 27 -i music.mp3 \
 -filter_complex "[0:v]scale=1080:1920:flags=lanczos,format=yuv420p[v];[1:a]afade=t=in:st=0:d=0.15,afade=t=out:st=25.5:d=1.5,volume=-4.6dB[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -preset veryfast -crf 18 -c:a aac -b:a 192k -movflags +faststart -t 27 virtual_busan_tiktok.mp4
```
The Seoul video used the same music from 145.49 s. Cuts in the Busan video fall on the music's beat (every 0.75 s). The music file is not stored in this repository.

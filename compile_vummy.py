from pathlib import Path
from compile_video import compile_video_from_frames
import shutil


if __name__ == "__main__":
    ivp = Path(r"C:\Games\vummy")
    for dir in ivp.glob('*'):
        fp = 24
        fb = True
        if not dir.is_dir(): 
            continue  
        img_files = [x.stem for x in dir.glob('*.jpg')]
        fname = img_files[0] + '.mp4'
        yt = Path(r"D:\paradise\stuff\new\yummy_clips")
        yt.mkdir(parents=True, exist_ok=True)
        ovp = yt / fname
        if ovp.is_file():
            shutil.rmtree(dir)
            continue
        if len(img_files) < 15:
            fp = 24 - len(img_files)
        if len(img_files) > 150:
            fb = True
        try:
            compile_video_from_frames(dir, ovp, fps=fp, forward_backward=fb)
            shutil.rmtree(dir)


        except Exception as e:
            print(e)
            continue
        # Compile video with or without forward-backward effect
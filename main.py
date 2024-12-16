from moviepy.editor import VideoFileClip
from pathlib import Path

from extract_frames import extract_frames


def main():
    in_dir = r'C:\dumpinggrounds\stable_video\src\v'
    out_dir = r'C:\dumpinggrounds\stable_video\src\f'
    for x in Path(in_dir).glob('*.mp4'):
        ot = Path(out_dir) / x.stem
        ot.mkdir(parents=True, exist_ok=True)
        extract_frames(x, ot, x.stem[:50])

def extract_audio(video_path: Path, output_folder: Path):
    """
    Extract audio from a video file.
    
    :param video_path: Path to the video file.
    :param output_folder: Path to the folder where the audio will be saved.
    """
    video = VideoFileClip(str(video_path))
    audio = video.audio
    
    output_folder.mkdir(parents=True, exist_ok=True)
    
    audio_path = output_folder / "audio.mp3"
    audio.write_audiofile(str(audio_path))

if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser(description="Extract audio from a video.")
    # parser.add_argument("video_path", type=Path, help="Path to the video file.")
    # parser.add_argument("output_folder", type=Path, help="Path to the output folder.")
    
    # args = parser.parse_args()
    # vp = Path(r"C:\dumpinggrounds\stable_video\src\v\tati_evans_nude_fucking_sextape_porn5_1_sexdug_clip_15.mp4")
    # op = Path(r'C:\dumpinggrounds\stable_video\src\f')
    # extract_audio(args.video_path, args.output_folder)
    # extract_audio(vp, op)
    main()

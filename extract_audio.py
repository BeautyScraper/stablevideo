from moviepy.editor import VideoFileClip
from pathlib import Path

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
    import argparse
    parser = argparse.ArgumentParser(description="Extract audio from a video.")
    parser.add_argument("video_path", type=Path, help="Path to the video file.")
    parser.add_argument("output_folder", type=Path, help="Path to the output folder.")
    
    args = parser.parse_args()
    extract_audio(args.video_path, args.output_folder)

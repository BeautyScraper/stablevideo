from moviepy.editor import VideoFileClip
from pathlib import Path
from PIL import Image
import cv2


def extract_frames(video_path: Path, output_folder: Path,frame_prefix: str, frame_rate: int = 1):
    """
    Extract frames from a video file using OpenCV.
    
    :param video_path: Path to the video file.
    :param output_folder: Path to the folder where frames will be saved.
    :param frame_rate: Number of frames to extract per second.
    """
    video = cv2.VideoCapture(str(video_path))
    
    if not video.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return
    
    output_folder.mkdir(parents=True, exist_ok=True)
    
    fps = int(video.get(cv2.CAP_PROP_FPS))
    frame_interval = 20
    # frame_interval = fps // frame_rate
    
    frame_count = 0
    success, frame = video.read()
    while success:
        if frame_count % frame_interval == 0:
            frame_time = frame_count // fps
            frame_path = output_folder / f"{frame_prefix}_{str(frame_count).zfill(5)}.jpg"
            cv2.imwrite(str(frame_path), frame)
        success, frame = video.read()
        frame_count += 1
    
    video.release()

if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser(description="Extract frames from a video.")
    # parser.add_argument("video_path", type=Path, help="Path to the video file.")
    # parser.add_argument("output_folder", type=Path, help="Path to the output folder.")
    # parser.add_argument("--frame_rate", type=int, default=1, help="Frames to extract per second.")
    
    # args = parser.parse_args()
    for vp in Path(r'C:\dumpinggrounds\stable_video_srcs').glob('*.mp4'):
        op = Path(r'C:\dumpinggrounds\stable_video\src' ) / vp.stem
        # extract_frames(args.video_path, args.output_folder, args.frame_rate)
        extract_frames(vp, op, vp.stem[:50])

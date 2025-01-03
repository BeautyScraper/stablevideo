import re
from moviepy.editor import VideoFileClip
from pathlib import Path
from PIL import Image
import cv2
from tqdm import tqdm

fir_to_check_frames = Path(r'C:\dumpinggrounds\stable_video\out\to_sel')
def precompile_set():
    fir_to_check_frames.mkdir(parents=True, exist_ok=True)
    regex = '.* W1t81N (.*)\.'
    compile = re.compile(regex)
    string_set = set()
    for vp in fir_to_check_frames.glob('*.jpg'):
        match = compile.search(vp.name)
        if match:
            string_set.add(match.group(1))
    # breakpoint()
    return string_set

set_to_check_frames = precompile_set()

def extract_frames(video_path: Path, output_folder: Path,frame_prefix: str, frame_interval: int = 1):
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
    # frame_interval = 20
    # frame_interval = fps // frame_rate
    
    frame_count = 0
    success, frame = video.read()
    while success:
        if frame_count % frame_interval == 0:
            # frame_time = frame_count // fps
            frame_path = output_folder / f"{frame_prefix}_{str(frame_count).zfill(5)}.jpg"
            cv2.imwrite(str(frame_path), frame)
        success, frame = video.read()
        frame_count += 1
    
    video.release()

def extract_frames_co(video_path: Path, output_folder: Path,frame_prefix: str, frame_interval: int = 1):
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
    # frame_interval = 20
    # frame_interval = fps // frame_rate
    
    frame_count = 0
    success, frame = video.read()
    while success:
        if condition(frame_count,frame_prefix):
            # frame_time = frame_count // fps
            frame_path = output_folder / f"{frame_prefix}_{str(frame_count).zfill(5)}.jpg"
            cv2.imwrite(str(frame_path), frame)
        success, frame = video.read()
        frame_count += 1
    
    video.release()
def condition(frame_count,frame_prefix):
    frame_lapse = 10
    selecter_frame_lb = frame_lapse * (frame_count // frame_lapse)
    selecter_frame_ub = frame_lapse * ((frame_count // frame_lapse) + 1)
    frame_path_lb = f"{frame_prefix}_{str(selecter_frame_lb).zfill(5)}_0"
    frame_path_ub = f"{frame_prefix}_{str(selecter_frame_ub).zfill(5)}_0"
    # if frame_count > 180:
    #     breakpoint()
    if frame_path_lb in set_to_check_frames or frame_path_ub in set_to_check_frames:
        return True
    
    return False



if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser(description="Extract frames from a video.")
    # parser.add_argument("video_path", type=Path, help="Path to the video file.")
    # parser.add_argument("output_folder", type=Path, help="Path to the output folder.")
    # parser.add_argument("--frame_rate", type=int, default=1, help="Frames to extract per second.")
    
    # args = parser.parse_args()
    to_remove_dir = Path(r'C:\temp\deletable')
    for vp in tqdm([x for x in Path(r'C:\dumpinggrounds\stable_video\src_cap_video').glob('*.mp4')]):
        if len(vp.name) > 50:
            rp = vp.with_name(vp.name[:30]+vp.name[-10:])
            vp.rename(rp)
        op = Path(r'C:\dumpinggrounds\stable_video\src' ) / vp.stem
        # extract_frames(args.video_path, args.output_folder, args.frame_rate)

        if op.exists():
            # to_remove_dir.mkdir(parents=True, exist_ok=True)
            # vp.replace(to_remove_dir / vp.name)
            continue
        extract_frames(vp, op, vp.stem[:50],20)
    for vp in tqdm([x for x in Path(r'C:\dumpinggrounds\stable_video\fullSRc').glob('*.mp4')]):
        op = Path(r'C:\dumpinggrounds\stable_video\fsrc' ) / (vp.stem+'full')
        # extract_frames(args.video_path, args.output_folder, args.frame_rate)
        if op.exists():
            to_remove_dir.mkdir(parents=True, exist_ok=True)
            vp.replace(to_remove_dir / vp.name)
            continue
        extract_frames_co(vp, op, vp.stem[:50],1)

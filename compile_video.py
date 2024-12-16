from moviepy.editor import ImageSequenceClip
from pathlib import Path

def compile_video_from_frames(frames_folder: Path, output_video_path: Path, fps: int = 12, forward_backward: bool = False):
    """
    Compile a video from a folder of frame images.
    
    :param frames_folder: Path to the folder containing frame images.
    :param output_video_path: Path to save the output video.
    :param fps: Frames per second for the output video.
    """
    # Ensure the frames are sorted by their filename
    frame_files = sorted(frames_folder.glob('*.jpg'))
    
    # Convert frame files to list of strings
    frame_files = [str(frame) for frame in frame_files]
    
    if forward_backward:
        combined_frames = frame_files + frame_files[::-1]
    else:
        combined_frames = frame_files
    # Create the video clip from the image sequence
    clip = ImageSequenceClip(combined_frames, fps=fps)
    
    # Write the video file
    # clip.write_gif(str(output_video_path), fps=fps)
    clip.write_videofile(str(output_video_path), codec='libx264') 

if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser(description="Compile a video from a folder of frame images.")
    # parser.add_argument("frames_folder", type=Path, help="Path to the folder containing frame images.")
    # parser.add_argument("output_video_path", type=Path, help="Path to save the output video.")
    # parser.add_argument("--fps", type=int, default=24, help="Frames per second for the output video.")
    
    # args = parser.parse_args()
    # compile_video_from_frames(args.frames_folder, args.output_video_path, args.fps)
    ivp = Path(r"C:\dumpinggrounds\stable_video\out2")
    for dir in ivp.glob('*'):
        if not dir.is_dir(): 
            continue
        
        # Extract FPS value or default to 6 if an error occurs
        forward_backward = 'oo' in dir.name.lower()
        try:
            #replace all alphabets with '' in dir.name
            fps = int(''.join(c for c in dir.name if c.isdigit()))
            # fps = int(dir.name.replace('oo', ''))
        except ValueError:
            fps = 24
        
        # Check if 'oo' is in the directory name
        
        # Generate the output filename and path
        fname = [x.stem for x in dir.glob('*.jpg')][0] + '.mp4'
        ovp = Path(r"D:\paradise\stuff\new\FS") / fname
        
        # Compile video with or without forward-backward effect
        compile_video_from_frames(dir, ovp, fps=fps, forward_backward=forward_backward)

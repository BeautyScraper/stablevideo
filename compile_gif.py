from moviepy.editor import ImageSequenceClip
from pathlib import Path

def compile_video_from_frames(frames_folder: Path, output_video_path: Path, fps: int = 24, forward_backward: bool = False):
    """
    Compile a video from a folder of frame images.
    
    :param frames_folder: Path to the folder containing frame images.
    :param output_video_path: Path to save the output video.
    :param fps: Frames per second for the output video.
    :param forward_backward: If True, create a video that plays forward and then backward.
    """
    # Ensure the frames are sorted by their filename
    frame_files = sorted(frames_folder.glob('*.jpg'))
    
    # Convert frame files to list of strings
    frame_files = [str(frame) for frame in frame_files]
    
    # Duplicate frames in reverse order if forward_backward is True
    if forward_backward:
        combined_frames = frame_files + frame_files[::-1]
    else:
        combined_frames = frame_files
    
    # Create the video clip from the image sequence
    clip = ImageSequenceClip(combined_frames, fps=fps)
    
    # Write the video file
    clip.write_gif(str(output_video_path), fps=fps)
    # clip.write_videofile(str(output_video_path), codec='libx264')

if __name__ == "__main__":
    ivp = Path(r"C:\dumpinggrounds\stable_video\gif")
    for dir in ivp.glob('*'):
        if not dir.is_dir(): 
            continue
        
        # Extract FPS value or default to 6 if an error occurs
        try:
            fps = int(dir.name.replace('oo', ''))
        except ValueError:
            fps = 6
        
        # Check if 'oo' is in the directory name
        forward_backward = 'oo' in dir.name.lower()
        
        # Generate the output filename and path
        fname = [x.stem for x in dir.glob('*.jpg')][0] + '.gif'
        ovp = Path(r"D:\paradise\stuff\new\FS") / fname
        
        # Compile video with or without forward-backward effect
        compile_video_from_frames(dir, ovp, fps=fps, forward_backward=forward_backward)

import argparse
from pathlib import Path
import re
import os
import shutil

def move_files(source_to_move_from,target_to_move_to, reference_folder, regex_str):
    # Convert input_folder and reference_folder to Path objects
    input_folder_path = Path(source_to_move_from)
    reference_folder_path = Path(reference_folder)
    
    # Compile the regular expression
    regex_pattern = re.compile(regex_str)

    # Iterate through files in the reference folder
    for reference_file in reference_folder_path.rglob('*'):
        # Check if the item is a file
        if reference_file.is_file():
            # Apply regex to the file name in the reference folder
            regex_pattern = re.compile(regex_str)
            match = regex_pattern.search(reference_file.name)
            if match:
                # Obtain the matching string
                matching_string = match.group(1)
                
                # Search for files in the input folder and its subdirectories
                for input_file in input_folder_path.rglob('*' + matching_string+'.*'):
                    # breakpoint()
                    # Check if the item is a file
                    if input_file.is_file():
                        # Delete the file in the input folder
                        # Move the file to the target location
                        target_path = Path(target_to_move_to) / input_file.name
                        sourceFile = Path(source_to_move_from) / input_file.name
                        if not sourceFile.is_file():
                            return

                        shutil.move(str(sourceFile), str(target_path))
                        print(f"Moved: {input_file} to {target_path}")

                        print(f"Deleted: {input_file}")

def main():
    source_to_move_from = r'C:\dumpinggrounds\stable_video\src_cap_video'
    reference_folder = r'C:\dumpinggrounds\stable_video\out\to_sel'
    target_to_move_to = r'C:\dumpinggrounds\stable_video\fullSRc'
    regex_str =  '@hudengi (.*) W1t81N' 
    move_files(source_to_move_from,target_to_move_to, reference_folder, regex_str)

if __name__ == "__main__":
    main()

# python D:\Developed\Automation\mtut2\mtut\fsr.py D:\paradise\stuff\new\pvd_known D:\paradise\stuff\new\FS\bad_video '.mp4'
# python D:\Developed\Automation\mtut2\mtut\fsr.py D:\paradise\stuff\new\FS D:\paradise\stuff\new\FS\bad_video '.mp4'
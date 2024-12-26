import shutil
import random
from pathlib import Path

def overwrite_with_random_file(source_dir, target_file):
    """
    Selects a random file from source_dir and overwrites the target_file with its content.

    Parameters:
        source_dir (str): Path to the directory containing source files.
        target_file (str): Path to the file to be overwritten.
    """
    source_path = Path(source_dir)
    target_path = Path(target_file)

    # Check if source directory exists and is a directory
    if not source_path.is_dir():
        raise ValueError(f"The source path {source_dir} is not a valid directory.")

    # List all files in the directory
    files = [file for file in source_path.iterdir() if file.is_file()]

    if not files:
        raise ValueError(f"No files found in the directory {source_dir}.")

    # Randomly select a file
    random_file = random.choice(files)
    
    # Overwrite the target file
    shutil.copy(random_file, target_path)
    print(f"Overwritten {target_file} with {random_file}")

# Example usage
overwrite_with_random_file(r"D:\Developed\Automation\stablevideo\rand_config", r"D:\Developed\automatic1111\stable-diffusion-webui\ui-config.json")

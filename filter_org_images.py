from pathlib import Path
import re
import shutil

def organize_images_by_regex(dir_to_filter, organized_dir, regex_pattern):
    """
    Organizes images from `dir_to_filter` into a new directory in `organized_dir` based on a regex pattern.

    Args:
        dir_to_filter (str): The directory containing the images to be filtered.
        organized_dir (str): The base directory where the new directory will be created.
        regex_pattern (str): The regex pattern to extract the name for the new directory.

    Returns:
        None
    """
    dir_to_filter = Path(dir_to_filter)
    organized_dir = Path(organized_dir)

    if not dir_to_filter.exists():
        raise FileNotFoundError(f"The directory '{dir_to_filter}' does not exist.")

    organized_dir.mkdir(parents=True, exist_ok=True)

    # Create a dictionary to map directory names to files
    organized_files = {}

    # Iterate through files in the directory to filter
    for file_path in dir_to_filter.iterdir():
        # Skip if not a file
        if not file_path.is_file():
            continue

        # Match the regex pattern
        # breakpoint()
        match = re.search(regex_pattern, file_path.name)
        if match:
            new_dir_name = match.group(1)  # Use the matched part of the regex

            # Ensure the directory exists in organized_dir
            new_dir_path = organized_dir / new_dir_name
            if new_dir_name not in organized_files:
                new_dir_path.mkdir(exist_ok=True)
                organized_files[new_dir_name] = new_dir_path

            # Move the file to the new directory
            shutil.move(str(file_path), str(new_dir_path / file_path.name))

if __name__ == "__main__":
    dir_to_filter = r"C:\dumpinggrounds\stable_video\out\new"
    organized_dir = r"C:\Games\vummy"
    regex_pattern = '(?<=@hudengi )(.*)(?=full)'  # Replace with your actual regex pattern

    organize_images_by_regex(dir_to_filter, organized_dir, regex_pattern)

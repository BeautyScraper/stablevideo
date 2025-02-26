import argparse
import pathlib
import re
import shutil
import logging
from pathlib import Path

def merge_directories(src, dst):
    src_path = pathlib.Path(src)
    dst_path = pathlib.Path(dst)
    dst_path.mkdir(exist_ok=True)
    for item in src_path.glob('*'):
        dst_file_path = dst_path / item.name
        if not (dst_file_path).is_file():
            # brekpoint()
            try:
                shutil.move(str(item), str(dst_file_path))
            except Exception:
                breakpoint()
        else:
            item.unlink()
    src_path.rmdir()

def check_filenames_in_file(dir_path, file_path):
    # Get a list of all the filenames in the directory
    filenames = [file.name for file in pathlib.Path(dir_path).glob('*.jpg')]
    filenames += [file.name for file in pathlib.Path(dir_path).glob('*.jpeg')]

    # Read the contents of the file
    with open(file_path, 'r') as f:
        file_contents = f.read()

    # Check if all the filenames are present in the file
    for filename in filenames:
        # breakpoint()
        if filename not in file_contents:
            logging.debug(f'{filename} not found in')
            return False
    logging.info('returning True')
    return True


def move_directory_if_files_in_file(src_parent_dir):
    for dir_path in pathlib.Path(src_parent_dir).iterdir():
        file_path = dir_path / 'sdfs_records.opml'
        if file_path.is_file() and dir_path.is_dir() and check_filenames_in_file(dir_path, file_path):
            # Move the directory to the target directory
            logging.info('Move the directory to the target directory')
            try:
                shutil.rmtree(str(dir_path))
            except Exception as e:
                logging.debug(f'Could not move {dir_path} because' + str(e))
                # merge_directories(str(dir_path), target_dir)
                pass
def del_file_if_correspond_file_does_not_exist(src_parent_dir:str,correspond_parent_dir: list[str]):
    correspond_dir_set = set()
    for parent_dir in correspond_parent_dir:
        for dir_path in pathlib.Path(parent_dir).iterdir():
            if dir_path.is_file():
                
                if(re.search('(.*) @hudengi (.*) W1t81N (.*)',str(dir_path.name))):
                    file_name_to_save = re.search('(.*) @hudengi (.*) W1t81N (.*)',str(dir_path.name))[2]
                    correspond_dir_set.add(file_name_to_save)
                else:
                    breakpoint()
            else:
                    # breakpoint()
                    correspond_dir_set.add(dir_path.name)
                            
    
    for dir_path in pathlib.Path(src_parent_dir).glob('*.mp4'):
        if not Path(dir_path).stem in correspond_dir_set:
            dir_path.unlink()

                # breakpoint()
        

def main():
    # parser = argparse.ArgumentParser(description='Move directories containing all the filenames in a file')
    # parser.add_argument('src_parent_dir', help='path to the source parent directory', default=r'C:\Heaven\Haven\brothel')
    # parser.add_argument('target_dir', help='path to the target directory',default=r'D:\paradise\stuff\new\imageset2')
    logging.debug('Move the directory to the target directory')
    # # parser.add_argument('file_path', help='path to the file containing the filenames')
    # args = parser.parse_args()

    move_directory_if_files_in_file(r'C:\dumpinggrounds\stable_video\src')
    # move_directory_if_files_in_file(r'D:\paradise\stuff\new\imageset', r'D:\paradise\stuff\new\imageset2') 
    # pathlib.Path(r'C:\dumpinggrounds\stable_diff_dg\source2').mkdir(exist_ok=True)
    # pathlib.Path(r'D:\paradise\stuff\new\imageset').mkdir(exist_ok=True)
    # pathlib.Path(r'C:\dumpinggrounds\stable_diff_dg\source2').mkdir(exist_ok=True)
    # move_directory_if_files_in_file(r'C:\dumpinggrounds\stable_diff_dg\source', r'D:\paradise\stuff\new\imageset2')
    del_file_if_correspond_file_does_not_exist(r'C:\dumpinggrounds\stable_video\src_cap_video',[r'C:\dumpinggrounds\stable_video\out\caps',r'C:\dumpinggrounds\stable_video\out\to_sel', r'C:\dumpinggrounds\stable_video\src'] )

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()

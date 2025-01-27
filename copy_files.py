import os
import argparse
import shutil

def copy_files(files, path = './seleccion', prefix = 'DSC_', extension = '.NEF'):
    #   Get Directory
    parent_dir = os.path.abspath('.')
    target_dir = os.path.join(parent_dir, path)

    #   Make Directory if doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    #   Successfully copied files counter
    count = 0

    for file in files:
        file_name = f"{prefix}{file}{extension}"
        try:
            shutil.copy(file_name, target_dir)
            count+=1
            print(f"File {file_name} copied into {target_dir}")
        except FileNotFoundError:
            print(f"File {file_name} not found")
        except PermissionError:
            print(f"Not enough permissions to cpy {file_name}")
    
    print(f"Files copied: {count}")
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Copy files into a new location')
    parser.add_argument("--files", help='List of files to copy', required=True)
    parser.add_argument("--target", help='The relative path to the new location')
    parser.add_argument("--prefix", help='The prefix of the file, in case it is different of DSC_')
    parser.add_argument("--extension", help='The extension of the file')

    args = parser.parse_args()

    files = args.files.split('-')
    path = args.target if args.target is not None else '../seleccion'
    prefix = args.prefix if args.prefix is not None else 'DSC_'
    extension = args.extension if args.prefix is not None else '.NEF'

    copy_files(files, path, prefix, extension)
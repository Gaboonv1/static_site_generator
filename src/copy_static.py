import os
import shutil


def sync(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    copy_files_recursive(source,dest)    

def copy_files_recursive(source, dest):
    for entry in os.listdir(source):
        source_path = os.path.join(source, entry)
        dest_path = os.path.join(dest, entry)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
             os.mkdir(dest_path)   
             copy_files_recursive(source_path, dest_path)
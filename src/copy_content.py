import os
import shutil

def copy_static(src,dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    
    for file_name in os.listdir(src):
        src_path = os.path.join(src,file_name)
        dst_path = os.path.join(dst,file_name)
        
        if os.path.isfile(src_path):
            shutil.copy(src_path,dst_path)
            print(f"File was copied from {src_path} to {dst}")
            
        elif os.path.isdir(src_path):
            os.mkdir(dst_path)
            copy_static(src_path,dst_path)
    
    
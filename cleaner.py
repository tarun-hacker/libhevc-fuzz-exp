import time
import os
CORPUS_DIR = "corpus"
SEED = "out.h265"

def delete():
    base_path = os.path.join(os.getcwd(),CORPUS_DIR)
    files = os.listdir(base_path)
    for file in files:
        file_path = os.path.join(base_path,file)
        stat = os.stat(file_path)
        if file!=SEED and (time.time()-stat.st_mtime)  > 30:
            os.remove(file_path)
            print("removed: "+file)

while True:
    delete()
    time.sleep(20)

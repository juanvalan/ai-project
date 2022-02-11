import glob
import os
import shutil
from rich.progress import track


directories = glob.glob('/home/amicis/Documentos/un/ai/DBturbidity/*')

for directory in track(directories):
    name = directory.split('_')[0].split('/')[-1]
    files = glob.glob( os.path.join(directory, '*' ) )

    for idx, file in enumerate(files):
        path = '/home/amicis/Documentos/un/ai/new_db'
        new_file_path = os.path.join(path, name, "_".join(file.split('/')[-2:]) )
        os.makedirs(os.path.dirname( new_file_path), exist_ok=True )
        shutil.copy(file, new_file_path ) 

    

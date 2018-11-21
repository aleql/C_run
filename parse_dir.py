import os
import shutil

import sys


"""
Copia cada tarea, test y makefile a su carpeta correspondiente
"""
def parse_dir(files_dir, result_dir, content_folder_dir):

    # Iterate over all files of the folder
    files = os.listdir(files_dir)
    for file in files:
        # Obtain rut and name of file
        file_l = file.split("_")
        rut = file_l[1]
        fname = file_l[2]
        print(" >Copiado {}".format(file))

        # Crear directorio para el archivo, copiarlo, y moverlo ahi
        oldroute = os.path.join(files_dir, file)
        newroute = os.path.join(result_dir, rut)

        # Crear carpeta
        os.mkdir(newroute)

        # Copiar ahi file, test y makefile
        shutil.copy(oldroute, newroute)

        # Copiar contenidos de la carpeta de contenidos
        content_files = os.listdir(content_folder_dir)
        for content_file in content_files:
            shutil.copy(os.path.join(content_folder_dir, content_file), newroute)

        # Renombrar
        os.rename(os.path.join(newroute, file), os.path.join(newroute, fname))


"""
/home/ale-chan/tareas/SO/T/test/tareas /home/ale-chan/tareas/SO/T/results /home/ale-chan/tareas/SO/T/test/content
"""

# parse_dir(sys.argv[1], sys.argv[2], sys.argv[3])
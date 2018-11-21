from compile_and_run import compile_and_run
from extract_zip import extract_zip
from parse_dir import parse_dir

if __name__ == '__main__':


    # Extract zip
    q_zip = input(">> Extraer zip? [enter/n] ")
    if q_zip != 'n':
        hw_directory = input(" >> Ingrese directorio donde se encuentra el zip: ")
        zip_name = input(" >> Ingrese nombre del zip: ")

        files_dir = extract_zip(hw_directory, zip_name)
        print(" >> Zip extraido con exito en direccion: {}\n".format(files_dir))
    else:
        files_dir = input(" >> Ingrese direccion de carpeta donde se ubican las tareas: ")


    # Copiar tareas a cada directorio
    copy_dir = input(" >> Copiar cada archivo a una carpeta? [enter/n]]: ")
    if copy_dir != 'n':
        # Copy to each directory
        print(" >> Se procedera a copiar cada tarea a una carpeta separada")
        result_dir = input(" >> Ingrese direccion de carpeta donde desea copiar las tareas: ")
        content_folder_dir = input(" >> Ingrese direccion de carpeta con contenidos (Makefile, Tests, headers, etc): ")
        fname = input(" >> Ingrese nombre del archivo")
        parse_dir(files_dir, result_dir, content_folder_dir, fname)
        print(" >> Se crearon las carpetas con exito\n")
    else:
        result_dir = input(" >> Ingrese direccion de carpeta donde se encuentran las tareas: ")

    # Correr y testear cada tarea
    compilar = input(" >> Correr y compilar cada tarea? [enter/n] ")
    if compilar != 'n':
        test = input(" >> Ingrese nombres del test: ")
        compile_and_run(result_dir, test)

    print(" chao!!")
    print("                                     O W O /")





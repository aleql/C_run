import csv
import shlex
import subprocess
import os
import sys



def compile_and_run(results_folder, test_name):

    # ista de tareas con resultado de correr c/u
    resultados = {}


    # Comando correr test
    cmd_test = "./{}".format(test_name)

    # ir carpeta por carpeta
    for folder in os.listdir(results_folder):

        compilar = input(" >> Compilar tarea {} ??? [enter/n]: ".format(folder))
        if compilar != 'n':
            # compilar
            cwd = os.path.join(results_folder, folder)
            print(' >> Compilando tarea {}...'.format(folder))
            result = subprocess.run(shlex.split('make'), cwd=cwd, stdout=subprocess.PIPE)
            print(result.stdout.decode('utf-8'))


            # Fallo al compilar
            if result.returncode != 0:
                # print(result.stderr.decode('utf-8'))
                print("--- Tarea fallo en compilar!!!! ---\n")
                resultados[folder] = 1
                continue

            # Compilo bien preguntar si correr
            print(" >> Compilado con exito!! ")
            correr = input(" >> Correr tarea {} ??? [enter/n]: ".format(folder))
            if correr != 'n':
                result = subprocess.run(shlex.split(cmd_test), cwd=cwd, stdout=subprocess.PIPE)
                print(result.stdout.decode('utf-8', 'ignore'))
                # print(unicode(result.stdout, errors='replace'))

                # Fallo al testear
                if result.returncode != 0:
                    # print(result.stderr.decode('utf-8'))
                    print("--- Tarea fallo en testear!!!! ---\n")
                    resultados[folder] = 1
                    continue
                else:
                    #Paso bien?
                    nota = input(" >> Test paso bien? [enter/n]")
                    if nota != 'n':
                        resultados[folder] = 7
                    else:
                        resultados[folder] = 1
                    continue

        resultados[folder] = 0

    print(resultados)
    # Guardar resultados
    with open('results.csv', 'w') as f:  # Just use 'w' mode in 3.x
        writer = csv.writer(f)
        for row in resultados.items():
            writer.writerow(row)

    return resultados

# compile_and_run(sys.argv[1], sys.argv[2])


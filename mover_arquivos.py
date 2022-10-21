
import os
import shutil

caminho_original = r'C:\Users\Home\Desktop\Estagio\Estudos_EA'
caminho_novo = r'C:\Users\Home\Desktop\Estagio\Estudos_EA2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'pasta {caminho_novo} ja existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if file:
            os.remove(new_file_path)


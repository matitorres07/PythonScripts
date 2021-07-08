from importlib import machinery
import os 
import shutil
from sys import path
import ctypes, sys

carpetas_ = os.listdir(r'C:\Users\Mati\Desktop\destino')
carpetas_b = [int(i) for i in carpetas_]
sorted(carpetas_b)

if carpetas_b == []:

    ultima_backup = 0
    backup_mas_viejo = 0
    numero_backup = 1
else :
    ultima_backup = max(carpetas_b)
    backup_mas_viejo = min(carpetas_b)
    numero_backup = ultima_backup + 1

cantidad_backups =  (len(list(os.listdir(r'C:\Users\Mati\Desktop\destino'))))

main = r'C:\Users\Mati\Desktop\destino\{}'.format(numero_backup)
dirs = r'C:\Users\Mati\Desktop\origen'


if cantidad_backups < 10:
    carpetas_a_mover = [ f.path for f in os.scandir(dirs) if f.is_dir() ]
    shutil.copytree(dirs,main)
    #numero_backup += 1
    
else : 
    remove = r'C:\Users\Mati\Desktop\destino\{}'.format(backup_mas_viejo)
    shutil.rmtree(remove)
    shutil.copytree(dirs,main)





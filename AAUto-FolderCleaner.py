from importlib import machinery
import os 
import shutil
from sys import path

#main = r'C:\Users\Mati\Desktop\destino'
dirs = r'C:\Users\Mati\Desktop\origen'

extension_paths = {

        # audio
        '.aif':    r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        '.cda':    r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        '.mid':    r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        '.midi':   r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        '.mp3':    r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        '.mpa':    r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        '.ogg':    r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        '.wav':    r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        '.wma':    r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        '.wpl':    r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        '.m3u':    r'C:\Users\Mati\Desktop\destino\Archivos Musica',
        # text
        '.txt':    r'C:\Users\Mati\Desktop\destino\Archivos Texto',
        '.doc':    r'C:\Users\Mati\Desktop\destino\Archivos Texto',
        '.docx':   r'C:\Users\Mati\Desktop\destino\Archivos Texto',
        '.odt ':   r'C:\Users\Mati\Desktop\destino\Archivos Texto',
        '.pdf':    r'C:\Users\Mati\Desktop\destino\Archivos Texto',
        '.rtf':    r'C:\Users\Mati\Desktop\destino\Archivos Texto',
        '.tex':    r'C:\Users\Mati\Desktop\destino\Archivos Texto',
        '.wks ':   r'C:\Users\Mati\Desktop\destino\Archivos Texto',
        '.wps':    r'C:\Users\Mati\Desktop\destino\Archivos Texto',
        '.wpd':    r'C:\Users\Mati\Desktop\destino\Archivos Texto',
    
        # images
        '.ai':     r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.bmp':    r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.gif':    r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.jpg':    r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.jpeg':   r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.png':    r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.ps':     r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.psd':    r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.svg':    r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.tif':    r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.tiff':   r'C:\Users\Mati\Desktop\destino\Archivos Imagenes',
        '.cr2':    r'C:\Users\Mati\Desktop\destino\Archivos Imagenes'
        }

carpetas_a_crear = []

for key,values in extension_paths.items():
    if values not in carpetas_a_crear:
        carpetas_a_crear.append(values)

for items in carpetas_a_crear:
    if  os.path.exists(items):
        print ("El directorio ya esta creado")
    else:
        os.makedirs(items)
        print("Directorio creado en : ", items)

for root,subdirs,files in  os.walk(dirs):
    print('root: ', root)
    print('subdirs: ', subdirs)
    print('files: ', files)
    
    for file in files:
        path = os.path.join(root,file)
        filename, file_extension = os.path.splitext(file)
        filename = filename.lower ()
        file_extension = file_extension.lower ()
        print (filename, file_extension)
        for keys,values in extension_paths.items():
            if keys == file_extension:
                print ("El archivo es un ",file_extension, " mover a",values)
                shutil.move(path,values)
        







        



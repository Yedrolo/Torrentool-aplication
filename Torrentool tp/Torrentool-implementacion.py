# Antes de correr el programa es necesario tener un archivo torrent en cualquier ubicacion ,
# esto se puede realizar descargando un archivo torrent desde cualquier lado o de forma mas sencilla utilizando la herramienta que nos
# proporciona la libreria torrentool
# Colocando torrentool torrent create "C:\alguna_ubicacion" en la terminal , creara un archivo torrent con el mismo nombre de la ubicacion especificada 
 


from torrentool.api import Torrent
import os.path


# Especifica la ruta del archivo torrent con el que se intentara operar
archivo_torrent = 'C:\\Users\\Yedro\\Primer.torrent'

# Verifica si el archivo torrent existe en la ruta especificada
if os.path.exists(archivo_torrent):
    # Si archivo torrent existe, procede a abrirlo y realizar modificaciones
    my_torrent = Torrent.from_file(archivo_torrent)
    print("Tamaño total del archivo en bytes:", my_torrent.total_size) # Muestra el atamaño del archivo en bytes 
    print("El enlace magnético del archivo es:", my_torrent.magnet_link) # Muestra el enlace magnetico del archivo
    my_torrent.comment = 'Me gustan los torrents' # Modifica el comentario que se encuentra adentro del torrent ,por ejemplo "d7:comment23" 
    my_torrent.to_file()
else:
    # Lanza una excepcion si el archivo no se encuentra o no existe
    print("El archivo torrent no existe en la ruta especificada:", archivo_torrent)
 

# Aquí se crea un nuevo torrent desde un directorio, en este caso C:\\Trash
new_torrent = Torrent.create_from('C:\\Trash')  # Recorre el directorio C:\Trash y todos sus subdirectorios, recopilando la información necesaria para crear el archivo torrent.
new_torrent.announce_urls = 'udp://tracker.openbittorrent.com:80'
new_torrent.to_file('another.torrent')  # Nombra al archivo torrent creado como "another.torrent" , este se guarda en la misma ubicación que Primer.Torrent
print("Tamaño total del nuevo archivo en bytes:", new_torrent.total_size)
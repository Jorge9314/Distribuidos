# Enunciado Taller 5

Construir un sistema cliente-servidor utilizando sockets que permita enviar un archivo completo de texto de cualquier tamaño, desde el servidor al cliente. El cliente debe poder escoger el archivo a partir de una lista enviada por el servidor.

--- 
## Solucion al Taller #5

Como solución al problema planteado, se crea un [Servidor](server.py) y un [Cliente](client.py) con socket TCP para garantizar el envio completo de la información.
+ El servidor lee todos los archivos en el directorio que tengan extension .txt
+ El cliente escoge cual de estos archivos desea
+ El servidor envia por tramas al cliente el archivo
+ El cliente guarda esta informacion en nuevo documento llamado rcv-*nombreArchivo*.txt

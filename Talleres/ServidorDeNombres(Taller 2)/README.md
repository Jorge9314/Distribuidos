# Servidor de nombres

> Un cliente, un servidor de nombres, y siete servidores de operaciones

1. El cliente se comunica inicialmente con el servidor de nombres preguntando por un servicio.
2. El servidor de nombres se comunica con todos los servidores de operaciones activos, los cuales le envian su ***Servicio, dirección y puerto*** a lo que el servidor contesta con un ***OK*** confirmando que fueron almacenados en su tabla de servidores.
3. Posteriormente el servidor de nombres le indica al cliente la dirección del servicio solicitado. 
4. Finalmente el cliente se comunica directamente con el servidor del servicio solicitado para realizar la operación requerida.

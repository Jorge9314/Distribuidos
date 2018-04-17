## Lamport: Algoritmo para sincronizar relojes

+ Def. a ocurre antes de b a --> b
+ Si a es un evento dentro del mismo proceso que ocurre antes de b entonces a --> b es V
+ Si a es el evento de enviar mensaje y b es el envento de la recepción, entonces a --> b es V
+ "Ocurre antes de" es una relación transitiva: si dos eventos X e Y están en procesos diferentes que no intercambian mensjaes entonces X --> Y es F. y Y --> es F. Eventos Concurrentes
+ Si T(a) es la marca de tiempo donde ocurre el evento a y a --> b es verdadero, entonces T(a) < T(b)

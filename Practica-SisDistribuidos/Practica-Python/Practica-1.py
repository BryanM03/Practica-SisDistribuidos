import threading


import time

start_time = time.time()

class Counter:
    def __init__(self):
        self.counter = 0
        
    def increment(self):
        self.counter += 1
        
    def get(self):
        return self.counter

counter = Counter()

class CountingThread(threading.Thread):
    def run(self):
        for x in range(500000):
            counter.increment()

def main():
    t1 = CountingThread()
    t2 = CountingThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(counter.get()) # debería dar 1000000

if __name__ == '__main__':
    main()

end_time = time.time()

print("La suma es:", sum)
print("El tiempo de ejecución fue:", end_time - start_time, "segundos")




###En este código se utilizan hilos (threads) para incrementar el contador en paralelo. Se definen dos hilos llamados 
# "t1" y "t2" que ejecutan el método "run" de la clase "CountingThread". El método "run" simplemente incrementa el 
# contador llamando al método "increment" de la instancia "counter" de la clase "Counter".
##Los hilos se inician llamando al método "start" de cada hilo. Esto permite que los hilos se ejecuten en paralelo. 
# Luego, se espera a que los hilos terminen de ejecutar llamando al método "join" de cada hilo.
##Una vez que los hilos han terminado de ejecutar, se imprime el valor del contador llamando al método "get" de la instancia "counter".
#  El resultado debería ser 1000000, ya que cada hilo incrementa el contador 500000 veces.

##En Python, self es una convención que se utiliza para referirse a la instancia actual de una clase.
#  En la clase Counter, self se utiliza para acceder al atributo counter y a los métodos increment y 
# get de la instancia de la clase. Cuando se crea una instancia de la clase, self se refiere a dicha instancia 
# y se utiliza para realizar operaciones sobre ella, como incrementar o obtener el valor del contador. 
# En resumen, self es necesario para acceder a los atributos y métodos de una instancia de una clase en Python.
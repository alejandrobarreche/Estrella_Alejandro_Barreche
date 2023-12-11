### ESTRELLAS ###

"""
El siguiente código permite la ilustración de estrellas poligonales mediante el uso del 
módulo turtle, el cual permite precisamente la ilustración de objetos.
"""

import turtle


# Pedir el número de vértices de la estrella

def pedir_numero():
    while True:
        numero_puntas = input("Dime el número de puntas que quieres que tenga tu estrella \n(recuerda que las estrellas son mínimo de 5 puntas): ")
        try:
            numero_puntos = int(numero_puntas)
            if numero_puntos >= 5:
                return numero_puntos
            else:
                print("Ese número no es válido. Por favor introduzca un número mayor o igual a 5.")
        except:
            print("Entrada no válida. Por favor, introduzca un número mayor o igual a 5.")
            

# Esta función implementa toda la lógica necesaria para dibujar las estrella
def dibujar_estrella(num_puntas, x_size = 600, y_size = 600):

    '''
    num_puntas : int  # Esta variable almacena el número de puntas que tiene la estrella
    x_size, y_size: int  # Estas variables permiten establecer el número de píxeles de la pantalla de visualización
    '''


    # Configuración inicial
    ventana = turtle.Screen()
    ventana.bgcolor("lightgreen")
    ventana.setup(x_size, y_size)
    

    # Crear una tortuga
    tortuga = turtle.Turtle()
    tortuga.speed(3)
    tortuga.shape("turtle")
    tortuga.color("black", "orange")
    tortuga.shapesize(1)
    tortuga.width(3)
    tortuga.setpos(-((x_size/2)-100),0)  #Esto nos permite establecer siempre a 100 píxeles del borde izquierdo la tortuga desde el principio


    # Calcular el ángulo entre cada punta de la estrella
    distancia = x_size - 200    # Lo calculamos en función del número de píxeles para cerntrarlo
    resto = num_puntas % 2     
    cociente = num_puntas / 2
    if (resto) != 0:                              # Si el numero de puntas es impar
        angulo = 180 - (180 / num_puntas)
    elif (resto) == 0:                            # Si el número de puntas es par
        if (cociente) % 2 == 0:                          # Si el cociente es par
            angulo = 180 - (360 / num_puntas)
        else:                                            # Si el cociente es impar
            angulo = 180 - (360/ (num_puntas/2) )
            
    
    # Dibujar la estrella
    
    '''
    En caso de que la estrella tenga 6 puntas falla, por lo que se ha implementado una lógica
    distinta para poder procesar una estrella en caso de que fuera de 6 puntas
    '''
    
    if num_puntas != 6:
        tortuga.begin_fill()           # Para rellenar de color los huecos
        for _ in range(num_puntas):
            tortuga.forward(distancia)  # Longitud de la punta
            tortuga.right(angulo) 
        tortuga.end_fill()  
             
    else:                # Lógica alternativa para dibujar estrella de 6 puntas
        for _ in range(3):
            tortuga.forward(distancia)  # Longitud de la punta
            tortuga.right(120)
        tortuga.goto((-200 + (distancia/3)), 0)
        tortuga.goto(0,(22+(2**0.5)*(distancia/6)))
        tortuga.left(240)
        for _ in range(3):
            tortuga.forward(distancia)  # Longitud de la punta
            tortuga.left(120)
    

    # Cerrar la ventana al hacer clic
    ventana.exitonclick()


# La función principal
def main():
    numero_puntas = pedir_numero()
    dibujar_estrella(numero_puntas)
    
if __name__ == "__main__":
    main()
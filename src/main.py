
class Calc:
        def sumar ( self, x , y):
                return (x + y)

        def resta (self, x , y):
                return (x - y)

        def multi (self,x , y):
                return (x * y)

        def div (self, x , y):
                return(x / y)

        def pot (self, x, y):
                result = 1
                for _ in range(y):
                        result = result * x
                return result

        def menu(self):
                print('')
                print(' Selecciona una opcion ')
                print(' 1- Suma')
                print(' 2- Resta')
                print(' 3- Multiplicacion')
                print(' 4- Dividir')
                print(' 5- Potencia')
                print(' 0- Salir')


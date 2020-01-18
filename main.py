import logic
import assets
import time

def main():

  assets.pintarBienvenido()
  assets.tocarCancion()

  input("Pulsa ENTER para jugar...")

  juego = logic.Juego()
  juego.elegirPuerta()

  input("Pulsa ENTER para salir...")
  #pausa = input("Pulsa una tecla")
  
if __name__== "__main__":
  main()

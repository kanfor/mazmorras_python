import assets
import random
import time

class Juego():
  TOTAL_PUERTAS = 2
  nivel = 1
  puerta_correcta = 1
  game_over = False
  
  def obtenerPuertaCorrecta(self):
    self.puerta_correcta = random.randint(1, 3)

  def elegirPuerta(self):
    assets.pintarMazmorra(self.nivel)
    self.obtenerPuertaCorrecta()
    self.hacerPregunta()

  def hacerPregunta(self, error = ''):
    try:
      if error == 'no_numero':
          print('Solo se permiten números, gracioso.')
      if error == 'numero_excedido':
          print('Solo se permiten números, gracioso.')
      puerta = input('Elige la puerta a cruzar:')
      if puerta == '':
        self.elegirPuerta()
      if int(puerta) > 3 or int(puerta) < 0:
        self.hacerPregunta('numero_excedido')
      if int(puerta) == int(self.puerta_correcta):
        self.hasAcertado()
      else:
        self.hasPerdido()
    except ValueError:
        if self.game_over == False:
          self.hacerPregunta('no_numero')

  def hasAcertado(self):
    if self.nivel > self.TOTAL_PUERTAS:
      assets.pintarHasGanado()
    else:
      print('La puerta era la ' + str(self.puerta_correcta) + ' y has ACERTADO')
      assets.tocarCancion()
      self.nivel += 1
      time.sleep(0.5)
      self.elegirPuerta()

  def hasPerdido(self):
    self.game_over = False
    print('La puerta era la ' + str(self.puerta_correcta) + ' y has FALLADO')
    assets.muerteCancion()
    time.sleep(0.5)
    assets.pintarMuerte()
    reintentar = input('¿Desdeas reintentar? [s/n]:')
    if reintentar == 's':
      self.nivel = 1
      self.elegirPuerta()

    
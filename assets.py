import winsound
import os

def pintarBienvenido():
    print('┌──────────────────────────────────────────┐')
    print('│ ╋ Bienvenido a las mazmorras de Python ╋ │')
    print('└──────────────────────────────────────────┘')
    print('')
    print('Acabas de entrar en los dominios de Gosu,')
    print('el gran brujo. Elige sabiamente cada puerta')
    print('para poder escapar.')
    print('¡Solo una es correcta! Logra avanzar tan')
    print('solo CINCO veces y la libertad será tuya.')
    print('')

def pintarMazmorra(puerta):
    os.system('cls')
    print('')
    print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒' + str(puerta) + '▒▒▒╋╋╋╋╋▒▒▒▒▒▒▒▒▒╋╋╋╋╋▒▒▒▒▒▒▒▒▒╋╋╋╋╋▒▒▒▒▒')
    print('▒▒▒▒▒╋╋1╋╋▒▒▒▒▒▒▒▒▒╋╋2╋╋▒▒▒▒▒▒▒▒▒╋╋3╋╋▒▒▒▒▒')
    print('▒▒▒▒▒╋╋╋╋╋▒▒▒▒▒▒▒▒▒╋╋╋╋╋▒▒▒▒▒▒▒▒▒╋╋╋╋╋▒▒▒▒▒')
    print('')
    print('')

def pintarMuerte():
    os.system('cls')
    print('')
    print('                ╭─────────╮')
    print('                │    ┼    │')
    print('                │  R.I.P. │')
    print('                │         │')
    print('               ┙└─────────┘┕')
    print('         AQUI FALLECIO UN PERDEDOR')
    print('╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤')
    print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
    print('')

def pintarGanar():
    os.system('cls')
    print('')
    print('           ▒ ▒ ▒ ▒         ▒ ▒ ▒ ▒')
    print('           ▒▒▒▒▒▒▒         ▒▒▒▒▒▒▒')
    print('            ▒▒╋▒▒           ▒▒╋▒▒')
    print('            ▒▒▒▒▒ ▒ ▒ ▒ ▒ ▒ ▒▒▒▒▒')
    print('            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
    print('            ▒▒▒▒▒▒▒▒╋╋╋╋╋▒▒▒▒▒▒▒▒')
    print('            ▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒')
    print('═══════════════════════════════════════════')
    print('')
    print('De algún modo que se escapa a la compresión, has')
    print('logrado escapar. Seguro que has hecho trampas, pero')
    print('gracias por jugar, aunque seas un tramposo.')
    print('')

def pintarHasGanado():
    os.system('cls')
    print('Has ganado')
    muerteCancion()
    tocarCancion()

def tocarCancion():
    frequency: int = 500
    duration: int = 20
    for x in range(10):
        f = frequency + (x * 100)
        winsound.Beep(f, duration)

def muerteCancion():
    frequency: int = 1000
    duration: int = 20
    for x in range(10):
        f = frequency - (x * 100)
        winsound.Beep(f, duration)
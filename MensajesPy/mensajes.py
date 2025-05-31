import pywhatkit as kit
import pyautogui
import time
import argparse

parser = argparse.ArgumentParser(description="Un programa para enviar mensajes de whats!")
parser.add_argument("mensaje", help="Tu mensaje", default='Mensaje por default!!!') # Mensaje a enviar
parser.add_argument("--veces", type=int, help="10", default=5)  # Número de veces a enviar
parser.add_argument("--numero", help="+5211234567890")  # Número telefonico en formato internacional, ejemplo: +5211234567890

args = parser.parse_args() # Simplificacion de variable

time.sleep(5)  # Tiempo de espera 5 segundos para que abras el chat correcto

if args.numero:
    # Envio de mensaje a un numero en especifico
    for _ in range(args.veces):
        # Programa el mensaje para enviarlo 1 minuto después de la hora actual
        hora = time.localtime().tm_hour
        minuto = time.localtime().tm_min + 1
        kit.sendwhatmsg(args.numero, args.mensaje, hora, minuto, wait_time=10) # Tiempo desde que esta escrito hasta que se envia
        time.sleep(60)  # espera 1 minuto para que WhatsApp no bloquee el envío
else:
    # Envio de mensajes al chat abierto en pantalla
    for _ in range(args.veces):
        pyautogui.write(args.mensaje)
        pyautogui.press('enter')
        time.sleep(1)
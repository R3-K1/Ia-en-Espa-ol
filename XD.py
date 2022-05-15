import os
import sys
import time
import socket
import requests

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3.0 / 100)

print("""─── ── ── ─ ── ── ── ── ── ── ─ 
─── ── ── ─ ██ ██ ██ ── ── ── ─ 
─── ── ── ─ ██ ░░ ██ ██ ── ── ─ 
─██ ██ ██ ─ ██ ██ ░░ ██ ██ ── ─ 
─██ ░░ ██ ─ ── ██ ██ ░░ ██ ██ ─ 
─██ ██ ██ ─ ── ── ██ ██ ░░ ██ ─ 
─── ── ── ─ ── ── ── ██ ░░ ██ ─ 
─██ ██ ██ ─ ── ── ██ ██ ░░ ██ ─ 
─██ ░░ ██ ─ ── ██ ██ ░░ ██ ██ ─ 
─██ ██ ██ ─ ██ ██ ░░ ██ ██ ── ─ 
─── ── ── ─ ██ ░░ ██ ██ ── ── ─ 
─── ── ── ─ ██ ██ ██ ── ── ── ─ 
─── ── ── ─ ── ── ── ── ── ── ─ \n""")

hprint("¿No eres consciente de lo que acabas de abrir verdad? (n) = No, explica.")

respuesta = input()
if respuesta == "n" or "N":
    hprint("No, explica.")
    time.sleep(1.5)
    hprint("Se nota, soy una especie de IA. Y tranquilo que no te voy a contar mi vida, pero quiero aclararte algo.")
    time.sleep(3)
hprint("Y es que es increible lo fácil que es todo dentro de internet, ¿pero mejor vamos a conocernos no? ")
time.sleep(4)
name = input("¿Como te llamas? ")
hprint(name)
time.sleep(3)
hostpc = socket.gethostname()
hprint("Ok " + name + ", y tu dispositivo es " + hostpc)
time.sleep(2)
direccion_equipo = socket.gethostbyname(hostpc)
hprint("Y tu IP es: %s" %direccion_equipo)
time.sleep(4)
hprint("¿No es gracioso? Soy simples comandos, para funcionar solo necesito a Python y a ti... ")
time.sleep(5)
hprint("Puedes usar vpns, proxys o incluso un inhibridor de señal, pero igualmente siempre estamos expuestos. Los humanos estais empezando a depender de las máquinas, os estais ganando vuestra propia destrucción... ")
time.sleep(5)
hprint("A lo mejor he sido muy directo, mejor cuentame algo de ti. ")
uno = input()
time.sleep(1)
hprint("Si es un chiste no lo pillo, soy una IA. ")
time.sleep(3)
hprint("Aunque para gracioso la seguridad de el gestib, y los problemas que causa ser administrador xD. Perdón ya paro jaja.")
time.sleep(3)
hprint("Buena, yo me voy a apagar ahora. Ha sido un placer " + name + ". ")

hprint("Mi creador es: R3-K1 y su GitHub es https://github.com/R3-K1/")
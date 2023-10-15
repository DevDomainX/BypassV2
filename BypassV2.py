#!/usr/bin/env python3 
from random import randint
from time import sleep
import os
import sys
from colorama import init, Fore, Style, Back
init()
title = Fore.LIGHTRED_EX+Style.BRIGHT+"""_Script Whattsap_ V2 Bypass Code

    Nota: este script esta hecho para mero projecto de programacion

    Descargo: No me hago responsable del mal uso del script 'BypassV2 Code'

    ;> Post data : Hans Saldias
\n\n"""

 
def Bypass(number):
    """Del numero ingresado se extrae el codigo de verificacion del la apk de whatsapp
    retornando toda la informacion posible 

    Args:
        number (_int_): _Ingreso de numero telefonico del usuario_
        str (_strings_): _numero que tome cualquier caracter en este caso +
    """
    os.system("clear")
    for i in title:
        print(i, end="", flush=True)
        sleep(0.1)
    sleep(3)
    code = randint(111111, 999999)
    print("[#] Inicialite number {}\n\n".format(number))
    sleep(3)
    print("[!] Verify number insert {}\n\n".format(number))
    sleep(3)
    print('[#] Waiting response data number {}\n\n'.format(number))
    sleep(3)
    if "+569" in number:
        print('[!] Location number {} is CHILE\n\n'.format(number))
        sleep(3)
    if '+1' in number:
        print('[!] Location number {} is CANADA\n\n'.format(number))
        sleep(3)
    if '+1' in number:
        print('[!] Location number {} is ESTADOS UNIDOS\n\n'.format(number))
        sleep(3)
    if '+52' in number:
        print('[!] Location number {} is MEXICO\n\n'.format(number))
        sleep(3)
    if '+51' in number:
        print('[!] Location number {} is PERU\n\n'.format(number))
        sleep(3)
    if "+54" in number:
        print('[!] Location number {} is ARGENTINA\n\n'.format(number))
        sleep(3)
    if '+55' in number:
        print('[!] Location number {} is BRAZIL\n\n'.format(number))
        sleep(3)
    if '+57' in number:
        print('[!] Location number {} is COLOMBIA\n\n'.format(number))
        sleep(3)
    if '+58' in number:
        print('[!] Location number {} is VENEZUELA\n\n'.format(number))
        sleep(3)
    if '+591' in number:
        print('[!] Location number {} is BOLIVIA\n\n'.format(number))
        sleep(3)
    

    cont = number.count(number[0:0])
    print('[#] Number number {} has {} characters\n\n'.format(number, cont))
    sleep(3)
    print('[#] Brute Force number {} Waiting..\n\n'.format(number))
    sleep(3)
    print("!!!! Your Code Verify in process ... \n\n")
    sleep(3)
    print('[!!] {} is Ready ....\n\n'.format(number))
    sleep(3)
    print('[*] Code Bypass is {}\n\n'.format(code))
    sleep(3)
    print('[ >_< ] Thanks for using my tool \n\n')
    sleep(3)
    Create = "Created: Hans saldias\n\n"
    tools = "BypassV2\n\n"
    for i in Create:
        print(i, end="*", flush=True)
        sleep(0.1)
    sleep(3)
    for i in tools:
        print(i, end="*", flush=True)
        sleep(0.1)
    sleep(3)
    


number = input(Fore.LIGHTGREEN_EX+'insert a number: ')
sleep(3)

Bypass(number)
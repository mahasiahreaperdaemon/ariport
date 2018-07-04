#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import sys

print("#=#=#=#=#=#=#=#=#")
print("     ARIPORT     ")
print("#=#=#=#=#=#=#=#=#")
print("Criado por: Astaroth Ariel")
print("--------------------------")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alvo = sys.argv[1]
if alvo == "-h":
    print("MODO DE USAR")
    print("python3 ariport.py [alvo]")
    print("python3 ariport.py google.com.br")
    print("python3 ariport.py 192.168.2.1")
else:
    print("Escaneando por portas abertas...")
    print("--------------------------------")
    for porta in range(0, 65536):
        if s.connect_ex((alvo, porta)) == 0:
            print("[{}]ABERTA".format(porta))





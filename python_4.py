# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 10:09:30 2023

@author: User
"""

menu = {
        "Osh":20 000, 
        "Kaboa":15 000,
        "Somsa":30 000,
        "Jiz":90 000
        }
print("3 ta taom buyurtma bering.")
buyurtmalar = []

for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom: ").lower())
    
for buyurtma in buyurtmalar:
    if buyurtma in menu: 
        print("f{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")
    
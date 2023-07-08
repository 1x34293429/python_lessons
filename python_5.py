# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:34:45 2023

@author: User
"""

shaxs1 = {
    "ism":"Abu Abdulloh Muhammad Ibn Ismoil",
    "t_yil":"810-yil",
    "t_joy":"Buxoro",
    "yosh":"60 yil"
    }
shaxs2 = {
    "ism":"Abdulla Qodiriy",
    "t_yil":"1894-yil",
    "t_joy":"Toshkent",
    "yosh":"44 yil"
    }
shaxs3 = {
    "ism":"Erkin Vohidov",
          "t_yil":"1936-yil",
          "t_joy":"Farg'ona",
          "yosh":"80 yil"
    }
shaxs4 = {
    "ism":"Alisher Navoiy",
    "t_yil":"1441-yil",
    "t_joy":"Xirot",
    "yosh":"60 yil"
    }
shaxslar = [shaxs1, shaxs2, shaxs3, shaxs4]
for shaxs in shaxslar:
    print(f"{shaxs['ism']}, {shaxs['t_yil']}, {shaxs['t_joy']}da tug'ilgan, {shaxs['yosh' ] } umr ko'rgan  ")

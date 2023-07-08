# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 18:47:29 2023

@author: User
"""

davlatlar = {
    "O'zbekiston":{"Poytaxti":"Toshkent",
                   "Hududi":"448978 kv.km",
                   "Aholisi":"37000000",
                   "Pul birligi":"so'm"
                   },
    "Rossiya":{"Poytaxti":"Moskva",
                   "Hududi":"17098246 kv.km",
                   "Aholisi":"144000000",
                   "Pul birligi":"rubl"
                   },
    "AQSH":{"Poytaxti":"Vashington",
                   "Hududi":"9631418 kv.km",
                   "Aholisi":"327000",
                   "Pul birligi":"dollar"
                   },
    "Malayziya":{"Poytaxti":"Kuala-Lumpur",
                   "Hududi":"329750 kv.km",
                   "Aholisi":"250000000",
                   "Pul birligi":"rinngit"}
        }
davlat=input("Davlat nomini kiriting: ")
if davlat in davlatlar:
    info=davlatlar[davlat]
    print(f"\n{davlat}ning poytaxti: {info['Poytaxti']} shahri,\n Hududi: {info['Hududi']},\n Aholisi: {info['Aholisi']},\n Pul birligi: {info['Pul birligi']}")
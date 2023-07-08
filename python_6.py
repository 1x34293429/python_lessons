# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 21:39:03 2023

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
for davlat, info in davlatlar.items():
    print(f"\n{davlat}ning poytaxti: {info['Poytaxti']} shahri,\n Hududi: {info['Hududi']},\n Aholisi: {info['Aholisi']},\n Pul birligi: {info['Pul birligi']}")
  
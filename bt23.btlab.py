# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:57:24 2024

@author:  Phan Le Quynh 23720041  
"""

import math
a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
c = float(input("Nhap c:"))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Phuong trinh vo nghiem!")
elif delta == 0:
     x = -b/ (2*a)
     print("Phuong trinh co nghiem kep x: ", -b/(2*a))
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("Phuong trinh co 2 nghiem phan biet x1= ", (-b+math.sqrt(delta)/(2*a)))
    print("Phuong trinh co 2 nghiem phan biet x2= ", (-b-math.sqrt(delta)/(2*a)))

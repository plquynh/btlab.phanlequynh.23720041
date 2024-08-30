# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:27:32 2024

@author: Phan Le Quynh 23720041
"""
a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))
c = int(input("Nhap so c:"))
d = int(input("Nhap so d:"))
min_value = a
if b < min_value:
    min_value = b
if c < min_value:
    min_value = c
if d < min_value:
    min_value = d
print("so nho nhat la:", min_value)
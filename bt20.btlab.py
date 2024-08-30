# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:37:07 2024

@author:  Phan Le Quynh 23720041 
"""
a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))
c = int(input("Nhap so c:"))
max_value = a
if b > max_value:
    max_value = b
if c > max_value:
    max_value = c
print("so lon nhat la:", max_value)

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:53:00 2024

@author:  Phan Le Quynh 23720041
"""

a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
if a == 0 and b == 0:
    print("Phuong trinh co vo so nghiem.")
elif a == 0 and b != 0:
    print("Phuong trinh vo nghiem.")
elif a != 0 and b != 0:
    print("Phuong trinh co mot nghiem duy nhat X=", -b/a)
else:
    print("Khong hop le!")
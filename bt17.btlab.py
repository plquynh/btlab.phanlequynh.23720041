# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:33:27 2024

@author: phan le quynh 23720041
"""

a = int(input("Nhap so thu nhat:"))
b = int(input("Nhap so thu hai:"))
c = int(input("Nhap so thu ba:"))
so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)
print("so lon nhat la:",so_lon_nhat)
print("so nho nhat la:",so_nho_nhat)
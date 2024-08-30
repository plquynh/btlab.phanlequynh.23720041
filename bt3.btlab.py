# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:32:48 2024

@author: Phan Le Quynh 23720041 
"""

N = int(input("Nhap so nguyen duong N co 2 chu so:"))
chu_so_hang_chuc = N // 10
chu_so_hang_don_vi = N % 10
tong = chu_so_hang_chuc + chu_so_hang_don_vi
print("Tong cac chu so cua N la:",tong)
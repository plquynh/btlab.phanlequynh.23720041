# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:23:58 2024

@author: Phan Le Quynh 23720041
"""

soxe = input("Nhap vao so xe cua ban: ")
tong = sum(int(chuso) for (chuso) in (soxe))
hang_chuc = tong//10
hang_don_vi = tong%10
so_nut=hang_chuc + hang_don_vi
print("Số nút của xe đó là:", so_nut)
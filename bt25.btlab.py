# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:10:11 2024

@author: Phan Le Quynh 23720041 
"""
ky_tu = input("Nhap mot ky tu: ")
if ky_tu.islower():
  ky_tu_moi = ky_tu.upper()
else:
    ky_tu_moi = ky_tu.lower()
print("ky tu sau khi chuyen doi:", ky_tu_moi)
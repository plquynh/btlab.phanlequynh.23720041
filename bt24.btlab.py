# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:00:14 2024

@author: Phan Le Quynh 23720041   
"""
gio = int(input("Nhap gio:"))
phut = int(input("Nhap phut:"))
giay = int(input("Nhap giay:"))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("gio, phut, giay hop le.")
else:
    print("gio, phut, giay khong hop le.")
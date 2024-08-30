# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:19:33 2024

@author: phan le quynh 23720041
"""

a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
bt1 = a+b
bt2 = a**(1/3)+b**(1/3)
bt3 = (a*b)**(1/3)
bt4 = (a**(1/3)-b**(1/3))**2
ketqua = ((bt1/bt2)-bt3)/bt4 
print("Ket qua cua bieu thuc la:",ketqua)
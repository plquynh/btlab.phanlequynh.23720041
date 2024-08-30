# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:43:51 2024

@author: phan le quynh 23720041
"""

import datetime
ngay = int(input("nhap ngay:"))
thang = int(input("Nhap thang:"))
nam = int(input("Nhap nam:"))
ngay_sinh = datetime.date(nam, thang, ngay)
print("a) Ngay/thang/nam:",
      ngay_sinh.strftime("%d/%m/%y"))
print("b) Ngay/thang/nam:",
      ngay_sinh.strftime("%d/%m/%y"))
print("c) Nam/thang/ngay:",
      ngay_sinh.strftime("%y/%m/%d"))

      
      
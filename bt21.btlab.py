# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:42:52 2024

@author: Phan Le Quynh 23720041  
"""
number = int(input("Nhap mot so:"))
number_words = { 0: "khong",
                 1: "mot",
                 2: "hai",
                 3: "ba",
                 4: "bon",
                 5: "nam",
                 6: "sau",
                 7: "bay",
                 8: "tam",
                 9: "chin",}
if 0 <= number <= 9:
    print(number_words[number])
else:
    print("khong doc duoc")
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:23:37 2021

@author: hthuang
"""

def is_float(a):
    try:
        float(a)
    except ValueError:
        try:
            complex(a)
        except ValueError:
            return False
    return True
                
    
def add(a):
    x = a
    b = True
    while is_float(a):
        a = float(a)
        x = (x + a)
        a = input()
    else:
        print(x)
        

def average():
    x = input()
    x1 = x.split(",")
    xnew =  [int(i) for i in x1]
    c = sum(xnew)
    print(c/len(xnew))
    

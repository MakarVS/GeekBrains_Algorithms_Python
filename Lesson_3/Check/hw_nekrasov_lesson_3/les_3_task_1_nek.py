# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:18:15 2020

@author: Nekad
"""
# =============================================================================
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.
# =============================================================================

Max_num = 99
Min = 2
Max = 9

for i in range(Min, Max+1):
    print(f' Числу {i} кратно {Max_num // i} чисел в диапазоне натуральных чисел от 2 до 99')
    
    
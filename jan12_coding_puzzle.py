# -*- coding: utf-8 -*-
"""jan12_coding_puzzle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/198DYrBwd8It8MMnX7xkEOO7YVMj2E25J
"""

# @author: Tashi Tsering Gurung
# @email: hseb.tashi@gmail.com
# @date: 1/12/2021

def sum_of_integers(num):
  """to find the sum from 0 to n"""
  if type(num) != int:
    print("wrong input ... BYE!")
    return
  sum = 0
  for add in range(1,num+1):
    print(f' adding {sum} and {add}')
    sum += add
    print(sum)
    print('=============')
  return sum

a = 4
a_str = 'four'
sum_of_integers(a)

sum_of_integers(a_str)

# Alternative Solution

# User Input

def sum_of_integers():
  """to find the sum from 0 to n"""
  try:
    num =input()
    int_num = int(num)
  except:
    print('wrong input ... Bye !!')
    return
  sum = 0
  for add in range(1,int_num + 1):
    print(f' adding {sum} and {add}')
    sum += add
    print(sum)
    print('=============')
  return sum

sum_of_integers()
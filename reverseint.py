#!/usr/bin/python
import sys
import math

def reverseint(num):
   a = str(num)
   lst = list(a)
   ans = 0
   for x in reversed(lst):
      ans = int(x) + ans * 10
      print('ans:%s' %(x))
   print('ANS:%d' %(ans))

def main():
   x = input("Input number:")
   print ('x:%d' %(x))
   reverseint(x)

if __name__=='__main__':
   main()

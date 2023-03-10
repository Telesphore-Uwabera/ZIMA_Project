#!/usr/bin/python3
temp= int(input("Enter the region's temperature: "))
if 0<temp<17:
  print("cold")
elif 17<=temp<25:
  print("medium")
elif 25<=temp<100:
  print("hot")

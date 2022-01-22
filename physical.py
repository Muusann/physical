# -*- coding: utf-8 -*-

#検定基準（24歳以下）

#腕立ての関数
def push(push_count):
  if push_count >= 30 and push_count <= 54:
    return  2
  elif push_count >= 55 and push_count <= 70:
    return  3
  elif push_count >= 71 and push_count <= 99:
    return  4
  elif push_count >= 89:
    return  5
  else:
    return  0

#腹筋の関数
def abdo(abdo_count):
  if abdo_count >= 35 and abdo_count <= 50:
    return  2
  elif abdo_count >= 51 and abdo_count <= 70:
    return  3
  elif abdo_count >= 71 and abdo_count <= 90:
    return  4
  elif abdo_count >= 91:
    return  5
  else:
    return  0

#3000m走
  
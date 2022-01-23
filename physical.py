# -*- coding: utf-8 -*-

#年齢別基準の作成
class PhysTest:
  #腕立ての関数(24歳以下)
  def push(self,push_count):
    if push_count >= 82 and push_count <= 55:
      return  2
    elif push_count >= 56 and push_count <= 61:
      return  3
    elif push_count >= 72 and push_count <= 81:
      return  
    elif push_count >= 82:
      return  
    else:
      return  0

  #腹筋の関数(24歳以下)
  def abdo(self,abdo_count):
    if abdo_count >= 58 and abdo_count <= 63:
      return  2
    elif abdo_count >= 64 and abdo_count <= 71:
      return  3
    elif abdo_count >= 72 and abdo_count <= 79:
      return  4
    elif abdo_count >= 80:
      return  5
    else:
      return  0

  #腕立ての関数(25歳以上30歳未満)
  def push2(self,push_count):
    if push_count >= 24 and push_count <= 44:
      return  2
    elif push_count >= 45 and push_count <= 65:
      return  3
    elif push_count >= 66 and push_count <= 80:
      return  4
    elif push_count >= 85:
      return  5
    else:
      return  0

#腹筋の関数(25歳以上30歳未満)
  def abdo2(self,abdo_count):
    if abdo_count >= 20 and abdo_count <= 44:
      return 2
    elif abdo_count >= 45 and abdo_count <= 64:
      return  3
    elif abdo_count >= 65 and abdo_count <= 79:
      return  4
    elif abdo_count >= 80:
      return  5
    else:
      return  0



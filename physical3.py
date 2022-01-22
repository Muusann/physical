#検定基準（30歳以上40歳未満）




#腕立ての関数
def push(push_count):
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
  

#腹筋の関数
def abdo(abdo_count):
  if abdo_count >= 20 and abdo_count <= 44:
    return  2
  elif abdo_count >= 45 and abdo_count <= 64:
    return  3
  elif abdo_count >= 65 and abdo_count <= 79:
    return  4
  elif abdo_count >= 80:
    return  5
  else:
    return  0

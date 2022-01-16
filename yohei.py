# -*- coding: utf-8 -*-
import physical

print("あなたの体力を測定します。")
name = input("名前を入力してください")

p_count = int(input("腕立て伏せの記録を入力してください。"))
if p_count < 0:
  print("正しい数値を入力してください")
  exit()

a_count = int(input("腹筋の記録を入力してください。"))
if a_count < 0:
  print("正しい数値を入力してください")
  exit()


p_result = physical.push(p_count)
a_result = physical.abdo(a_count)

result = p_result + a_result

#検定結果表示
if result >= 9:
  print(name + "さんあなたの結果は1級です")
elif result <= 8 and result >= 4:
  print(name + "さんあなたの結果は2級です")
elif result <= 3 and result >= 2 :
  print(name + "さんあなたの結果は3級です")
else:
  print(name + "さんあなたの結果は級外です")




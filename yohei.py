# -*- coding: utf-8 -*-
from physical import PhysTest

print("あなたの体力を測定します。")
name = input("名前を入力してください")
age = int(input("あなたの年齢を入力してください"))

p_count = int(input("腕立て伏せの記録を入力してください。"))
if p_count < 0:
  print("正しい数値を入力してください")
  exit()

a_count = int(input("腹筋の記録を入力してください。"))
if a_count < 0:
  print("正しい数値を入力してください")
  exit()

physical_test1 = PhysTest()
physical_test2 = PhysTest()


if age <= 24:
  p_result = physical_test1.push(p_count)
  a_result = physical_test1.abdo(a_count)
elif age >= 25 and age < 30:
  p_result = physical_test2.push2(p_count)
  a_result = physical_test2.abdo2(a_count)


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



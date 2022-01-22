# -*- coding: utf-8 -*-
from physical import PhysTest

print("あなたの体力を測定します。")

#基本情報の入力
name = input("名前を入力してください")
while name == "":
  name = input("名前が未入力です。名前を入力してください。")
  if name != "":
    continue
  
age = input("あなたの年齢を入力してください")
while age == "":
  age = input("年齢が未入力です。年齢を入力してください。")
  if age != "":
    age = int(age)
    continue
age = int(age)

#記録の入力
p_count = int(input("腕立て伏せの記録を入力してください。"))
while p_count < 0:
  p_count = int(input("正しい数値を入力してください。"))
  if p_count >= 0:
    continue

a_count = int(input("腹筋の記録を入力してください。"))
while a_count < 0:
  a_count = int(input("正しい数値を入力してください。"))
  if a_count >= 0:
    continue

#年齢基準のインスタンス生成
physical_test1 = PhysTest()
physical_test2 = PhysTest()

#年齢別による条件分岐
if age <= 24:
  p_result = physical_test1.push(p_count)
  a_result = physical_test1.abdo(a_count)
elif age >= 25 and age < 30:
  p_result = physical_test2.push2(p_count)
  a_result = physical_test2.abdo2(a_count)

#検定結果代入
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



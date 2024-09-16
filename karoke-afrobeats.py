print("PITCH PERFECT- LYRICS NAME")
print("Fill in the blank lyrics!")
print()
attempts_1 = 0
while True:
  print("It's lonley at the top.__________ ")
  lyric =input("What is the missing lyric ?")
  attempts_1 += 1
  if lyric.lower() == "lonley, lonley, lonley":
    print("That is correct")
    print(f"It took you {attempts_1} attempts.")
    break
  else:
    print(" upsiee, try again")
  print()
attempts_2 = 0
while True:
  print("Money on my mind.__________")
  lyric =input("What is the missing lyric ?")
  attempts_2 += 1
  if lyric.lower() == "money, money, money":
    print("That is correct")
    print(f"It took you {attempts_2} attempts.")
    break
  else:
    print(" upsiee, try again")
  print()
attempts_3 = 0
while True:
  print("Love me Jeje, love me _____")
  lyric =input("What is the missing lyric ?")
  attempts_3 += 1
  if lyric.lower() == "tender":
    print("That is correct")
    print(f"It took you {attempts_3} attempts.")
    break
  else:
    print( " upsiee, try again")


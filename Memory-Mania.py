from random import randint
import time
print("Welcome to Memory Mania!\nEnter the length of the string you would like to create.\nYou will have 30 seconds to memorize a string 5 or less digits\nYou will have 1 minute to memorize a string between 6 and 10 digits\nYou will have 2 minutes to memorize a string greater than 10 digits\nGood luck!\n\n")
def game():
  count = int(input("\nLength of string?\n >"))
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  start = 10 ** (count - 1)
  end = (10 ** count) - 1
  string = (randint(start, end))
  if count <= 5:
    print(string)
    print("\nYou have 30 seconds, GO!")
    time.sleep(30)
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    answer = int(input("What was the number?\n >"))
    if answer == string:
      print("Nice Job!")
      time.sleep(2)
      game()
    if answer != string:
      print("\nINCORRECT\n\n", string)
      time.sleep(2)
      game()
  if count <= 10:
    print(string)
    print("\nYou have 60 seconds, GO!")
    time.sleep(60)
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    answer = int(input("What was the number?\n >"))
    if answer == string:
      print("Nice Job!")
      time.sleep(2)
      game()
    if answer != string:
      print("\nINCORRECT\n\n", string)
      time.sleep(2)
      game()
  if count >= 11:
    print(string)
    print("\nYou have 120 seconds, GO!")
    time.sleep(120)
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    answer = int(input("What was the number?\n >"))
    if answer == string:
      print("Nice Job!")
      time.sleep(2)
      game()
    if answer != string:
      print("\nINCORRECT\n\n", string)
      time.sleep(2)
      game()
game()
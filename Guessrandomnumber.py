import random
num=random.randint(1,10)
tries=0
while True:
  guess=int(input("Please guess the number from 1 to 100:"))
  if num==guess:
    tries+=1
    print("you selected correct number in ",tries)
  elif num<guess:
    tries+=1
    print("number is lower")
  elif num>guess:
    tries+=1
    print("number is greater")
  else:
    tries+=1
    print("sorry you are wrong")


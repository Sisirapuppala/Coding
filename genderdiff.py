N= input("Please enter your name: ")
G= input("Please enter your gender:")

if(G == 'M' or G =='m' or G =='Male' or G =='male'):
  print(f"Good morning {N} sir")
elif (G == 'F' or G =='f' or G =='Female' or G =='female'):
  print(f"Good morning {N} Madam")
else:
  print(f"Good morning {N}, unidentified gender")

#OUTPUT:
#Please enter your name: Sisira
#Please enter your gender:Female
#Good morning Sisira Madam

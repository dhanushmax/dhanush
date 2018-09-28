#write a program to play snake and lader game
count=0
import random
while(count<=100):
	n=input("enter r to roll the dice")
	if(n=='r'):
		a=random.randint(1,6)
		count=count+a
		print("my positon",count)
		print("the random value",a)

		if(count==11):
			count=2
			print("sry snake has bitten")
		elif(count==8):
			count=37
			print("climb the ladder pos=37")
		elif(count==13):
			cout=34
			print("climb the ladder pos")
		elif(count==38):
			count=9
			print("sry snake has bitten")
		elif(count==40):
			count=68
			print("climb the ladder")
		elif(count==65):
			count=46
			print("sry snake has bitten")
		elif(count==52):
			count=81
			print("climb the ladder")
		elif(count==76):
			count=97
			print("cilmb the ladder")
		elif(count==89):
		    count=70
		    print("sry snake has bitten")
		elif(count==93):
			count=64
			print("sry snake has bitten")
		elif(count==100):
			print("congrats u won the game")
		elif(count>100):
			count=100
			print("congrts u won the game")



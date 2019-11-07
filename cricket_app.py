#This code is to simulate a game called HAND CRICKET played by children in school days ( a great childhood memory ). 
#In this game user can give a user diffined number of over he wants to play, and also the number of players he wants to play with.
#In this game user is supposed to call for toss either heads or tails and the computer will do the coin flip. 
#For batting or bowling user has to select a number between 1 to 6 , so will the computer by using RANDOM function, 
#	to generate a random number between 1 to 6. 
#	If the user gives any number other than 1 to 6 the score will not be counted but as a penalty the ball will be counted.

#In case the number selected by the user and computer match, the player (user or computer) will loose their batting chance 
#	and the next player will walk in, ones all the players from the batting team are eliminated or the specified overs are finnished 
#	batting is shifted to the opponent team to reach the target.
#	the batting and bowling functions are defined in a module named by "cricket_app_module.py".

#Since, I had kept a test cricket match in mind even if the second player reaches the required target, 
#	he will be allowed to continue batting till the complete over is finished or player gets out.
#	After both the teams are done batting the scores that where stored in a list are used to calculate the total score.
#	Finally, both the scores are compared with each other, and a winner is selected, or a draw match is declared.

#To enjoy the game the code comes with music option which will be played in the banground. 
#	The song will be selected by the computer on a random basis from the list of songs that are listed in its directry.
#	This code comes with two musics to be played. In order to play music you need to have "pygame" library files.
#	Make sure to keep all the songs in '.ogg' formate. 'pygame' supports this formate without any problem, '.mp3','.waw' might show few problems to play.
#	Link to downlode the songs: " https://drive.google.com/drive/folders/1V5aXEZZr9xJteqIsHlX8hjD2mHMSRrll?usp=sharing " -drive_link
#	Link generate .ogg formate: "https://audio.online-convert.com/convert-to-ogg" - online-convert.com 

#Make sure to keep "cricket_app.py","cricket_app_module.py",all the listed songs in a single directry.

#HAPPY PLAYING.
#created by SATHWIK S 

import random
import cricket_app_module
from pygame import *

final_user_s=0
final_comp_s=0
user_s=0
comp_s=0
finished_ball=0

song=random.choice(['1.ogg','2.ogg'])
mixer.init()
mixer.music.load(song)
mixer.music.play(-1)
print()
print("$"*20,"\nWELCOME TO COMMAND CRICKET\n","$"*20)


overs=int(input("Enter the number of overs: "))
balls=overs*6
ball1=balls
wickets=int(input("Enter the nos of players: "))

uplayers=[]
uscore=[]
cplayers=[]
cscore=[]
for i in range(0,wickets):
	uplayers.append(input(f"Enter player{i+1} name: "))
print("\n\nALL THE BEST","\n\t\tfrom Team COMMAND CRICKET\n\n")

coin=[1,2]
action=["bat","bowl"]
c_toss=random.choice(coin)
#print(c_toss)
#user toss choice
print("Call for toss\n heads--> 1\n tails--> 2")
while True:
	u_toss=int((input("-->")))
	if (u_toss==1 and c_toss==1) or (u_toss==2 and c_toss==2):
		print("You won the toss\nChoose to bat or bowl")
		action_choice_u=int(input("bat:1\nball:2\n-->"))
		
		if action_choice_u==1:
			print("You choose to bat\n")
			for i in range(0,wickets):
				print(f"Batting by {uplayers[i]}")
				user_s,finished_ball=cricket_app_module.u_batting(balls)
				balls-=finished_ball
				uscore.append(user_s)
				final_user_s+=uscore[i]

			print("*"*5,f"\nTARGET: {final_user_s+1}\n","*"*5)

			for i in range(0,wickets):
				print(f"Batting by computer{i+1}")
				comp_s,finished_ball=cricket_app_module.u_bowling(ball1)
				ball1-=finished_ball
				cscore.append(comp_s)
				final_comp_s+=cscore[i]

			break
		
		elif action_choice_u==2:
			print("You choose to bowl\n")
			for i in range(0,wickets):
				print(f"Batting by computer{i+1}")
				comp_s,finished_ball=cricket_app_module.u_bowling(ball1)
				ball1-=finished_ball
				cscore.append(comp_s)
				final_comp_s+=cscore[i]

			print("*"*5,f"\nTARGET: {final_comp_s+1}\n","*"*5)

			for i in range(0,wickets):
				print(f"Batting by {uplayers[i]}")
				user_s,finished_ball=cricket_app_module.u_batting(balls)
				balls-=finished_ball
				uscore.append(user_s)
				final_user_s+=uscore[i]

			break
		
		elif action_choice_u!=1 or action_choice_u!=2:
			print("Invalid i/p")
			continue


	elif (u_toss==1 and c_toss==2) or (u_toss==2 and c_toss==1):
		print("Computer won the toss")
		action_choice_c=random.choice(action)
		
		if action_choice_c=="bat":
			print("Computer choose to bat")
			for i in range(0,wickets):
				print(f"Batting by computer{i+1}")
				print(ball1)
				comp_s,finished_ball=cricket_app_module.u_bowling(ball1)
				ball1-=finished_ball
				cscore.append(comp_s)
				final_comp_s+=cscore[i]

			print("*"*5,f"\nTARGET: {final_comp_s+1}\n","*"*5)

			for i in range(0,wickets):
				print(f"Batting by {uplayers[i]}")
				print(balls)
				user_s,finished_ball=cricket_app_module.u_batting(balls)
				balls-=finished_ball
				uscore.append(user_s)
				final_user_s+=uscore[i]

			break
		
		elif action_choice_c=="bowl":
			print("Computer choose to bowl")
			for i in range(0,wickets):
				print(f"Batting by {uplayers[i]}")
				print(balls)
				user_s,finished_ball=cricket_app_module.u_batting(balls)
				balls-=finished_ball
				uscore.append(user_s)
				final_user_s+=uscore[i]
			
			print("*"*5,f"\nTARGET: {final_user_s+1}\n","*"*5)

			for i in range(0,wickets):
				print(f"Batting by computer{i+1}")
				print(ball1)
				comp_s,finished_ball=cricket_app_module.u_bowling(ball1)
				ball1-=finished_ball
				cscore.append(comp_s)
				final_comp_s+=cscore[i]

			break



	elif u_toss not in coin:
		print("Invalid i/p")
		continue

print("$_"*10,"\nFINAL SCORE BOARD\n","$_"*10)
for i in range(0,wickets):
	print(f"player {i+1}\t",uplayers[i],"\t",uscore[i],f"\tcomputer{i+1}\t",cscore[i])
print(f"Total score\nUSER: {final_user_s}\nCOMPUTER: {final_comp_s}")

print("#"*20)
if final_user_s==final_comp_s:
	print("Match is draw")
elif final_user_s>final_comp_s:
	print("YOU won")
elif final_user_s<final_comp_s:
	print("COMPUTER won")
print("#"*20)

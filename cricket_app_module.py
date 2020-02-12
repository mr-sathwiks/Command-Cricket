#This script will run only as a module with 'cricket_app.py'. Make sure to keep both both the files in a same directry.
#created by SATHWIK S 


import random
run=list(range(1,1000))
cnt=0

def u_batting(balls):
	user_score=0
	fb=0
	print("Start user batting\nStart computer bowling")
	
	for i in range(0,balls):
		
		print("-"*20)

		run_n=random.choice(run)
		cball= run_n%6
		if cball==0:
			cball=6

		ubat=int(input("Enter number 1-6: "))
		print(f"\nComputer choice(comp_bowl): {cball}")
		print(f"User choice(user_bat): {ubat}")
		fb+=1
		if ubat==cball:
			print("\nUser is out\n")
			return user_score,fb
			break
		elif (ubat in run) and ubat!=cball:
			user_score+=ubat
			print(f"Player score: {user_score}")
		print()

	print("End of computer batting\n")
	return user_score,fb


def u_bowling(balls):
	
	comp_score=0
	fb=0
	print("Start computer batting\nStart user bowling")
	for i in range(0,balls):
		
		print("-"*20)

		run_n=random.choice(run)
		cbat= run_n%6
		if cbat==0:
			cbat=6
		

		uball=int(input("Enter number 1-6: "))
		print(f"\nComputer choice(comp_bat): {cbat}")
		print(f"User choice(user_bowl): {uball}")
		fb+=1
		if uball==cbat:
			print("\nComputer is out\n")
			return comp_score,fb
			break
		elif (uball in run) and uball!=cbat:
			comp_score+=cbat
			print(f"Computer score: {comp_score}")
		print()
	
	print("End of computer batting\n")
	return comp_score,fb

import random

def main():
	rolling = True
	while rolling :
		userInput = raw_input("Do you want to Roll your dice? (Y/N)")
		if userInput.lower() == "y" :
			roll = random.randint(1,6)
			print ("you rolled " , roll)
		else :
			rolling = False
			
			
	
	
main();	


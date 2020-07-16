# Coin Flip Simulation
# write some code that simulates flipping a single coin however many times the user decides. 
# The code should record the outcomes and count the number of tails and heads.
import random
# main function that executes codes for toss
def main():
        # user input
	num = int(input("enter the no of flips:"))
	
	heads = 0
	tails = 0
	head_list = []
	tail_list = []
	for i in range(num):
          # flip of coin
		flip = random.randint(0,1)
		if flip == 0:
			print("you got head")
			heads += 1
		else:
			print("you got tail")
			tails += 1
	print("HEADS:",heads)
	print("TAILS:",tails)
# calling a function
main()

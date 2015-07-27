from sys import argv

# script, filename = argv
# txt = open(filename, 'a')
# txt.write('\n\n')

need = 0
hold = 0
limit = 0
check = 0

name = raw_input("Name of the Course: ")
assign = {};
#txt.write(name+"\n")
goal = float(raw_input("What would you like your final grade to be? "))



while limit < 100:
	
	if need == 1:

		new_lim = 100 - limit
		want = goal - hold
		need = (want/new_lim)*100

		if new_lim < want:
			
			print("You will not reach your goal of %s even if you get 100 percent on your final %s\n" % (goal, new_lim))
			
			high = new_lim + hold
			print("The highest mark you can receive is %s" % high)
			
			new_goal = float(raw_input("Enter New Goal: "))
			if new_goal > high:
				check = 1
				while(check == 1):
					new_goal = float(raw_input("Too high, please enter again: "))
					if new_goal <= high:
						check = 0

			goal = new_goal
			
			
		else:
			print("You will need a %.2f percent on your final %s percent in order to get a %s in the course\n" % (need, new_lim, goal))
		
		
		cont = raw_input("Would you like to continue? ")
		if cont == 'no':
			print("You will need a %s percent on your final %s percent in order to get a %s in the course, GOOD LUCK!\n" % (need, new_lim, goal))
			# txt.write("You will need a %s percent on your final %s percent in order to get a %s in the course\n" % (need, new_lim, goal))
			# txt.close
			quit(1)
	
		need == 0		
		
	whats_left = 100 - limit


	school = raw_input("School Assignment: ")
	
	
	grade =  float(raw_input("Please enter grade: "))
	if grade > 100 or grade < 0:
		check = 1
		while(check == 1):
			grade = float(raw_input("I doubt you got that, please enter again: "))
			if grade <= 100 and grade >= 0:
				check = 0

	weight =  float(raw_input("Please enter weight: "))
	if weight > 100 or weight < 0 or weight > whats_left:
		check = 1
		while(check == 1):
			weight = float(raw_input("That weight seems off, please enter again: "))
			if weight <= 100 and weight >= 0 and weight < whats_left:
				check = 0


	assign[school] = grade
	
	#txt.write("Assignment: %s\n Grade: %s\n Weight %s\n\n" % (school,grade, weight))

	limit = limit + weight
	new_grade = (weight*0.01)*grade
	hold = hold + new_grade

	if limit >= 100:
		break

	choice = raw_input("Would you like to check what you need? ")	
	if choice == ("yes") or choice == ("YES") or choice == ("y") or choice == ("Y"):
		need = 1



diff = abs(goal - hold)
print ("Your grade is %.2f percent, which is a %s difference between your goal of %s" % (hold, diff, goal))
print assign


# txt.write("Final Grade: %s\n" % hold)

# txt.write("Your grade is %s percent, which is a %s difference between your goal of %s" % (hold, diff, goal))
# txt.write("\n\n")
# txt.close
quit(1)





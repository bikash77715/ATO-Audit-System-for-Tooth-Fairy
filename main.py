# Auditing system of Australian Taxation Office for Tooth Fairy
#source for Tooth Fairy-ATO case 

#regular expression lib for splitting
import logging
logging.disable(logging.INFO)

logging.basicConfig(level = logging.INFO, format = '%(levelname)s-%(message)s')

# function list:
# symbolLine(symbol) - prints a line of supplied symbol
# printMessage(msg) - prints the supplied message aligning at center
# getSpan() - returns estimated width to cover the printed texts
# genBanner() - prints the welcome message
# printMenu() - prints the menu
# getChoice() - takes and returns users' choice input
# splitLinesToList(lines) - returs list of splited lines
# getLostToothList(lines) - returns the int list of lost teeth from the lines: line list
# getTotalExpenditure() - returns total expenditure
# statistics(lines) - prints the statistics of the supplied lines: line list
# exportDetails() - prints the list of children who have never lost a tooth to a file


### main
from services import *
file = open("addresses.csv", 'r')
lines = file.readlines()
splitted_lines = splitLinesToList(lines)	

genBannar()
printMenu()

while True:
	
	ch = getChoice()
	symbolLine('-')

	if ch == 1:
		statistics(splitted_lines)
		
	elif ch == 2:
		file_name = input(" Enter the name for your file: ")
		status_msg = exportDetails(file_name, splitted_lines)
		printMessage(status_msg)
		
	elif ch == 3:
		# status_msg = displayClaimsByState(splitted_lines)
		# printMessage(status_msg)
		displayClaimsByState(splitted_lines)

	elif ch == 4:
		states = [0,0]
		states[0] = input(' Enter first state:\t')
		states[1] = input(' Enter second state:\t')
		states[0] = states[0].upper()
		states[1] = states[1].upper()

		state_list = getStateList(splitted_lines)
		if states[0] in state_list and states[1] in state_list:
			# status_msg = compare2StatesByAverageToothLost(states, splitted_lines)
			# printMessage(status_msg)
			compare2StatesByAverageToothLost(states, splitted_lines)
		else:
			printMessage(' Wrong state name !!!. \n state options: '+str(state_list))		

	elif ch == 5:
		print(" Program terminated as per user request.")
		symbolLine('*')
		exit()

	while True:
		choice = input(' Wish to choose another option? (y/n): ')
		symbolLine('-')
		if choice.upper() =='N':
			print(" Program Terminated.")
			symbolLine('*')
			exit()
		elif choice.upper() == 'Y':
			break
		else:
			print("!!!Please enter correct input!!!")
			symbolLine('-')


#closing data file	
file.close()

import logging
import re, logging, matplotlib.pyplot as pyplt

logging.disable(logging.INFO)

logging.basicConfig(level = logging.INFO, format = '%(levelname)s-%(message)s')

orgn = "Australian Tax Office (ATO)"
case = "Audit case: Tooth Fairy"
dev_name = "Developer: BIKASH SHRESTHA"
std_id = "Student Id: 30377519"

# determining the length of header
span = len(orgn) if len(orgn)>len(case) else len(case)
span = len(dev_name) if span<len(dev_name) else span 
span = len(std_id) if span<len(std_id) else  span 
	
span=int(5*span/2)

def symbolLine(symbol):
	print(symbol*span)

def printMessage(msg):
	print(msg.center(span))
	symbolLine('-')


def genBannar():

	symbolLine('*')

	print(orgn.center(span))
	print(case.center(span))
	print(dev_name.center(span))
	print(std_id.center(span))

	symbolLine('*')

def printMenu():
	print(" 1. Show statistics.")
	print(" 2. Export childrens details who haven't lost any tooth.")
	print(" 3. Display number of claims per State.")
	print(" 4. Compare 2 States.")
	print(" 5. Exit.")
	

def getChoice():
	symbolLine('-')
	while True:
		ch =input(" Enter your choice - (choice options: 1-5):\t ")
		if not ch.isdigit():
			printMessage("!!! Invalid Input !!! \n input range: "+str(list(range(1,6))))
			break
		elif int(ch) not in range(1,6):
			printMessage("!!! Invalid Input !!! \n input range: "+str(list(range(1,6))))
			break
		return int(ch)

def splitLinesToList(lines):
	splitted_lines = []
	for line in lines[:-1]:
		line = line[:-1]
		line_list = re.split(',', line)
		# print (line_list[6])
		splitted_lines.append(line_list)	

	return splitted_lines
	
def getLostToothList(splitted_lines):
	lost_teeth_list = []
	for line in splitted_lines[1:]:
		logging.info(' claims: '+str(line[6]))
		lost_teeth_list.append(int(line[6]))	
			
	# print("Line count is: ", len(lines))
	return lost_teeth_list

def getTotalExpenditure(lost_teeth_list):
	expenditure = 0.0

	for number in lost_teeth_list:
		if number == 0:
			continue

		elif number == 1:
			expenditure += 1

		else:
			expenditure +=0.5

	return expenditure


#prints statistics
def statistics(splitted_lines):

	total_children = len(splitted_lines)-1
	#total childrens
	print(" Total number of children : {}".format(total_children))	

	lost_teeth_list = getLostToothList(splitted_lines)
	#average claims over the years
	print(" Average number of tooth claims over the years: {}".format(float(sum(lost_teeth_list))/total_children))

	print(" Number of children who have never lost a tooth: {}".format(lost_teeth_list.count(0)))

	print(" Number of children who have lost all of their baby teeth: {}".format(lost_teeth_list.count(20)))

	print(" Total expenditure of this year: ${}".format(getTotalExpenditure(lost_teeth_list)))

	symbolLine('-')

def getNoLostList(splitted_lines):
	noLostList = []
	# print(lines[1:])
	for line in splitted_lines[1:]:
		if int(line[6]) == 0:
			noLostList.append(line)

	return noLostList

# exports list of children who haven't lost any teeth
def exportDetails(file_name, splitted_lines):
	noLostList = getNoLostList(splitted_lines)
	
	saveFile = open(file_name, 'w')
	saveFile.write(splitted_lines[0][0] + '\t' + splitted_lines[0][1] + '\t\t' + splitted_lines[0][2] + '\t\t\t' + splitted_lines[0][3] + '\t\t\t\t' + splitted_lines[0][4] + '\t\t' + splitted_lines[0][5] + '\t' + splitted_lines[0][6])
	for line in noLostList:
		saveFile.write(line[0] + '\t\t' + line[1] + '\t\t' + line[2] + '\t\t\t' + line[3] + '\t\t\t' + line[4] + '\t\t' + line[5] + '\t\t' + line[6])
	saveFile.close()
	return " !!! Data Export Successfulv !!!"
	symbolLine('-')

def getStateList(splitted_lines):
	logging.info(' Invoked: getClaimsByState()')

	state_list = []
	for line in splitted_lines[1:]:
		if line[4] not in state_list:
			state_list.append(line[4])
			logging.info('	added '+str(line[4])+' to state list.')

	logging.info(' state_list = '+ str(state_list))
	return state_list
def genZeroValList(list):
	gen_list = []
	for i in list:
		gen_list.append(0)

	return gen_list

def getClaimsByState(splitted_lines):
	logging.info(' Invoked: getClaimsByState()')
	state_list = getStateList(splitted_lines)
	claims_list= genZeroValList(state_list)
	logging.info(' no of state = '+ str(len(state_list)))
	
	for line in splitted_lines[1:]:
		for i in range(len(state_list)):
			if line[4] == state_list[i]:
				claims_list[i]+= 1

	logging.info(' claims_list : '+ str(claims_list))

	return claims_list 

def displayClaimsByState(splitted_lines):
	state_list = getStateList(splitted_lines)
	claims_list = getClaimsByState(splitted_lines)

	pyplt.bar(state_list, claims_list)
	pyplt.xlabel('States')
	pyplt.ylabel('Claims')
	pyplt.title(' Total tooth claims per state')

	pyplt.show()
	# pyplt.savefig('claims_per_states.png')
	symbolLine('-')	
	# return " claims list saved as claims_per_states.png in the directory of the main program."

def sumLostToothByState(states, splitted_lines):
	lost_tooth_sums = [0,0]

	logging.info(' Invoked sum function for lost tooth per state.')
	logging.info(' recieved states:'+ str(states))
	for line in splitted_lines[1:]:		
		if line[4] == states[0].upper():
			lost_tooth_sums[0] += int(line[6])
			logging.info(' lost_tooth_sum[0] = '+ str(lost_tooth_sums[0]))

		elif line[4] == states[1].upper():
			lost_tooth_sums[1] += int(line[6])
			logging.info(' lost_tooth_sum[1] = '+ str(lost_tooth_sums[1]))
		else: 
			continue
	logging.info(' lost_tooth_sums: '+ str(lost_tooth_sums))
	return lost_tooth_sums

def getAverageToothLostList(states, splitted_lines):
	# state_list, claims_list = displayClaimsByState()
	lost_tooth_sums = sumLostToothByState(states, splitted_lines)
	state_list = getStateList(splitted_lines)
	claims_list = getClaimsByState(splitted_lines)

	average_tooth_lost_list = [0,0]

	
	for i in range(len(state_list)):
		if state_list[i] == str(states[0]).upper():
			average_tooth_lost_list[0] = lost_tooth_sums[0]/claims_list[i]
			logging.info(' In getAverageToothLostList() average_tooth_lost_list[0]: '+ str(average_tooth_lost_list[0]))


		elif state_list[i] == str(states[1]).upper():
			average_tooth_lost_list[1] = lost_tooth_sums[1]/claims_list[i]
			logging.info(' In getAverageToothLostList() average_tooth_lost_list[1]: '+ str(average_tooth_lost_list[1]))

		else:
			continue
	return average_tooth_lost_list


def compare2StatesByAverageToothLost(states, splitted_lines):

	logging.info(' In compare2StatesByAverageToothLost() states: '+ str(states))
	average_tooth_lost_list = getAverageToothLostList(states, splitted_lines)	

	pyplt.bar(states, average_tooth_lost_list)
	pyplt.xlabel('States')
	pyplt.ylabel('Average tooth lost')
	pyplt.title(' Average tooth lost per state')
	pyplt.show()
	# pyplt.savefig('compare_average_tooth_lost_per_state.png')

	symbolLine('-')
	# return " Graph saved as compare_average_tooth_lost_per_state.png in the directory of main program."

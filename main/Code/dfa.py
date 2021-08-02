from sys import argv

def reader(file):
	"""
	This funciton returns a matrix M[i][j] of the input file.csv.
	"""
	lines = open(file, 'r').readlines()
	a = []
	for i in range(0, len(lines)):
		a.append(lines[i].strip().split(','))
	return a

def reader_grammar(file):
	lines = open(file, 'r').readlines()
	a = []
	for i in range(0, len(lines)):
		a.append(lines[i].strip().split('->'))
	return a

def states(matr_of_file):
	"""
	This function returns a list of the sates of a given transition matrix of a machine.
	The input must be a list of list of the form M[i][j].
	"""
	a = []
	for i in range(1,len(matr_of_file)):
		a.append(matr_of_file[i][0])
	return a 

def alphabet(matr_of_file):
	"""
	This function returns a list of the alphabet of the machine M given by the input in matrix form M[i][j].
	"""
	a = []
	for i in range(1, len(matr_of_file[0])-1):
		a.append(matr_of_file[0][i])
	return a

def number_list(l):
	"""
	This function returns a list of number from 1 to len(l) given the list l.
	"""
	a = []
	for x in range(1,len(l)+1):
		a.append(x)
	return a

def trans_func(matr_of_file, state, char):
	"""
	This function returns the state that the machine goes to, given an state and a character of the alphabet.
	e.g. trans_funciton('state[0]', 'a') = 'state1'
	"""
	return matr_of_file[dict(zip(states(matr_of_file), number_list(states(matr_of_file))))[state]][dict(zip(alphabet(matr_of_file), number_list(alphabet(matr_of_file))))[char]]

def init_state(matr_of_file):
	"""
	This function returns te initial state of the machine M given by the input in matrix form M[i][j].
	"""
	return matr_of_file[1][0]

def eof(matr_of_file):
	"""
	This function returns a list of the acceptance states of the machine M given by the input in matrix form M[i][j].
	"""
	a = []
	for i in range(0,len(states(matr_of_file))):
		if matr_of_file[i+1][len(matr_of_file[0])-1] == 'accept':
			a.append(states(matr_of_file)[i])
	return a

def isinalpha(a, alph):
	"""
	This is a boolean function that tells if the character a is in the alphabet alph.
	e.g. isinalpha('a', ['a', 'b']) = True
	"""
	return a in alph

def machine(file, string):
	"""
	This function implements the SFA give the input file in matrix form M[i][j] and given a string.
	e.g. machine(reader('filename.csv'), 'hola') = No
	"""
	if isinalpha(string[0], alphabet(file)):
		s0 = trans_func(file, init_state(file), string[0])
		i = 0
		while i < len(string)-1:
			n = s0
			i += 1
			if isinalpha(string[i], alphabet(file)):
				try:	
					s0 = trans_func(file, n, string[i])
				except:
					return 'no'
			else:
				return 'no'
		if (s0 in eof(file)) == True:
			return 'yes'
		else:
			return 'no'
	else:
		return 'no'

scrpt, file, string = argv
print(machine(reader(file), string))
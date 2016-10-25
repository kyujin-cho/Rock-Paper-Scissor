"""
Python code simulating Rock Paper Scissor game.
"""

from random import randint as rand
items = ['Scissor', 'Rock', 'Paper']
win = 0
lose = 0

class User(object):
	"""This class represents a user with win, lose value"""
	def __init__(self, lose, win, draw):
		self.__lose = lose
		self.__win = win
		self.__draw = draw

	"""This method returns encapulsed win value

	:returns: Integer win value
	"""

	@property
	def win(self):
		return self.__win

	"""This method returns encapulsed draw value

	:returns: Integer draw value
	"""
	
	@property
	def draw(self):
		return self.__draw

	"""This method returns encapulsed lose value

	:returns: Integer lose value
	"""
	@property
	def lose(self):
		return self.__lose

	"""This method is intended to increase win value by parameter v.
	
	:param int v: An integer value
	"""
	def addWin(self):
		self.__win += 1

	"""This method is intended to increase draw value by parameter v.
	
	:param int v: An integer value
	"""

	def addDraw(self):
		self.__draw += 1

	"""This method is intended to increase lose value by parameter v.
	
	:param int v: An integer value
	"""

	def addLose(self):
		self.__lose += 1
	

	
"""This function is intended to return the decesion by user

:returns: User's input kwd, should be one of the items in list 'items'
"""

def get_user_input():
	user_hand = input('Input : ')
	if user_hand not in items:
		while user_hand not in items:
			user_hand = input('Input : ')
	return user_hand


"""This function is intended to decide whether user beats or defeated by computer.

:param String user_hand: User's input value.
:param String user_hand: Computer's value, decided randomly.
:returns: Capitalized alphabet W/D/L, which means Win/Draw/Lose
"""

def decide(user_hand, computer_hand):
	if user_hand == computer_hand:
		return 'D'
	else:
		if user_hand == 'Scissor' or user_hand == '2':
			if computer_hand == 'Rock':
				return 'L'
			elif computer_hand == 'Paper':
				return 'W'
		elif user_hand == 'Rock' or user_hand == '1':
			if computer_hand == 'Paper':
				return 'L'
			elif computer_hand == 'Scissor':
				return 'W'
		elif user_hand == 'Paper' or user_hand == '3':
			if computer_hand == 'Scissor':
				return 'L'
			elif computer_hand == 'Rock':
				return 'W'


person = User(0, 0, 0)

while person.win + person.lose != 10:
	print("Game #" + str(person.win + person.lose + 1))
	computer = items[rand(0, 2)]
	user = get_user_input()

	result = decide(user, computer)
	print("You've ", end='')
	if result == 'L':
		print("Lost.")
		person.addLose()
	elif result == 'D':
		print("Draw.")
		person.addDraw()
	else:
		print("Won.")
		person.addWin()


print("Game ended.")
print("You've won", person.win, "times.")
print("You've lose", person.lose, "times.")
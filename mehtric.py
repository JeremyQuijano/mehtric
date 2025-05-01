#############################
#
# mehtric_main.py
#
#############################

### import packages
import os

### import class files
from mehtric_lexer import MehtricLexer
from mehtric_parser import MehtricParser
from mehtric_interpreter import MehtricInterpreter
from mehtric_interpreter import language_name as lang_name
from mehtric_interpreter import ascii_art

### clear console
os.system('cls')

### initialize main
if __name__ == '__main__':
	"""
	__main__

	Main program loop.
	Runs program until input = quit
	"""

	### create instances of lexer and parser
	lexer = MehtricLexer() 
	parser = MehtricParser()

	### ascii art header
	ascii_art('program_name')
	print("Enter code or \"help\" to display the user manual.\n\n\n")
	
	### create environment
	env = {} 
	
	### main running loop
	while True: 
		
		### try user input
		try:

			### user input
			text = input(lang_name + " > ")

		### end of file error
		except EOFError: 
			break
		
		### tokenize, parse, and interpret user input
		if text:
			### perform user operation
			try:
				tree = parser.parse(lexer.tokenize(text)) 
				MehtricInterpreter(tree, env)

			### print error if found
			except Exception as e:
				print(f"Parsing failed: {e}\n")
				continue
			
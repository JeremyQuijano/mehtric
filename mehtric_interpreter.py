#############################
#
# mehtric_interpreter.py
#
#############################

### import packages
import os
import sys
import time

### language name
language_name = "mehtric"

### define execution class
class MehtricInterpreter:
	
	### initialize environment
	def __init__(self, tree, env, silent=False):
		self.env = env
		self.silent = silent
		result = self.walkTree(tree)
		if result is not None and not silent:
			print(f'mehTPUT > {result}')
		elif result is not None and silent:
			print(result)

	### using walkTree to step through input
	def walkTree(self, node):
		"""
		walkTree

		Steps through user input checking for types, 
		variables, operation, etc.
		"""

		### check for types
		if isinstance(node, (int, float, str, bool)):
			return node 

		### check for none
		if node is None:
			return None

		if node[0] == 'program':
			if node[1]: self.walkTree(node[1])
			if node[2]: self.walkTree(node[2])
			return None

		### check nodes for types

		### number type
		if node[0] == 'num':
			return node[1] 

		### string type
		if node[0] == 'str':
			return node[1]
		
		### boolean type
		if node[0] == 'bool':
			return node[1]
		
		### group type
		if node[0] == 'group':
			return self.walkTree(node[1])
		
		### variable assignments
		if node[0] == 'var_assign':
			var_name = node[1]
			value = self.walkTree(node[2])
			if value is None:
				return None
			self.env[var_name] = value
			return None
		
		### variables
		if node[0] == 'var':
			var_name = node[1]
			if var_name in self.env:
				return self.env[var_name]
			else:
				self.handle_error('undefined_variable', var_name)

		### parse operation type
		try:
			left = self.walkTree(node[1]) if len(node) > 1 else None
			right = self.walkTree(node[2]) if len(node) > 2 else None
		except IndexError:
			left = self.walkTree(node[1])
		
		### operation ladder
		match node[0]:
			### arithmetic operations
			case 'add':
				if not self.silent:
					print(f'mehPERATION > {left} + {right}')
				if isinstance(left, str) and isinstance(right, str):
					result = left + right
					return result
				if isinstance(left, (int, float)) and isinstance(right, (int, float)):
					result = left + right
					return result
				self.handle_error('math_error', 'Cannot add non-numeric types')

			case 'sub':
				if not self.silent:
					print(f'mehPERATION > {left} - {right}')
				if isinstance(left, (int, float)) and isinstance(right, (int, float)):
					result = left - right
					return result
				self.handle_error('math_error', 'Subtraction requires numeric operands')
			
			case 'mul':
				if not self.silent:
					print(f'mehPERATION > {left} * {right}')
				if isinstance(left, (int, float)) and isinstance(right, (int, float)):
					result = left * right
					return result
				self.handle_error('math_error', 'Multiplication requires numeric operands')
			
			case 'div':
				if not self.silent:
					print(f'mehPERATION > {left} / {right}')
				if right == 0:
					self.handle_error('division_by_zero')
					return None
				result = left / right
				return result
			
			case 'mod':
				if not self.silent:
					print(f'mehPERATION > {left} % {right}')
				if right == 0:
					self.handle_error('division_by_zero')
					return None
				result = left % right
				return result
			
			case 'pow':
				if not self.silent:
					print(f'mehPERATION > {left} ^ {right}')
				try:
					result = left ** right
					return result
				except Exception:
					self.handle_error('math_error', 'Exponentiation error')
			
			### comparison operations
			case 'eqeq':
				if not self.silent:
					print(f'mehPERATION > {left} == {right}')
				if type(left) != type(right):
					self.handle_error('type_error', 'Comparison requires operands of the same type')
				result = left == right
				return result
			
			case 'noteq':
				if not self.silent:
					print(f'mehPERATION > {left} != {right}')
				if type(left) != type(right):
					self.handle_error('type_error', 'Comparison requires operands of the same type')
				result = left != right
				return result
			
			case 'lte':
				if not self.silent:
					print(f'mehPERATION > {left} <= {right}')
				if type(left) != type(right):
					self.handle_error('type_error', 'Comparison requires operands of the same type')
				result = left <= right
				return result
			
			case 'gte':
				if not self.silent:
					print(f'mehPERATION > {left} >= {right}')
				if type(left) != type(right):
					self.handle_error('type_error', 'Comparison requires operands of the same type')
				result = left >= right
				return result
			
			case 'lt':
				if not self.silent:
					print(f'mehPERATION > {left} < {right}')
				if type(left) != type(right):
					self.handle_error('type_error', 'Comparison requires operands of the same type')
				result = left < right
				return result
			
			case 'gt':
				if not self.silent:
					print(f'mehPERATION > {left} > {right}')
				if type(left) != type(right):
					self.handle_error('type_error', 'Comparison requires operands of the same type')
				result = left > right
				return result
			
			### quit command
			case 'quit':
				if input("\nAre you sure you want to exit the program?\n(y to exit) ") == 'y':
					print(f"\n{language_name} shutting down...\n")
					time.sleep(1)
					os.system('cls')
					sys.exit()
				else:
					print()
					return None

			### exit command
			case 'exit':
				if input("\nAre you sure you want to exit the program?\n(y to exit) ") == 'y':
					print(f"\n{language_name} shutting down...\n")
					time.sleep(1)
					os.system('cls')
					sys.exit()
				else:
					print()
					return None
				
			### clear command
			case 'clear':
				os.system('cls')
				print(r"""
                 _     _    
                | |   | |     
  _ __ ___   ___| |__ | |_ _ __ _  ___ 
 | '_ ` _ \ / _ \ '_ \| __| '__| |/ __|
 | | | | | |  __/ | | | |_| |  | | (__ 
 |_| |_| |_|\___|_| |_|\__|_|  |_|\___|
	   				""")
				print("Enter code or \"help\" to display the user manual.\n\n\n")
				return None
			
			### restart command
			case 'restart':
				print(f"\n{language_name} restarting...\n")
				time.sleep(1)
				os.system('cls')
				sys.exit(os.system(f'python3 ./{language_name}_main.py'))

			### help command
			case 'help':
				self.help_menu()
				return None
			
			### meh command
			case 'meh':
				print('Have a meh day. ¯\_(ツ)_/¯\n')
				print(r"""
                 _     
                | |    
  _ __ ___   ___| |__  
 | '_ ` _ \ / _ \ '_ \ 
 | | | | | |  __/ | | |
 |_| |_| |_|\___|_| |_|
		  """)
				return None
			
			### defualt case error
			case _:
				self.handle_error('runtime_error', node[0])

	### error handling function
	def handle_error(self, error_type, *args):
		match error_type:
			case 'reserved_keyword_error':
				print(f"\nReservedKeywordError: '{args[0]}' is a reserved keyword and cannot be used as a variable at line {args[1]}.")
				raise SyntaxError(f"Reserved keyword used as variable: {args[0]}")
			
			case 'illegal_symbol':
				print(f"\nIllegal character '{args[0]}' at line {self.lineno}")
				raise SyntaxError(f"Illegal character: {args[0]}")
			
			case 'syntax_error':
				print(f"\nSyntaxError: Unexpected token {args[0]} ('{args[1]}') at line {args[2]}")
				raise SyntaxError(f"Unexpected token {args[0]} ('{args[1]}')")
			
			case 'math_error':
				print(f"\nMathError: {args[0]}")
				raise ValueError(f"Math error: {args[0]}")
			
			case 'assignment_error':
				print("\nAssignmentError: Left-hand side must be a variable name.")
				raise SyntaxError("Assignment error: Invalid assignment target.")
			
			case 'runtime_error':
				print(f"\nRuntimeError: Unknown operation '{args[0]}'")
				raise RuntimeError(f"Unknown operation: {args[0]}")
			
			case 'undefined_variable':
				print(f"\nNameError: Undefined variable '{args[0]}'")
				raise NameError(f"Undefined variable: {args[0]}")
			
			case 'division_by_zero':
				print("\nMathError: Division by zero.")
				raise ZeroDivisionError("Division by zero.")
			
			case _:
				print(f"\nUnknown error: {error_type}")
				raise Exception(f"Unknown error: {error_type}")

	### reserved words for built-in functions/methods/commands
	### extendable for more pre-defined functions/methods/commands
	keywords = {
		'command': ['quit', 'exit', 'clear', 'restart', 'help', 'meh',],
		'value': ['QUIT', 'EXIT', 'CLEAR', 'RESTART', 'HELP', 'MEH',],
		'def': [
			'quit: Shuts down program.',
			'exit: Shuts down program.',
			'clear: Clears console screen.',
			'restart: Restarts program.',
			'help: Displays user manual.',
			'meh: Displays mehssage',
		],
	}
	
	### help funciton
	def help_menu(self):
		### ascii art header
		print(r"""
                 _     _ 
                | |   | |   
  _ __ ___   ___| |__ | |_ _ __ _  ___ 
 | '_ ` _ \ / _ \ '_ \| __| '__| |/ __|
 | | | | | |  __/ | | | |_| |  | | (__ 
 |_| |_| |_|\___|_| |_|\__|_|  |_|\___|
  _    _  _____ ______ _____    __  __          _   _ _    _         _      
 | |  | |/ ____|  ____|  __ \  |  \/  |   /\   | \ | | |  | |  /\   | |     
 | |  | | (___ | |__  | |__) | | \  / |  /  \  |  \| | |  | | /  \  | |     
 | |  | |\___ \|  __| |  _  /  | |\/| | / /\ \ | . ` | |  | |/ /\ \ | |     
 | |__| |____) | |____| | \ \  | |  | |/ ____ \| |\  | |__| / ____ \| |____ 
  \____/|_____/|______|_|  \_\ |_|  |_/_/    \_\_| \_|\____/_/    \_\______|
    """)

		print(f"\n{language_name} User Manual")
		print("Created by Jeremy Quijano\n")

		### supported functionality
		print("Supported Functionality:")
		print("- Data Types:")
		print("    • int     → whole numbers (e.g., 42)")
		print("    • float   → decimal numbers (e.g., 3.14)")
		print("    • string  → text (e.g., \"hello\")")
		print("- Arithmetic Operators:")
		print("    • +, -, *, /, %, ^")
		print("    • Example: 2 + 3 * 4 → 14")
		print("- Comparison Operators:")
		print("    • ==, !=, <, <=, >, >=")
		print("    • Example: 5 == 5 → true")
		print("- Variables:")
		print("    • Use '=' to assign values")
		print("    • Example: x = 10")
		print("- Silent Output:")
		print("    • User can change the output type by changning the 'silent' variable in the interpreter file.")
		print("    • mehtric_interpreter.py → MehtricInterpreter → def __init__(..., silent=True/False):")
		print("    • silent = True	→ No operation or output message.")
		print("    • silent = False	→ Includes operation and output message.")

		### reserved words
		print("\nReserved Words:")
		print("These cannot be used as variable names:")
		for word in self.keywords['def']:
			print(f"    • {word}")

		### examples section
		print("\nExamples:")
		print("  ### variable assignment")
		print("  x = 5")
		print("  y = x * 2")

		print("\n  ### strings and concatenation")
		print("  msg = \"Hello\" + \" \" + \"World!\"")

		print("\nEnd of User Manual.\n")
		return None
	

#############################
#
# mehtric_lexer.py
#
#############################

### import Lexer package
from sly import Lexer
from mehtric_interpreter import MehtricInterpreter

### define lexer class
class MehtricLexer(Lexer):
	"""
	BasicLexer

	Defines tokens, ignores, literals for user input.
	Defines variables, numbers, strings, comments, and newlines.
	"""

	### import handle_error from Interpreter
	handle_error = MehtricInterpreter.handle_error

	### import reserved keywords from interpreter
	reserved_keywords = MehtricInterpreter.keywords

	### token types
	### extendable for more tokens
	tokens = {
		NAME, NUMBER, STRING, 
		EQEQ, NOTEQ, LTE, GTE, LT, GT, 
		} | set(reserved_keywords['value'])

	### ignore/skip tokens
	ignore = '\t '

	### comparison operator symbol token
	EQEQ	= r'=='
	NOTEQ	= r'!='
	LTE		= r'<='
	GTE		= r'>='
	LT		= r'<'
	GT		= r'>'

	### built-in literals
	literals = {'=', '+', '-', '/', '%', '*', '^', '(', ')', ',', '.', ';', '[', ']',}

	### define tokens as regular expressions (stored as raw strings)

	### name token
	@_(r'[a-zA-Z_][a-zA-Z0-9_]*')
	def NAME(self, t):
		return t

	### number token 
	@_(r'\d+(\.\d+)?')
	def NUMBER(self, t):
		### convert it into a python integer 
		t.value = float(t.value) if '.' in t.value else int(t.value)
		return t
	
	### string token
	@_(r'"[^"\n]*"')
	def STRING(self, t):
		t.value = t.value[1:-1]
		return t

	### comment token 
	@_(r'//.*')
	def COMMENT(self, t):
		pass

	### newline token (used only for showing errors in new line) 
	@_(r'\n+')
	def newline(self, t):
		self.lineno += t.value.count('\n')
	
	### error for illegal symbols
	def error(self, t):
		self.handle_error('illegal_symbol', t.value[0])
		self.index += 1
		return None
	
#############################
#
# mehtric_parser.py
#
#############################
 
### import Parser and class files
from sly import Parser
from mehtric_lexer import MehtricLexer
from mehtric_interpreter import MehtricInterpreter

### define parser class
class MehtricParser(Parser): 
	"""
	BasicParser

	Parses user input and checks for possible experssions
	"""
	### tokens are passed from lexer to parser 
	tokens = MehtricLexer.tokens 

	### reserved keywords passed from lexer to parser
	reserved_keywords = MehtricInterpreter.keywords['command']

	### import handle_error from interpreter
	handle_error = MehtricInterpreter.handle_error

	### precedence for operations
	precedence = ( 
		('left', '+', '-'), 
		('left', '*', '/', '%'),
		('left', EQEQ, NOTEQ, LTE, GTE, LT, GT),
		('right', 'UMINUS', '^'), 
	) 

	### initialize environment
	def __init__(self):
		self.env = { }
		self.lineno = 1

	### skip
	@_('')
	def statement(self, p):
		pass
	
	### variable names
	@_('NAME')
	def expr(self, p):
		if p.NAME in self.reserved_keywords:
			return (p.NAME,)
		else:
			return ('var', p.NAME)
	
	### variable assignment
	@_("NAME '=' expr")
	def statement(self, p):
		if p.NAME in self.reserved_keywords:
			self.handle_error('reserved_keyword_error', p.NAME, p.lineno)
			return
		else:
			self.env[p.NAME] = p.expr
			return ('var_assign', p.NAME, p.expr)
		
	### numbers
	@_('NUMBER')
	def expr(self, p):
		return ('num', p.NUMBER)

	### strings
	@_('STRING')
	def expr(self, p):
		return('str', p.STRING)

	### mathematical expressions
	@_('expr')
	def statement(self, p):
		return (p.expr)

	@_('expr "+" expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('add', p.expr0, p.expr1)

	@_('expr "-" expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('sub', p.expr0, p.expr1)


	@_('expr "*" expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('mul', p.expr0, p.expr1)


	@_('expr "/" expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('div', p.expr0, p.expr1)

	
	@_('expr "%" expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('mod', p.expr0, p.expr1)

	@_('expr "^" expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('pow', p.expr0, p.expr1)


	@_('"-" expr %prec UMINUS')
	def expr(self, p):
		if p.expr[0] in self.reserved_keywords:
			self.handle_error('reserved_keyword_error', p.expr[0], p.lineno)
			return None
		else:
			return p.expr
	
	@_('"(" expr ")"')
	def expr(self, p):
		if p.expr[0] in self.reserved_keywords:
			self.handle_error('reserved_keyword_error', p.expr[0], p.lineno)
			return None
		else:
			return ('group', p.expr)
	
	### comparison operations
	@_('expr EQEQ expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('eqeq', p.expr0, p.expr1)
	
	@_('expr NOTEQ expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('noteq', p.expr0, p.expr1)
	
	@_('expr LTE expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('lte', p.expr0, p.expr1)
	
	@_('expr GTE expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('gte', p.expr0, p.expr1)
	
	@_('expr LT expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('lt', p.expr0, p.expr1)
	
	@_('expr GT expr')
	def expr(self, p):
		if self._is_reserved(p.expr0):
			self.handle_error('reserved_keyword_error', p.expr0[0], p.lineno)
			return None
		elif self._is_reserved(p.expr1):
			self.handle_error('reserved_keyword_error', p.expr1[0], p.lineno)
			return None
		else:
			return ('gt', p.expr0, p.expr1)
	
	### quit keyword
	@_('QUIT')
	def statement(self, p):
		return ('quit',)
	
	### exit keyword
	@_('EXIT')
	def statement(self, p):
		return ('exit',)
	
	### clear keyword
	@_('CLEAR')
	def statement(self, p):
		return ('clear',)
	
	### restart keyword
	@_('RESTART')
	def statement(self, p):
		return ('restart',)
	
	### help keyword
	@_('HELP expr')
	def statement(self, p):
		return ('help', p.expr0)
	
	### help keyword
	@_('MEH expr')
	def statement(self, p):
		return ('meh', p.expr0)
	
	### error handling
	def _is_reserved(self, expr):
		if isinstance(expr, tuple):
			return expr[0] in self.reserved_keywords
		else:
			return False

	def error(self, p):
		if p:
			self.handle_error('syntax_error', p.type, p.value, p.lineno)
			return None
		
		else:
			self.handle_error('syntax_error', 'EOF', 'end of input', 0)
			return None

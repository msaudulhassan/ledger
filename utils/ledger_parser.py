import re
from utils.helpers import remove_dollar_signs, eval_expr, css_as_tokens
from utils.person import Name

class LedgerEntry():
	def __init__(self, ledger_line):
		self.verbatim = ledger_line
		self.tokens = parse_ledger_line(ledger_line)

	def has_ellipsis(self):
		for _, value in self.tokens.items():
			if is_ellipsis(value):
				return True
		return False

	def fill_ellipsis(self, ref_ledger_entry):
		for token, value in self.tokens.items():
			if is_ellipsis(value):
				self.tokens[token] = ref_ledger_entry[token]

	def __getitem__(self, item):
		return self.tokens[item]


def is_ellipsis(thing):
	if type(thing) is list:
		return thing[0] == '...'
	else:
		return thing == '...'


def parse_ledger_line(ledger_line):
	# matches = re.search(r"^\s*([^\+\-]+?)\s+(\+|\-)\s+\$?([\d\.\+\-\*\/\(\)\$]+)(\s+([^'\"]+))?(\s+'([^']+)')?$",
	# 					ledger_line)
	matches = re.search(r'^\s*([^\+\-]+?)\s+(\+|\-)\s+\$?([\d\.\+\-\*\/\(\)\$]+)(\s+([^"]+))?(\s+"([^"]+)")?$',
						ledger_line)

	names = [Name(name) for name in css_as_tokens(matches.group(1))]
	direction = matches.group(2)
	amount = eval_expr(remove_dollar_signs(matches.group(3)))
	date = matches.group(5)
	desc = matches.group(7)		

	return {'names': names, 'direction': direction, 'amount': amount,
			'date': date, 'desc': desc}
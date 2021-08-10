import re

def remove_dollar_signs(string):
	return string.replace("$", "")


def is_expr(string):
	# is expression?
	non_expr_stuff = re.search(r"[^\d\.\+\-\*\/\(\)\$]+", string)
	return True if non_expr_stuff is None else False
	

def eval_expr(string):
	# evaluate expression (with a little caution)
	if is_expr(string):
		return eval(string)
	else:
		raise ValueError("'%s' is not a valid expression" % string)

def css_as_tokens(string):
	# tokenize comma-seperated string (css)
	return re.split(r",\s*", string)

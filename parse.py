#! /usr/bin/env python

import argparse
from utils.ledger_parser import LedgerEntry
from utils.person import People


def main(ledger_path, my_name):
	# parse ledger into ledger entries (and fill in ellipsis)
	ledger_entries = []
	with open(ledger_path) as ledger:
		for line in ledger:
			ledger_entry = LedgerEntry(line)

			if ledger_entry.has_ellipsis():
				ledger_entry.fill_ellipsis(ledger_entries[-1])

			ledger_entries.append(ledger_entry)

	# process ledger entries to compute net balance for each person
	people = People()
	for line_num, entry in enumerate(ledger_entries):
		names = entry['names']
		amount_per_person = entry['amount'] / len(names)
		
		if len(names) > 1 and my_name in names and entry['direction'] == '-':
			raise Exception("error: line %i has multiple names, including %s," % (line_num, my_name) + 
				"\nbut its direction is -")
		
		for name in names:
			if name == my_name:
				continue
			if name not in people:
				people.add_person(name)

			people.get_person(name).update_balance(entry['direction'], amount_per_person)

	# pretty print
	for person in people:
		if person.balance > 0:
			print('$%.2f from %s to %s' % (abs(person.balance), person.name, my_name))
		elif person.balance < 0:
			print('$%.2f from %s to %s' % (abs(person.balance), my_name, person.name))
		else:
			print('%s and %s are square' % (my_name, person.name))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Parse Ledger')
	parser.add_argument('--path', type=str, default='ledger.txt',
						 help='path to ledger [%(type)s]')
	parser.add_argument('--name', type=str, default='Joe',
						 help='your name (default: %(default)s) [%(type)s]')

	args = parser.parse_args()

	main(args.path, args.name)
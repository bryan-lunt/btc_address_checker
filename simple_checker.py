#!/usr/bin/env python
from __future__ import print_function

from blockchain import util as BCU
import blockchain.blockexplorer as BCE

import re

address_matcher = re.compile("(A|a)ddress: (.*)")
def read_addresses_from_stream(an_input_stream):
	for line in an_input_stream:
		is_a_match = address_matcher.match(line)
		if is_a_match is not None:
			yield is_a_match.group(2).strip()

def group_things(in_iterator,group_size=10):
	a_group = list()
	count = 0
	while True:
		try:
			a_group.append(in_iterator.next())
		except StopIteration:
			yield a_group
			break
		except:
			yield a_group
			break
		else:
			count += 1
			if count == group_size:
				yield a_group
				count = 0
				a_group = list()
	#END of group_things


def main(input_stream,output_stream,group_size=200):
	#read the input file
	group_generator = group_things(
							read_addresses_from_stream(input_stream),
							group_size
							)
	for one_group in group_generator:
		group_balances = BCE.get_balance(tuple(one_group))
		for one_addr in one_group:
			one_balance = group_balances[one_addr].final_balance

			print("{}\t{}\t{}".format(str(one_addr),str(one_balance > 0.0).upper(), one_balance),file=output_stream)





if __name__ == "__main__":
	import argparse
	import sys
	parser = argparse.ArgumentParser(description="Check the balances of several accounts.")
	parser.add_argument("input",metavar="IN_FILE",type=str)
	parser.add_argument("output",metavar="OUT_FILE",type=str,default="-",nargs="?")

	args, other = parser.parse_known_args()

	in_stream = None
	out_stream = None
	if args.input == "-":
		in_stream = sys.stdin
	else:
		try:
			in_stream = file(args.input)
		except:
			print("Could not open the specified input file.",file=sys.stderr)
			sys.exit(1)

	if args.output == "-":
		out_stream = sys.stdout
	else:
		out_stream = file(args.output,"w")


	main(in_stream, out_stream, group_size=200)

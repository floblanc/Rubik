import random
import argparse

moves = ['F', 'B', 'L', 'R', 'U', 'D']
direction = ["", "'", "2"]


def range_type(value_string):
	value = int(value_string)
	if value not in range(1, 101):
		raise argparse.ArgumentTypeError(f"{value} is out of range, choose in [1-100]")
	return value


def scramble(number):
	string = ""
	last_m = ""
	m = ""
	d = ""
	for _ in range(number):
		while m == last_m:
			m = random.choice(moves)
			d = random.choice(direction) + " "
		string += m + d
		last_m = m
	return (string)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", "--number", type=range_type, metavar='[1-100]', choices=(range(1, 101)), help="number of moves to scramble", default=random.randint(1, 101))
	args = parser.parse_args()
	string = scramble(args.number)
	print(string)

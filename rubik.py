from timeit import default_timer as timer
from utils import ft_print, full_cube
import moves as mv
import argparse
import scramble
import solver
import sys
import random
import os

moves = ["F", "B", "L", "R", "U", "D", "f", "b", "l", "r", "u", "d"]
direction = ["", "'", "2"]
cube = ["U", "U", "U", "U", "U", "U", "U", "U", "U", "L", "L", "L", "L", "L", "L", "L", "L", "L", "F", "F", "F", "F", "F", "F", "F", "F", "F", "R", "R", "R", "R", "R", "R", "R", "R", "R", "B", "B", "B", "B", "B", "B", "B", "B", "B", "D", "D", "D", "D", "D", "D", "D", "D", "D"]
PATH = "/Users/florianblanchard/42_works/myRubik/"


def print_verbose(arg, verbose):
	if arg is True:
		print(verbose)


def commands_gen(args):
	commands = [0] * len(args)
	for x in range(len(commands)):
		commands[x] = [0] * 2
	for x in range(len(commands)):
		commands[x][0] = args[x][0]
		commands[x][1] = "" if len(args[x]) < 2 else args[x][1]
	return commands


def check_str(m):
	m = m.strip()
	error, nb = "", 0
	if len(m) > 0:
		m = m.split()
		for x in range(len(m)):
			if len(m[x]) > 2:
				error += f"\nArg {str(x + 1)} \"{m}\", is too long."
				nb += 1
			if m[x][0] not in moves:
				error += f"\nArg {str(x + 1)} \"{m[x]}\", \"{m[x][0]}\" doesn't match to an available move"
				nb += 1
			if len(m[x]) > 1 and m[x][1] not in direction:
				error += f"\nArg {str(x + 1)} \"{m[x]}\", \"{m[x][1]}\" doesn't match to an available direction"
				nb += 1
		if nb != 0:
			sys.exit(f"The following errors have been reported :{error}")
	return (m)


def scramble_default(n):
	moves = scramble.scramble(n).split()
	return moves


if __name__ == "__main__":
	start = timer()
	parser = argparse.ArgumentParser(prog="rubik.py", description="Rubik's cube solver")
	parser.add_argument("-v", "--verbose", help="Enable verbose", action="store_true")
	parser.add_argument("-uv", "--ultraverbose", help="Enable ULTRA verbose mode", action="store_true")
	parser.add_argument("-t", "--time", help="Display time", action="store_true")
	parser.add_argument("-vi", "--visu", help="Enable visual", action="store_true")
	parser.add_argument("-s", "--scramble", type=scramble.range_type, metavar='[1-100]', choices=(range(1, 101)), help="number of moves to scramble")
	parser.add_argument("-d", "--debug", help="Enable debug-mode", action="store_true")
	parser.add_argument("-n", "--none", help="If you are really rigorous", action="store_true")
	parser.add_argument("-c", "--correction", help="Correction verbose", action="store_true")
	parser.add_argument('Moves', nargs='?', type=check_str)
	args = parser.parse_args()
	if args.ultraverbose is True:
		args.verbose = True
	if args.debug is True or args.correction is True or args.none is True:
		args.verbose = False
		args.ultraverbose = False
		args.time = False
	if args.scramble is None:
		args.scramble = random.randint(1, 101)
	if args.Moves is None:
		args.Moves = scramble_default(args.scramble)
	if args.none is True:
		args.debug = False
		args.correction = False
	commands = commands_gen([x.upper() for x in args.Moves])
	verbose = ""
	if len(commands) != 0:
		if args.ultraverbose is True:
			verbose += f"{'Original Cube':^22}\n\n{ft_print(cube)}\n\n"
		if args.debug is False and args.correction is False and args.none is False:
			print(f"{'Scramble Moves'} ({len(commands)}):\n{' '.join(args.Moves)}\n")
		mv.use_move(commands, cube)
		if args.ultraverbose is True:
			verbose += f"{'Scrambled Cube':^22}\n\n{ft_print(cube)}\n"
		if cube == full_cube:
			sys.exit("Cube was already solved")
		solved, solved_len, tmp_vb = solver.solver(cube, args.ultraverbose, args.verbose, args.time)
		verbose += tmp_vb
		if args.time is True and solved_len != 0:
			if args.verbose is True:
				verbose += f"\nTotal time : {timer() - start:.5f} seconds\n"
			else:
				print(f"Total time : {timer() - start:.5f} seconds\n")
		print_verbose(args.verbose, verbose)
		if args.none is True:
			print(solved)
		if solved_len != 0 and args.debug is False and args.correction is False and args.none is False:
			print(f"Total moves to solve ({solved_len}):\n{solved}")
		if args.debug is True and args.correction is False:
			print(f"nb_s: {len(commands):>3} | nb_m: {solved_len:>3} | time: {timer() - start:>6.5f} ")
		if args.correction is True:
			print(f"{' '.join(args.Moves)} {solved}")
		if args.visu is True:
			os.system("processing-java --sketch=" + PATH + "visu --run \"" + ' '.join(args.Moves) + "\" \"" + solved + "\"")
	else:
		print("No scramble, Cube was already solved")

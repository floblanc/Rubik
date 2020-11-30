from g0 import g0
from g1 import g1
from g2 import g2
from g3 import g3
from timeit import default_timer as timer
from utils import return_moves, ft_print, simplify_moves


def verbosity(cube, uv, vb, time, phase, phase_str, start, real, moves, len_moves=0, verbose=""):
	verbose += f"\n\033[33m{phase} : {phase_str}\033[0m\n"
	if time is True:
		t = timer()
		real = t - real
		t = t - start
		if vb is True:
			verbose += f"Time : {t:>19.5f} seconds\n"
			if phase != "G0":
				verbose += f"Time from start :  {real:>.5f} seconds\n"
		else:
			print(f"\033[33m{phase}: \033[0m{t:>7.5f} seconds\n")
	verbose += f"{'Number of moves : ':<19}{len(moves[len_moves:])}\n{'Moves : ':<19}{return_moves(moves[len_moves:])}\n"
	if phase != "G0":
		verbose += f"{'Total Moves : ':<19}{len(moves)}\n"
	verbose += "\n"
	if uv is True:
		verbose += ft_print(cube)
	return verbose, len(moves)


def solver(cube, uv, vb, time):
	moves = []
	start = timer()
	edges, cube, moves = g0(cube, moves)
	g0_t = timer()
	verbose, len_moves = verbosity(cube, uv, vb, time, "G0", "Scrambled → Edges Orientation", start, start, moves)
	cube, moves = g1(edges, cube, moves, uv)
	g1_t = timer()
	verbose, len_moves = verbosity(cube, uv, vb, time, "G1", "Edges Orientation → Paired Colors for Top/​Bottom Face", g0_t, start, moves, len_moves, verbose)
	cube, moves = g2(cube, moves, uv)
	g2_t = timer()
	verbose, len_moves = verbosity(cube, uv, vb, time, "G2", "Paired Colors for Top/​Bottom Faces → Paired Colors for All Faces", g1_t, start, moves, len_moves, verbose)
	len_moves = len(moves)
	cube, moves = g3(cube, moves)
	verbose, len_moves = verbosity(cube, uv, vb, time, "G3", "Paired Colors for All Face → Solved Cube", g2_t, start, moves, len_moves, verbose)
	moves = simplify_moves(moves)
	return return_moves(moves), len(moves), verbose

import moves as mv
from utils import apply_move_e, make_edges, algo

g0_moves = [["L", ""], ["R", ""], ["F", ""], ["B", ""], ["U", ""], ["D", ""]]


def check_g0(cube):
	for j in range(24):
		face = int(j / 4)
		cubbie = cube[j]
		pos = j % 4
		if cubbie == "U" and (face == 1 or face == 3):
			return False
		elif cubbie == "L" and (face == 0 or face == 5):
			return False
		elif cubbie == "U" and (face == 2 or face == 4) and (pos == 0 or pos == 3):
			return False
		elif cubbie == "L" and (face == 2 or face == 4) and (pos == 1 or pos == 2):
			return False
	return True


def g0(cube, moves):
	edges = make_edges(cube)
	if check_g0(edges) is False:
		result, edges = algo(edges, check_g0, g0_moves, apply_move_e)
		mv.use_move(result, cube)
		moves += result
	return edges, cube, moves

import moves as mv
import edges_moves as e_mv
from utils import apply_move_e, algo, full_cube
from g0 import check_g0

g1_1_moves = [["L", ""], ["R", ""], ["F", ""], ["B", ""], ["U", ""], ["D", ""]]
g1_2_moves = [["R", ""], ["R", "'"], ["L", ""], ["L", "'"], ["U", ""], ["U", "'"], ["D", ""], ["D", "'"]]


def corner_cases(cube, bad_corner, m0):
	for m1 in (["", ""], ["U", ""], ["U", "2"], ["U", "'"]):
		for m2 in (["", ""], ["D", ""], ["D", "2"], ["D", "'"]):
			cpy = cube[:]
			mv.use_move([m0] + [m1] + [m2], cpy)
			if (cpy[24] == 'U' and cpy[27] == "U"):
				return ([m0] + [m1] + [m2] + [["L", ""], ["D", "'"], ["R", "2"], ["D", ""], ["L", "'"]])
			elif (cpy[11] == 'U' and cpy[26] == "U"):
				return ([m0] + [m1] + [m2] + [["R", "'"], ["D", ""], ["L", "2"], ["D", "'"], ["R", ""]])
	if bad_corner % 3 == 0:
		for m1 in (["", ""], ["U", ""], ["U", "2"], ["U", "'"]):
			for m2 in (["", ""], ["D", ""], ["D", "2"], ["D", "'"]):
				cpy = cube[:]
				mv.use_move([m0] + [m1] + [m2], cpy)
				if (cpy[24] == 'U' and cpy[20] == "U"):
					return ([m0] + [m1] + [m2] + [["L", ""], ["D", "'"], ["R", "2"], ["D", ""], ["L", "'"]])
				elif (cpy[18] == 'U' and cpy[26] == "U"):
					return ([m0] + [m1] + [m2] + [["R", "'"], ["D", ""], ["L", "2"], ["D", "'"], ["R", ""]])
	return None


def solve_ud_corners(cube, bad_corner):
	moves = []
	while bad_corner > 0:
		for m0 in (["", ""], ["F", "2"], ["B", "2"], ["L", "2"], ["R", "2"]):
			tmp = corner_cases(cube, bad_corner, m0)
			if tmp is not None:
				tmp[:] = [x for x in tmp if x[0]]
				break
		mv.use_move(tmp, cube)
		moves += tmp
		bad_corner = check_g1_corner(cube)
	return moves


def get_index(cube):
	itop, ibot = -1, -1
	top = cube[:4]
	bot = cube[20:]
	tmp = bot[0]
	bot[0] = bot[3]
	bot[3] = tmp
	for i in range(4):
		if top[i] != "U":
			itop = i
		if bot[i] != "U":
			ibot = i
	result = itop - ibot
	return itop, ibot, result


def aligned_cross(cube):
	itop, ibot, result = get_index(cube)
	if itop == -1 or ibot == -1 or result == 0:
		return []
	move = []
	for _ in range(3):
		e_mv.up_move(cube, "U")
		move += [["U", ""]]
		_, _, result = get_index(cube)
		if result == 0:
			break
	if len(move) == 2:
		move = [["U", "2"]]
	if len(move) == 3:
		move = [["U", "'"]]
	return move


def make_corner(cube):
	corner = []
	for face in range(6):
		for j in range(9):
			cubbie = cube[face * 9 + j]
			if cubbie == "D":
				corner.append("U")
			elif cubbie == "R":
				corner.append("L")
			elif cubbie == "B":
				corner.append("F")
			else:
				corner.append(cubbie)
	return corner


def check_g1_corner(cube):
	bad_corner = 0
	for i in (0, 2, 6, 8, 45, 47, 51, 53):
		if cube[i] != "U":
			bad_corner += 1
	return bad_corner


def check_g1_bis(cube):
	for j in (0, 1, 2, 3, 20, 21, 22, 23):
		cubbie = cube[j]
		if cubbie != "U":
			return False
	return check_g0(cube)


def check_g1(cube):
	up = 0
	down = 0
	for j in (0, 1, 2, 3):
		cubbie = cube[j]
		if cubbie == "U":
			up += 1
	for j in (20, 21, 22, 23):
		cubbie = cube[j]
		if cubbie == "U":
			down += 1
	if down >= 3 and up >= 3 and check_g0(cube):
		return True
	return False


def g1(edges, cube, moves, uv):
	if cube == full_cube:
		return cube, moves
	tmp = []
	if check_g1(edges) is False:
		result, edges = algo(edges, check_g1, g1_1_moves, apply_move_e)
		tmp += result
	result = aligned_cross(edges)
	tmp += result
	if check_g1_bis(edges) is False:
		result, edges = algo(edges, check_g1_bis, g1_2_moves, apply_move_e)
		tmp += result
	mv.use_move(tmp, cube)
	moves += tmp
	cube_tricolor = make_corner(cube)
	bad_corners = check_g1_corner(cube_tricolor)
	if (bad_corners > 0):
		result = solve_ud_corners(cube_tricolor, bad_corners)
		mv.use_move(result, cube)
		moves += result
	return cube, moves

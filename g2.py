from utils import apply_move, apply_move_e, make_edges, algo, full_cube
import moves as mv


g2_1_moves = [["L", "2"], ["R", "2"], ["F", "2"], ["B", "2"], ["U", ""], ["D", ""]]
g2_2_moves = [["R", "2"], ["F", "2"], ["U", ""]]
g2_3_moves = [["L", "2"], ["R", "2"], ["F", "2"], ["B", "2"], ["D", "2"], ["U", "2"]]
g2_4_moves = [["L", "2"], ["R", "2"], ["F", "2"], ["B", "2"], ["D", "2"], ["U", "2"]]


def check_config(edges):
	if edges[8] == "F" and edges[11] == "L" and edges[12] == "F" and edges[15] == "L" \
		and edges[16] == "F" and edges[19] == "L" and edges[4] == "F" and edges[7] == "L":
		return True
	return False


def aligned_corner(cube):
	m = []
	for i in ([["", ""]], [["U", ""]], [["U", "'"]], [["U", "2"]]):
		cpy = cube[:]
		mv.use_move(i, cpy)
		if cpy[9] == "R" and cpy[11] == "R":
			m += i
			mv.use_move(i, cube)
			break
	for i in ([["", ""]], [["D", ""]], [["D", "'"]], [["D", "2"]]):
		cpy = cube[:]
		mv.use_move(i, cpy)
		if cpy[15] == "L" and cpy[17] == "L":
			mv.use_move(i, cube)
			m += i
			break
	if cpy[15] == "L" and cpy[17] == "L" and cpy[9] == "R" and cpy[11] == "R":
		return [x for x in m if x[0]]


def get_g2_alg_1_match(cube):
	for face in range(1, 5):
		if cube[face * 9 + 0] == cube[face * 9 + 2]:
			alg_1_match = [["R", "'"], ["F", ""], ["R", "'"], ["B", "2"], ["R", ""], ["F", "'"], ["R", ""]]
			if face == 1:
				alg_1_match.insert(0, ["U", "'"])
			elif face == 3:
				alg_1_match.insert(0, ["U", ""])
			elif face == 4:
				alg_1_match.insert(0, ["U", "2"])
			return alg_1_match
		if cube[face * 9 + 6] == cube[face * 9 + 8]:
			alg_1_match = [["L", "'"], ["F", ""], ["L", "'"], ["B", "2"], ["L", ""], ["F", "'"], ["L", ""]]
			if face == 1:
				alg_1_match.insert(0, ["D", ""])
			elif face == 3:
				alg_1_match.insert(0, ["D", "'"])
			elif face == 4:
				alg_1_match.insert(0, ["D", "2"])
			return alg_1_match


def count_matched_corner_pairs(cube):
	matched_corner_pairs = 0
	for face in range(1, 5):
		if cube[face * 9 + 0] == cube[face * 9 + 2]:
			matched_corner_pairs += 1
		if cube[face * 9 + 6] == cube[face * 9 + 8]:
			matched_corner_pairs += 1
	return matched_corner_pairs


def is_matched_1(cube):
	count = count_matched_corner_pairs(cube)
	if count == 1 or count == 0 or count == 8:
		return True
	return False


def check_g2(cube):
	if check_g2_ud(cube) is False:
		return False
	count = count_matched_corner_pairs(cube)
	if count != 1 and count != 0 and count != 8:
		return False
	return True


def check_config_edges_g2(edges):
	bad_edges = check_g2_edges(edges)
	if bad_edges > 2 and edges[4] != edges[8] and edges[8] != edges[12] and edges[12] != edges[16] and edges[16] != edges[4]:
		return True
	if bad_edges == 2 and ((edges[4] == "F" and edges[8] == "L") or (edges[7] == "F" and edges[11] == "L")):
		return True
	return False


def check_g2_edges(edges):
	bad_edges = 0
	for j in (4, 7, 8, 11, 12, 15, 16, 19):
		face = int(j / 4)
		cubbie = edges[j]
		if cubbie == "F" and face != 2 and face != 4:
			bad_edges += 1
		if cubbie == "L" and face != 1 and face != 3:
			bad_edges += 1
	return bad_edges


def check_g2_ud(cube):
	for i in (0, 2, 6, 8):
		if cube[i] != "U":
			return False
	for j in (45, 47, 51, 53):
		if cube[j] != "D":
			return False
	return True


def match_corners_pairs(cube, moves):
	matched_corner_pairs = count_matched_corner_pairs(cube)
	if matched_corner_pairs != 8:
		if matched_corner_pairs != 0 and matched_corner_pairs != 1:
			result, cube = algo(cube, check_g2, g2_2_moves, apply_move)
			moves += result
		if count_matched_corner_pairs(cube) == 0:
			alg_no_match = [["R", "2"], ["F", "2"], ["R", "2"]]
			moves += alg_no_match
			mv.use_move(alg_no_match, cube)
		if count_matched_corner_pairs(cube) == 1:
			alg_1_match = get_g2_alg_1_match(cube)
			moves += alg_1_match
			mv.use_move(alg_1_match, cube)
	return moves, cube


def g2(cube, moves, uv):
	if cube == full_cube:
		return cube, moves
	if check_g2_ud(cube) is False:
		result, cube = algo(cube, check_g2_ud, g2_1_moves, apply_move)
		moves += result
	moves, cube = match_corners_pairs(cube, moves)
	moves += aligned_corner(cube)
	edges = make_edges(cube)
	bad_edges = check_g2_edges(edges)
	if bad_edges == 0:
		return cube, moves
	if bad_edges != 4:
		result, edges = algo(edges, check_config_edges_g2, g2_3_moves, apply_move_e)
		mv.use_move(result, cube)
		moves += result
		mv.use_move([["U", ""], ["L", "2"], ["R", "2"], ["D", "'"]], cube)
		moves += [["U", ""], ["L", "2"], ["R", "2"], ["D", "'"]]
	edges = make_edges(cube)
	if check_config(edges) is False:
		result, edges = algo(edges, check_config, g2_4_moves, apply_move_e)
		mv.use_move(result, cube)
		moves += result
	mv.use_move([["U", ""], ["L", "2"], ["R", "2"], ["D", "'"]], cube)
	moves += [["U", ""], ["L", "2"], ["R", "2"], ["D", "'"]]
	return cube, moves

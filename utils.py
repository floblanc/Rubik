import edges_moves as e_mv
import moves as mv
import sys


full_cube = ["U", "U", "U", "U", "U", "U", "U", "U", "U", "L", "L", "L", "L", "L", "L", "L", "L", "L", "F", "F", "F", "F", "F", "F", "F", "F", "F", "R", "R", "R", "R", "R", "R", "R", "R", "R", "B", "B", "B", "B", "B", "B", "B", "B", "B", "D", "D", "D", "D", "D", "D", "D", "D", "D"]
g3 = [["L", "2"], ["R", "2"], ["F", "2"], ["B", "2"], ["D", "2"], ["U", "2"]]


apply_move_e = {"U": e_mv.up_move, "D": e_mv.down_move, "R": e_mv.right_move, "L": e_mv.left_move, "F": e_mv.front_move, "B": e_mv.back_move}
apply_move = {"U": mv.up_move, "L": mv.left_move, "F": mv.front_move, "R": mv.right_move, "B": mv.back_move, "D": mv.down_move}


def is_same_or_opposite(a, b, duos):
	for i in range(len(duos)):
		if ((a in duos[i]) and (b in duos[i])):
			return True
	return False


def concat_moves(buff, duos):
	if len(buff) == 2 and buff[0][0] != buff[1][0]:
		return buff
	duo_index = [i for i in range(len(duos)) if buff[0][0] in duos[i]]
	values = ["", "2", "'"]
	symb_1 = duos[duo_index[0]][0]
	symb_2 = duos[duo_index[0]][1]
	move_1 = 0
	move_2 = 0
	for move in buff:
		value = [i for i in range(len(values)) if values[i] == move[1]][0] + 1
		if (move[0] == symb_1):
			move_1 += value
		else:
			move_2 += value
	move_1 = (move_1 % 4) - 1
	move_2 = (move_2 % 4) - 1
	new_buff = []
	if (move_1 != -1):
		new_buff += [[symb_1, values[move_1]]]
	if (move_2 != -1):
		new_buff += [[symb_2, values[move_2]]]
	return new_buff


def simplify_moves(moves):
	i = 0
	duos = [['U', 'D'], ['L', 'R'], ['F', 'B']]
	final_moves = []
	while i < len(moves):
		buff = []
		buff += [moves[i]]
		len_buff = len(buff)
		for j in range(i + 1, len(moves)):
			if (is_same_or_opposite(moves[j][0], buff[-1][0], duos)):
				buff += [moves[j]]
				len_buff = len(buff)
				if j == len(moves) - 1:
					buff = concat_moves(buff, duos)
			else:
				len_buff = len(buff)
				if len(buff) > 1:
					buff = concat_moves(buff, duos)
				break
		i += len_buff
		final_moves += buff
	return final_moves


def ft_print(cube):
	return("{0:>10s}{1:>2s}{2:>2s}\n{3:>10s}{4:>2s}{5:>2s}\n{6:>10s}{7:>2s}{8:>2s}\n\n{9:2s}{10:2s}{11:2s}{18:>4s}{19:>2s}{20:>2s}{27:>4s}{28:>2s}{29:>2s}{36:>4s}{37:>2s}{38:>2s}\n{12:2s}{13:2s}{14:2s}{21:>4s}{22:>2s}{23:>2s}{30:>4s}{31:>2s}{32:>2s}{39:>4s}{40:>2s}{41:>2s}\n{15:2s}{16:2s}{17:2s}{24:>4s}{25:>2s}{26:>2s}{33:>4s}{34:>2s}{35:>2s}{42:>4s}{43:>2s}{44:>2s}\n\n{45:>10s}{46:>2s}{47:>2s}\n{48:>10s}{49:>2s}{50:>2s}\n{51:>10s}{52:>2s}{53:>2s}\n".format(
		cube[0], cube[1], cube[2], cube[3], cube[4], cube[5], cube[6], cube[7], cube[8],
		cube[9], cube[10], cube[11], cube[12], cube[9 + 4], cube[14], cube[15], cube[16], cube[17],
		cube[18], cube[19], cube[20], cube[21], cube[22], cube[23], cube[24], cube[25], cube[26],
		cube[27], cube[28], cube[29], cube[30], cube[31], cube[32], cube[33], cube[34], cube[35],
		cube[36], cube[37], cube[38], cube[39], cube[40], cube[41], cube[42], cube[43], cube[44],
		cube[45], cube[46], cube[47], cube[48], cube[49], cube[50], cube[51], cube[52], cube[53]))


def make_edges(cube):
	edges = []
	for face in range(0, 6):
		for j in range(1, 8, 2):
			cubbie = cube[face * 9 + j]
			if cubbie == "D":
				edges.append("U")
			elif cubbie == "R":
				edges.append("L")
			elif cubbie == "B":
				edges.append("F")
			else:
				edges.append(cubbie)
	return edges


def mirror(m1, m2):
	if (m1 == "F" and m2 == "B") or (m2 == "F" and m1 == "B"):
		return True
	if (m1 == "L" and m2 == "R") or (m2 == "L" and m1 == "R"):
		return True
	if (m1 == "U" and m2 == "D") or (m2 == "U" and m1 == "D"):
		return True
	return False


def algo(cube, fun, auth_moves, apply_move):
	open_list = [(cube, [])]
	closed_list = {}
	i = 1
	while len(open_list) > 0:
		state = open_list.pop(0)
		hash_str = str(state[0])
		if hash_str not in closed_list:
			for move in auth_moves:
				if len(state[1]) > 0 and move[0] == state[1][-1][0]:
					continue
				cpy = state[0][:]
				apply_move[move[0]](cpy, move[0] + move[1])
				if fun(cpy) is True:
					return state[1] + [move], cpy
				open_list.append((cpy, state[1] + [move]))
				i += 1
			closed_list[hash_str] = hash_str
	sys.exit("No solutions")


def return_moves(moves):
	string = ""
	for i in moves:
		string += " " + i[0] + i[1]
	return string.strip()

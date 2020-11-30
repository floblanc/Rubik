from utils import apply_move, full_cube
import heapq
from moves import use_move


g3_moves = [["L", "2"], ["R", "2"], ["F", "2"], ["B", "2"], ["D", "2"], ["U", "2"]]


def solve_cube(cube):
	open_list1 = [(0, cube, [])]
	heapq.heapify(open_list1)
	full_list1 = {}
	i = 1
	closed_list1 = {}
	open_list2 = [(0, full_cube, [])]
	heapq.heapify(open_list2)
	full_list2 = {}
	j = 1
	closed_list2 = {}
	while len(open_list1) > 0 and len(open_list2) > 0:
		state1 = heapq.heappop(open_list1)
		hash_str = str(state1[1])
		if hash_str not in closed_list1:
			for move in g3_moves:
				if len(state1[2]) > 0 and move[0] == state1[2][-1][0]:
					continue
				cpy = state1[1][:]
				apply_move[move[0]](cpy, move[0] + move[1])

				if str(cpy) in full_list2:
					return state1[2] + [move] + full_list2.get(str(cpy))
				full_list1[str(cpy)] = state1[2] + [move]
				heapq.heappush(open_list1, (i, cpy, state1[2] + [move]))
				i += 1

		closed_list1[hash_str] = hash_str
		state2 = heapq.heappop(open_list2)
		hash_str = str(state2[1])
		if hash_str not in closed_list2:
			for move in g3_moves:
				if len(state2[2]) > 0 and move[0] == state2[2][-1][0]:
					continue
				cpy = state2[1][:]
				apply_move[move[0]](cpy, move[0] + move[1])

				if str(cpy) in full_list1:
					return full_list1.get(str(cpy)) + [move] + state2[2]
				full_list2[str(cpy)] = [move] + state2[2]
				heapq.heappush(open_list2, (i, cpy, [move] + state2[2]))
				j += 1

		closed_list2[hash_str] = hash_str


def g3(cube, moves):
	if cube != full_cube:
		result = solve_cube(cube)
		moves += result
		use_move(result, cube)
	return cube, moves

def use_move(src, cube):
	x = 0
	for x in range(len(src)):
		if(src[x][0] == "U"):
			up_move(cube, src[x][0] + src[x][1])
		elif(src[x][0] == "D"):
			down_move(cube, src[x][0] + src[x][1])
		elif(src[x][0] == "R"):
			right_move(cube, src[x][0] + src[x][1])
		elif(src[x][0] == "L"):
			left_move(cube, src[x][0] + src[x][1])
		elif(src[x][0] == "F"):
			front_move(cube, src[x][0] + src[x][1])
		elif(src[x][0] == "B"):
			back_move(cube, src[x][0] + src[x][1])


def switch_value(cube, face):
	# print("switch value")
	temp = cube[face * 9 + 0]
	cube[face * 9 + 0] = cube[face * 9 + 6]
	cube[face * 9 + 6] = cube[face * 9 + 8]
	cube[face * 9 + 8] = cube[face * 9 + 2]
	cube[face * 9 + 2] = temp

	temp1 = cube[face * 9 + 1]
	cube[face * 9 + 1] = cube[face * 9 + 3]
	cube[face * 9 + 3] = cube[face * 9 + 7]
	cube[face * 9 + 7] = cube[face * 9 + 5]
	cube[face * 9 + 5] = temp1
	return


def up_move(cube, move):
	if(move == "U"):
		switch_value(cube, 0)

		temp = cube[18]
		cube[18] = cube[27]
		cube[27] = cube[36]
		cube[36] = cube[9]
		cube[9] = temp

		temp = cube[19]
		cube[19] = cube[28]
		cube[28] = cube[37]
		cube[37] = cube[10]
		cube[10] = temp

		temp = cube[20]
		cube[20] = cube[29]
		cube[29] = cube[38]
		cube[38] = cube[11]
		cube[11] = temp
	elif(move == "U'"):
		up_move(cube, "U")
		up_move(cube, "U")
		up_move(cube, "U")
		return
	elif(move == "U2"):
		up_move(cube, "U")
		up_move(cube, "U")
	return


def down_move(cube, move):
	if(move == "D"):
		switch_value(cube, 5)

		temp = cube[24]
		cube[24] = cube[15]
		cube[15] = cube[42]
		cube[42] = cube[33]
		cube[33] = temp

		temp = cube[25]
		cube[25] = cube[16]
		cube[16] = cube[43]
		cube[43] = cube[34]
		cube[34] = temp

		temp = cube[26]
		cube[26] = cube[17]
		cube[17] = cube[44]
		cube[44] = cube[35]
		cube[35] = temp
		return
	elif(move == "D'"):
		down_move(cube, "D")
		down_move(cube, "D")
		down_move(cube, "D")
		return
	elif(move == "D2"):
		down_move(cube, "D")
		down_move(cube, "D")
	return


def right_move(cube, move):
	if(move == "R"):
		switch_value(cube, 3)

		temp = cube[20]
		cube[20] = cube[47]
		cube[47] = cube[42]
		cube[42] = cube[2]
		cube[2] = temp

		temp = cube[23]
		cube[23] = cube[50]
		cube[50] = cube[39]
		cube[39] = cube[5]
		cube[5] = temp

		temp = cube[26]
		cube[26] = cube[53]
		cube[53] = cube[36]
		cube[36] = cube[8]
		cube[8] = temp
		return
	elif(move == "R'"):
		right_move(cube, "R")
		right_move(cube, "R")
		right_move(cube, "R")
		return
	elif(move == "R2"):
		right_move(cube, "R")
		right_move(cube, "R")
	return


def left_move(cube, move):
	if(move == "L"):
		switch_value(cube, 1)

		temp = cube[18]
		cube[18] = cube[0]
		cube[0] = cube[44]
		cube[44] = cube[45]
		cube[45] = temp

		temp = cube[21]
		cube[21] = cube[3]
		cube[3] = cube[41]
		cube[41] = cube[48]
		cube[48] = temp

		temp = cube[24]
		cube[24] = cube[6]
		cube[6] = cube[38]
		cube[38] = cube[51]
		cube[51] = temp
		return
	elif(move == "L'"):
		left_move(cube, "L")
		left_move(cube, "L")
		left_move(cube, "L")
		return
	elif(move == "L2"):
		left_move(cube, "L")
		left_move(cube, "L")
	return


def front_move(cube, move):
	if(move == "F"):
		switch_value(cube, 2)

		temp = cube[6]
		cube[6] = cube[17]
		cube[17] = cube[47]
		cube[47] = cube[27]
		cube[27] = temp

		temp = cube[7]
		cube[7] = cube[14]
		cube[14] = cube[46]
		cube[46] = cube[30]
		cube[30] = temp

		temp = cube[8]
		cube[8] = cube[11]
		cube[11] = cube[45]
		cube[45] = cube[33]
		cube[33] = temp
		return
	elif(move == "F'"):
		front_move(cube, "F")
		front_move(cube, "F")
		front_move(cube, "F")
		return
	elif(move == "F2"):
		front_move(cube, "F")
		front_move(cube, "F")
	return


def back_move(cube, move):
	if(move == "B"):
		switch_value(cube, 4)

		temp = cube[0]
		cube[0] = cube[29]
		cube[29] = cube[53]
		cube[53] = cube[15]
		cube[15] = temp

		temp = cube[1]
		cube[1] = cube[32]
		cube[32] = cube[52]
		cube[52] = cube[12]
		cube[12] = temp

		temp = cube[2]
		cube[2] = cube[35]
		cube[35] = cube[51]
		cube[51] = cube[9]
		cube[9] = temp
		return
	elif(move == "B'"):
		back_move(cube, "B")
		back_move(cube, "B")
		back_move(cube, "B")
		return
	elif(move == "B2"):
		back_move(cube, "B")
		back_move(cube, "B")
	return

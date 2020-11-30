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
	temp1 = cube[face * 4]
	cube[face * 4] = cube[face * 4 + 1]
	cube[face * 4 + 1] = cube[face * 4 + 3]
	cube[face * 4 + 3] = cube[face * 4 + 2]
	cube[face * 4 + 2] = temp1


def up_move(cube, move):
	if move == "U'":
		up_move(cube, "U")
		up_move(cube, "U")
		up_move(cube, "U")
	if move == "U2":
		up_move(cube, "U")
		up_move(cube, "U")
	else:
		switch_value(cube, 0)
		temp = cube[8]
		cube[8] = cube[12]
		cube[12] = cube[16]
		cube[16] = cube[4]
		cube[4] = temp


def down_move(cube, move):
	if move == "D'":
		down_move(cube, "D")
		down_move(cube, "D")
		down_move(cube, "D")
	if move == "D2":
		down_move(cube, "D")
		down_move(cube, "D")
	else:
		switch_value(cube, 5)
		temp = cube[11]
		cube[11] = cube[7]
		cube[7] = cube[19]
		cube[19] = cube[15]
		cube[15] = temp


def right_move(cube, move):
	if move == "R'":
		right_move(cube, "R")
		right_move(cube, "R")
		right_move(cube, "R")
	if move == "R2":
		right_move(cube, "R")
		right_move(cube, "R")
	else:
		switch_value(cube, 3)
		temp = cube[10]
		cube[10] = cube[22]
		cube[22] = cube[17]
		cube[17] = cube[2]
		cube[2] = temp


def left_move(cube, move):
	if move == "L'":
		left_move(cube, "L")
		left_move(cube, "L")
		left_move(cube, "L")
	if move == "L2":
		left_move(cube, "L")
		left_move(cube, "L")
	else:
		switch_value(cube, 1)
		temp = cube[9]
		cube[9] = cube[1]
		cube[1] = cube[18]
		cube[18] = cube[21]
		cube[21] = temp


def front_move(cube, move):
	if move == "F'":
		front_move(cube, "F")
		front_move(cube, "F")
		front_move(cube, "F")
	if move == "F2":
		front_move(cube, "F")
		front_move(cube, "F")
	else:
		switch_value(cube, 2)
		temp = cube[3]
		cube[3] = cube[6]
		cube[6] = cube[20]
		cube[20] = cube[13]
		cube[13] = temp


def back_move(cube, move):
	if move == "B'":
		back_move(cube, "B")
		back_move(cube, "B")
		back_move(cube, "B")
	if move == "B2":
		back_move(cube, "B")
		back_move(cube, "B")
	else:
		switch_value(cube, 4)
		temp = cube[0]
		cube[0] = cube[14]
		cube[14] = cube[23]
		cube[23] = cube[5]
		cube[5] = temp

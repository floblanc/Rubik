void turnZ(int index, int dir) {
  for (int i = 0; i < cube.length; i++) {
    Cubie qb = cube[i];
    if (qb.z == index) {
      PMatrix2D matrix = new PMatrix2D();
      matrix.rotate(dir*HALF_PI);
      matrix.translate(qb.x, qb.y);
      qb.update(round(matrix.m02), round(matrix.m12), round(qb.z));
      qb.turnFacesZ(dir);
    }
  }
}

void turnY(int index, int dir) {
  for (int i = 0; i < cube.length; i++) {
    Cubie qb = cube[i];
    if (qb.y == index) {
      PMatrix2D matrix = new PMatrix2D();
      matrix.rotate(dir*HALF_PI);
      matrix.translate(qb.x, qb.z);
      qb.update(round(matrix.m02), qb.y, round(matrix.m12));
      qb.turnFacesY(dir);
    }
  }
}

void turnX(int index, int dir) {
  for (int i = 0; i < cube.length; i++) {
    Cubie qb = cube[i];
    if (qb.x == index) {
      PMatrix2D matrix = new PMatrix2D();
      matrix.rotate(dir*HALF_PI);
      matrix.translate(qb.y, qb.z);
      qb.update(qb.x, round(matrix.m02), round(matrix.m12));
      qb.turnFacesX(dir);
    }
  }
}

 void applyMove(String instruction) {
  int value = 0;
  switch (instruction) {
    case "U": 
      value = 0;
      break;
    case "U'": 
      value = 1;
      break;
    case "U2" :
      value = 2;
      break;
    case "D": 
      value = 3;
      break;
    case "D'": 
      value = 4;
      break;
    case "D2": 
      value = 5;
      break;
    case "L": 
      value = 6;
      break;
    case "L'": 
      value = 7;
      break;
    case "L2": 
      value = 8;
      break;
    case "R": 
      value = 9;
      break;
    case "R'": 
      value = 10;
      break;
    case "R2": 
      value = 11;
      break;
    case "F": 
      value = 12;
      break;
    case "F'" :
      value = 13;
      break;
    case "F2" :
      value = 14;
      break;
    case "B" :
      value = 15;
      break;
    case "B'" :
      value = 16;
      break;
    case "B2" :
      value = 17;
      break;
   }
  doubleMove = null;
  if (value % 3 == 0)
    sequence.add(allMoves[value + 1]);
  else if (value % 3 == 1)
    sequence.add(allMoves[value - 1]);
  else if (value % 3 == 2) {
    sequence.add(allMoves[value]);
    doubleMove = allMoves[value];
  }
  currentMove = allMoves[value];
  currentMove.start();
  counter++;
}

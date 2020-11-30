void keyPressed() {
  if (key == '+' && speed < 0.95)
    speed += 0.05;
  else if (key == '-' && speed > 0.05)
    speed -= 0.05;
  if (args == null) {
    if (key == 'c' && sequence.size() > 0 && currentMove.finished()) {
      currentMove = sequence.get(sequence.size() - 1);
      doubleMove = null;
      if (currentMove.d() == true)
        doubleMove = currentMove;
      currentMove.start();
      sequence.remove(sequence.size() - 1);
      counter--;
    }
  }
  if (key == ' ' && (scramble != null|| resolve != null)) {
    if (counterScramble < scramble.length)
      scrambling = scrambling == true ? false : true;
    else
      resolving = resolving == true ? false : true;  
  }
  applyMove(key);
}

void applyMove(char move) {
  int value = 0;
  if (currentMove.finished()) {
    switch (move) {
    case 'u': 
      value = 0;
      break;
    case 'U': 
      value = 1;
      break;
    case '1' :
      value = 2;
      break;
    case 'd': 
      value = 3;
      break;
    case 'D': 
      value = 4;
      break;
    case '2': 
      value = 5;
      break;
    case 'l': 
      value = 6;
      break;
    case 'L': 
      value = 7;
      break;
    case '3': 
      value = 8;
      break;
    case 'r': 
      value = 9;
      break;
    case 'R': 
      value = 10;
      break;
    case '4': 
      value = 11;
      break;
    case 'f': 
      value = 12;
      break;
    case 'F' :
      value = 13;
      break;
    case '5' :
      value = 14;
      break;
    case 'b' :
      value = 15;
      break;
    case 'B' :
      value = 16;
      break;
    case '6' :
      value = 17;
      break;
    }
    if (key == 'f' || key == 'F' || key == 'b' || key == 'B' ||
        key == 'u' || key == 'U' || key == 'd' || key == 'D' ||
        key == 'r' || key == 'R' || key == 'l' || key == 'L' ||
        key == '1' || key == '2' || key == '3' || key == '4' || key == '5' || key == '6') {
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
  }
}

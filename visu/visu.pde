import peasy.*;

PeasyCam cam;

float speed = 0.1;
int dim = 3;
Cubie[] cube = new Cubie[dim*dim*dim];

Move[] allMoves = new Move[] {
  new Move(0, -1, 0, 1, false), // U
  new Move(0, -1, 0, -1, false), // U'
  new Move(0, -1, 0, -1, true), // U2
  
  new Move(0, 1, 0, -1, false), // D
  new Move(0, 1, 0, 1, false), // D'
  new Move(0, 1, 0, 1, true), // D2
    
  new Move(-1, 0, 0, -1, false), // L
  new Move(-1, 0, 0, 1, false), // L'
  new Move(-1, 0, 0, 1, true), // L2

  new Move(1, 0, 0, 1, false), // R
  new Move(1, 0, 0, -1, false), // R'
  new Move(1, 0, 0, -1, true), // R2

  
  new Move(0, 0, 1, 1, false), // F
  new Move(0, 0, 1, -1, false), // F'
  new Move(0, 0, 1, -1, true), // F2
  
  new Move(0, 0, -1, -1, false), // B
  new Move(0, 0, -1, 1, false),  // B'
  new Move(0, 0, -1, 1, true), // B2
};

ArrayList<Move> sequence = new ArrayList<Move>();
int counter = 0;
int counterScramble = 0;
int counterResolve = 0;

boolean started = false;
boolean scrambling = false;
boolean resolving = false;

String[] scramble = null;
String[] resolve = null;

Move currentMove;
Move doubleMove = null;

void setup() {
  size(1400, 800, P3D);
  //fullScreen(P3D);
  cam = new PeasyCam(this, 400);
  currentMove = new Move (0, 0, 0, 0, false);
  currentMove.finished = true;
  if (args != null && args.length >= 1 && args.length <= 2) {
    scrambling = true;
    scramble = split(args[0].trim(), " ");
    if (args.length == 2) {
      resolving = true;
      resolve = split(args[1].trim(), " ");
    }
    applyMove(scramble[counterScramble++]);
    currentMove.start();
  }
  int index = 0;
  for (int x = -1; x <= 1; x++) {
    for (int y = -1; y <= 1; y++) {
      for (int z = -1; z <= 1; z++) {
        PMatrix3D matrix = new PMatrix3D();
        matrix.translate(x, y, z);
        cube[index] = new Cubie(matrix, x, y, z);
        index++;
      }
    }
  }
}

void HUD() {
  cam.beginHUD();
  fill(255);
  push();
  fill(100);
  rect(10, 10, 400, 1000);
  pop();
  textSize(32);
  text("Moves : " + counter, 100, 100);
  if (scrambling == true)
    text("SCRAMBLING", 500, 100);
  else if (resolving == true)
    text("SOLVING", 500, 100);
  else if (resolve != null && scramble != null && counterScramble == scramble.length && counterResolve == resolve.length)
    text("SOLVED", 500, 100);
  cam.endHUD();
}

void draw() {
  background(51); 
  HUD();
  rotateX(-0.5);
  rotateY(0.4);//0.01 * frameCount);
  rotateZ(0.1);

  currentMove.update();
  if (args == null || counterScramble == scramble.length)
    scrambling = false;
  if (resolve == null || args.length != 2 || counterResolve == resolve.length)
    resolving = false;
  if (currentMove.finished() && currentMove.d() && doubleMove != null) {
    currentMove = doubleMove; 
    doubleMove = null;
    if (currentMove != null) {
      currentMove.start();
    } 
  }
  if (scrambling == true && currentMove.finished()) {
    //print("s"+scramble[counterScramble] + " ");
    applyMove(scramble[counterScramble++]);
    currentMove.start();
  }
  else if (resolving == true && scrambling == false && currentMove.finished()) {
    //print("r"+resolve[counterResolve] + " ");
    applyMove(resolve[counterResolve++]);
    currentMove.start();
  } 

  
  scale(50);
  for (int i = 0; i < cube.length; i++) {
    push();
    if (abs(cube[i].z) > 0 && cube[i].z == currentMove.z) {
      rotateZ(currentMove.angle);
    } else if (abs(cube[i].x) > 0 && cube[i].x == currentMove.x) {
      rotateX(currentMove.angle);
    } else if (abs(cube[i].y) > 0 && cube[i].y ==currentMove.y) {
      rotateY(-currentMove.angle);
    }   
    cube[i].show();
    pop();
  }
}

class Move {
  float angle = 0;
  int x = 0;
  int y = 0;
  int z = 0;
  int dir;
  boolean animating = false;
  boolean finished = false;
  boolean d = false;

  Move(int x, int y, int z, int dir, boolean d) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.dir = dir;
    this.d = d;
  }

  Move copy() {
    return new Move(x, y, z, dir, d);
  }

  void start() {
    animating = true;
    finished = false;
    angle = 0;
  }

  boolean finished() {
    return finished;
  }
  
  boolean d() {
    return d;
  }

  void update() {
    if (animating) {
      angle += dir * speed;
      if (abs(angle) > HALF_PI) {
        angle = 0;
        animating = false;
        finished = true;
        if (abs(z) > 0) {
          turnZ(z, dir);
        } else if (abs(x) > 0) {
          turnX(x, dir);
        } else if (abs(y) > 0) {
          turnY(y, dir);
        }
        // make double move
        //if (this.d == true) {
        //  currentMove.start();
        //  return ;
        //}
      }
    }
  }
}

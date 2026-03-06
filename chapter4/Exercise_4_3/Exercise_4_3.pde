Emitter emitter;

void setup() {
  size(640,360);
  emitter = new Emitter();
}

void draw() {
  background(255);
  emitter.addParticle(mouseX, mouseY);
  emitter.run();
}
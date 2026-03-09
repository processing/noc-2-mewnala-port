// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

// Particles are generated each cycle through draw(),
// fall with gravity and fade out over time
// A ParticleSystem object manages a variable size
// list of particles.


System particleSystem;

void setup() {
  size(640, 360);
  particleSystem = new System(width/2-50, 50);
  frameRate(30); //slowding down the frame rate so you can see the animation more clearly;

}

void draw() {
    background(255);
    particleSystem.run();
}

void mousePressed() {

  particleSystem.BreakIntoPeices();

}

// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

// Simple Particle System

// A simple Particle class

class Particle {
  PVector position, velocity, acceleration;
  float lifespan, radius;
  
  
  Particle(float x, float y, float radius) {
    
    this.position =  new PVector(x, y);
    this.velocity = new PVector(0, 0); //starts of stationary
    this.acceleration = new PVector(0, 0);
    this.lifespan = 255;
    this.radius = radius;

  }

  void run() {

    this.update();
    this.show();
  }

  void applyForce(PVector force) {
    this.acceleration.add(force);
  }

  // Method to update position
  void update() {
    this.velocity.add(this.acceleration);
    this.position.add(this.velocity);
    this.lifespan -= 2;
    this.acceleration.mult(0);
  }

  // Method to display
  void show() {
    //I have removed the lifespan which acts as the alpha channel, because I didnt want you to see
    //the individual squares that make up the big square
    //
    stroke(127);
    strokeWeight(2);
    fill(127);

    rectMode(CENTER);
    rect(this.position.x, this.position.y, this.radius, this.radius);
  }

  // Is the particle still useful?
  boolean isDead() {
    return (this.lifespan < 0.0);
  }
}

// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

// Simple Particle System

// A simple Particle class

class Particle {
  PVector position, velocity, acceleration;
  float lifespan;

  //adding angularVelocity and angular acceleration;
  float angularVelocity, angularAcceleration, angle;

  Particle(float x, float y) {
    this.position =  new PVector(x, y);
    // For demonstration purposes the Particle has a random velocity.
    this.velocity = new PVector(random(-1, 1), random(-2, 0));
    this.acceleration = new PVector(0, 0);
    this.lifespan = 255.0;

    // For demonstration purposes, the Particle will have a random angular acceleration
    this.angularAcceleration = random(0, 0.2);
    this.angularVelocity = 0;
    this.angle = 0;

  }

  void update() {
    this.velocity.add(this.acceleration);
    this.position.add(this.velocity);
    this.lifespan -= 2.0;
    this.acceleration.mult(0);

    this.angularVelocity += this.angularAcceleration;
    this.angle += this.angularVelocity;


  }


  void show() {
    stroke(0, this.lifespan);
    fill(0, this.lifespan);

    //save the state of the current grid
    pushMatrix();
    rectMode(CENTER);
    translate(this.position.x,this.position.y);
    rotate(radians(angle));

    //decide to change circle to rectangle so you could see the rotation more clearly
    rect(0, 0, 20, 20);

    //return the original state of the grid
    popMatrix();

  }

  // Keeping the same physics model as with previous chapters
  void applyForce(PVector force) {
    this.acceleration.add(force);
  }

  // Is the Particle alive or dead?
  boolean isDead() {
    return (this.lifespan < 0);
  }
}

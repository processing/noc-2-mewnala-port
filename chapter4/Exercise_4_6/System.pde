// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

import java.util.Random;
Random stream = new Random();

class System {

  PVector origin;
  ArrayList<Particle> particles;

  int maxNumParticles; //having a set number of particles will allows the system to come to an end
  int count; //used to keep track of the number of particles in system

  int rows;
  int columns;

  float radius; //radius will shrink as broken objects gets shattered into smaller peices
  PVector gravity; //This force is applied to all particles in this system

  System(float x, float y) {

    this.origin = new PVector(x, y);

    this.particles = new ArrayList<Particle>();
    this.rows = stream.nextInt(10) + 2;
    this.columns = this.rows;

    this.maxNumParticles = this.rows*this.columns; //dealing with a nice square number, will be 4 or bigger

    this.count = 0;
    this.radius = 16;

    this.gravity = new PVector(0, 0.05);

    //we are going to make the particle a square made up of smaller squares
    //we will use the starting co-ordinates provided as the center of the top left partticle.
    //
    for (int i = 0; i < this.rows; ++i) {

      for (int j = 0; j < this.columns; ++j) {

        addParticle(x+(j*this.radius), y+(i*this.radius));

      }
    }
    
  }

  void addParticle(float x, float y) {

    if (this.count < this.maxNumParticles) {

      this.particles.add(new Particle(x, y, this.radius));
      this.count+=1;

    }
  }

  void BreakIntoPeices() {

    //Looping through backwards to delete

    for (Particle particle : this.particles) {

      //generate new RandomForce and apply it to each particle
      //
      PVector randomForce = PVector.random2D();
      particle.applyForce(randomForce);
    }

  }

  void run() {
    // Looping through backwards to delete
    for (int i = this.particles.size() - 1; i >= 0; i--) {
      this.particles.get(i).applyForce(gravity);
      this.particles.get(i).run();
      if (this.particles.get(i).isDead()) {
        // Remove the particle
        this.particles.remove(i);
      }
    }

  

    // Run every particle
    // ES6 for..of loop
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of
    // https://www.youtube.com/watch?v=Y8sMnRQYr3c
    // for (let particle of this.particles) {
    //   particle.run();
    // }

    // Filter removes any elements of the array that do not pass the test
    // I am also using ES6 arrow snytax
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
    // https://www.youtube.com/watch?v=mrYMzpbFz18
    // this.particles = this.particles.filter(particle => !particle.isDead());

    // Without ES6 arrow code would look like:
    // this.particles = this.particles.filter(function(particle) {
    //   return !particle.isDead();
    // });
  }

  //method to check if there are no more particles left alive
  //in a given system
  boolean isSystemDead() {

    return (particles.size() <=0 );
  }
}

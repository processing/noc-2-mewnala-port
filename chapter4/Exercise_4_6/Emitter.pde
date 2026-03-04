// The Nature of Code
// Daniel Shiffman
// http://natureofcode.com

import java.util.Random;
Random stream = new Random();

class Emitter {

  PVector origin;
  ArrayList<Particle> particles;

  int maxNumParticles; //having a set number of particles will allows the system to come to an end
  int count; //used to keep track of the number of particles in system

  float radius; //radius will shrink as broken objects gets shattered into smaller peices

  Emitter(float x, float y) {

    this.origin = new PVector(x, y);

    this.particles = new ArrayList<Particle>();
    this.maxNumParticles = stream.nextInt(100) + 1;
    this.count = 0;
    this.radius = 16;

    
  }

  void addParticle() {

    if (this.count < this.maxNumParticles) {

        if (this.count == 0) {
            
            this.particles.add(new Particle(this.origin.x-2, this.origin.y, this.radius));
            this.particles.add(new Particle(this.origin.x+2, this.origin.y, this.radius));
        }

        else {

            //used to keep track of the previous position of particle
            //the new particle will be addded there so when a particle is shattered, the new particle is placed at that position
            //
            PVector previousLocation = this.particles.get(this.particles.size() - 1).position;
            this.particles.add(new Particle(previousLocation.x-2, previousLocation.y + 10, this.radius));
            this.particles.add(new Particle(previousLocation.x+2, previousLocation.y + 10, this.radius));
            
        }

        this.count += 2;
        this.radius = this.radius/2;
    }
  }

  void run() {
    // Looping through backwards to delete
    for (int i = this.particles.size() - 1; i >= 0; i--) {
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

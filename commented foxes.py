import random
import pylab

# Global Variables
MAXRABBITPOP = 400
CURRENTRABBITPOP = 100
CURRENTFOXPOP = 10

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    global CURRENTRABBITPOP
    


    # rabbits reproduce with prob of 1.0 - (current pop of rabits / maximum pop of rabbits)
    for rabbit in range(CURRENTRABBITPOP):
        if CURRENTRABBITPOP in range(1001)[10:-1]:
            if random.random() < float(1.0 - (CURRENTRABBITPOP / MAXRABBITPOP)):
                CURRENTRABBITPOP += 1
            
                
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    

    for fox in range(CURRENTFOXPOP):
        print ""
        print "***"
        print "Fox number: " + str(fox+1)
        print "Rabbits in forest: " + str(CURRENTRABBITPOP)
        print "Foxes in forrest: " + str(CURRENTFOXPOP)
        print ""
        
        foxKillsRabbitProb = CURRENTRABBITPOP / float(MAXRABBITPOP)
        print "Chance of success: " + str(foxKillsRabbitProb*100) + "%"
        
        
        if random.random() < foxKillsRabbitProb:
            print "Caught a rabbit!"
            CURRENTRABBITPOP -= 1
            print "conditions met, rabbit pop decreased to: " + str(CURRENTRABBITPOP)
            print "Will reproduce wth a chance of 2/3"


            if random.random() < 2/float(3):
                CURRENTFOXPOP +=1
                print "One baby fox added!"
            else:
                print "No babies today"
        else:
            print "No rabbit caught, will die with 0.1 prob"
            if random.random() < 0.1:
                CURRENTFOXPOP -=1
                print "dead fox"
            else:
                print "Survived"


def testStep():
    print "Zajici: " + str(CURRENTRABBITPOP)
    print "Lisky: " + str(CURRENTFOXPOP)
    
    rabbitGrowth()
    foxGrowth()
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    
    global CURRENTRABBITPOP,CURRENTFOXPOP
    rabbit_populations = []
    fox_populations = []
    
    for step in range(numSteps):
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)

        
        rabbitGrowth()
        foxGrowth()
        
        
    return (rabbit_populations,fox_populations)
    
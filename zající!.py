import random
import pylab

# Global Variables
CURRENTRABBITPOP = 10
CURRENTFOXPOP = 4000
MAXRABBITPOP = 5000

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    

    # rabbits reproduce with prob of 1.0 - (current pop of rabits / maximum pop of rabbits)
    for rabbit in range(CURRENTRABBITPOP):
        if CURRENTRABBITPOP in range(1001)[10:]:
            if random.random() < float(1.0 - (CURRENTRABBITPOP / float(MAXRABBITPOP))):
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
    
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    

    # TO DO
    for fox in range(CURRENTFOXPOP):
        
        foxKillsRabbitProb = CURRENTRABBITPOP / float(MAXRABBITPOP)
        
        
        if random.random() < foxKillsRabbitProb:
            if CURRENTFOXPOP <= CURRENTRABBITPOP and CURRENTFOXPOP > 10:
                    CURRENTRABBITPOP -= 1


                    if random.random() < 2/float(3):
                        CURRENTFOXPOP +=1
        else:
            if random.random() < 0.1:
                CURRENTFOXPOP -=1


            
def runSimulation(numSteps, plot = False):
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
        
    if plot:
        pylab.figure()


        pylab.xlabel('Time steps')
        pylab.ylabel('Number of animals')

        pylab.plot(rabbit_populations, "-b", label = "rabbits")
        pylab.plot(fox_populations, "-r", label = "Foxes")
        
        pylab.legend(loc = "lower right")
        pylab.title("Max pop in forrest:" + str(MAXRABBITPOP))

        pylab.show()

        
        
    return (rabbit_populations,fox_populations)
    
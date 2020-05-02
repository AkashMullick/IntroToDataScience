import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    results = []
    for i in range(numTrials):
        bucket = ['R', 'R', 'R', 'G', 'G', 'G']
        draws = []
        for i in range(3):
            choice = random.choice(bucket)
            draws.append(choice)
            bucket.remove(choice)
        results.append(draws)
    counter = 0
    for k in results:
        if k[0] == k[1] == k[2]:
            counter += 1
    return counter/float(numTrials)

print(noReplacementSimulation(1000))
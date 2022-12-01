#!/usr/bin/python
import random
class VoseAliasSampler(object):
    """Implementation of Vose-Alias Sampler based on http://www.keithschwarz.com/darts-dice-coins/)"""

    def __init__(self, dist):
        """ (VoseAlias, dict) -> NoneType """
        self.dist = dist
        self.symbols = list(dist)
        self.initialize()
        
        
        
    #Initialization Step
    def initialize(self):
        #Generate probability and alias tables for the distribution
        n = len(self.dist)
        self.prob_table = {}   # probability table
        self.alias_table = {}  # alias table
        under_sample = [] # stack for scaled probabilities smaller than 1(probability under the average)
        over_sample = [] # stacks for scaled probabilities greater or equal to 1(probability above the average)

        # generate scaled probabilities and place into appropriate stacks
        for symbol, prob in self.dist.items():
            self.prob_table[symbol] = prob*n
            if self.prob_table[symbol] < 1:
                under_sample.append(symbol)
            else:
                over_sample.append(symbol)

        # Construct the probability and alias tables
        while under_sample and over_sample:
            under = under_sample.pop()
            over = over_sample.pop()

            self.alias_table[under] = over
            # Decrement the probability of the larger one by the appropriate amount.
            self.prob_table[over] = (self.prob_table[over] + self.prob_table[under]) - 1

            if self.prob_table[over] < 1:
                under_sample.append(over)
            else:
                over_sample.append(over)

        # At this point, everything is in one of the stacks, therefore the
        # remaining scaled probabilities should all be set to 1 and the stack should be emptied
        while over_sample:
            self.prob_table[over_sample.pop()] = 1

        while under_sample:
            self.prob_table[under_sample.pop()] = 1
          
    #Generation Step  
    def generate(self):
        # randomly pick slot of table_prob
        slot = random.choice(self.symbols)

        # pick appropriate value from slot
        rand = random.uniform(0,1)
        res = self.alias_table[slot] if  rand > self.prob_table[slot]  else slot
        return res 

    def sample(self, k):
        """ Return a sample of size k from the distribution."""
        return [self.generate() for i in range(k)]


def main():
    #sample test for sampler
    alphabet = dict(a=0.15,b=0.1,c=0.1,d=0.1,e=0.2,f=0.1,g=0.05,h=0.05,i=0.15)
    sampler = VoseAliasSampler(alphabet)
    samples = {s:0 for s in alphabet}
    for _sample in sampler.sample(1000):
        samples[_sample] += 1
    assert(samples == dict(a=150,b=100,c=100,d=100,e=200,f=100,g=50,h=50,i=150) )
    


if __name__ == "__main__":
    main()

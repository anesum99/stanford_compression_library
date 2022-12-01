# Milestone 


## Project Statement

Often, data is compressed once while the decoding is later done several times, probably by several users. 
In such cases, it is desirable that the decoding operation be as fast as possible. 
The current SCL implementation of rANS is slowed down by the binary search for the symbol from the cumulative frequency table. 
This project aims to reduce this compute complexity from Olog(M) to constant time per symbol using the Alias method and subsequently speed up the decoding process. 

## Literature Review
1. rANS with static probability distributions
 https://fgiesen.wordpress.com/2014/02/18/rans-with-static-probability-distributions/
 
 
 
 
2. Understanding ANS - 10 - Optimal normalized counts 
 http://cbloomrants.blogspot.com/2014/02/02-11-14-understanding-ans-10.html
 
 
 
 
3. Lab Notes: The Alias Method for Sampling from Discrete Distributions 
   http://pandasthumb.org/archives/2012/08/lab-notes-the-a.html



4. Darts, Dice, and Coins: Sampling from a Discrete Distribution
   https://www.keithschwarz.com/darts-dice-coins/


## Alias Method for Sampling





### Sampler Pseudo-code

Initialization Step:
  -Create arrays alias and and scaled prob tables of size n each.
  -Create two bucket lists, under_sample and over_sample.
  -Multiply each probability by n to get the scaled probability.
  -For each scaled probability pi:
      -If pi<1,
        -add i to under_sample.
      -Otherwise (pi≥1), 
         -add i to over_sample.
  -While under_sample and over_sample are not empty:
      -Remove the first element, u, from under_sample
      -Remove the first element, o, from over_sample; 
      -Set alias[u]= o
      -Set prob[o] = (prob[0]+prob[u])−1. 
      -If prob[o]<1
        -add u to under_sample.
      -else:
        -add g to oversample.
  -While under_sample is not empty:
      -Remove the first element,u from under_sample and set prob[u] to 1
  -While over_sample is not empty: 
      -Remove the first element,o from over_sample and set prob[o] to 1
 
Generation Step:
  -Generate a fair die roll i from an n-sided die; 
  -Flip a biased coin that comes up heads with probability prob[i].
  -If the coin comes up "heads," return i.
  -Else, return alias[i].


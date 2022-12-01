# Milestone 


## Project Statement

Often, data is compressed once while the decoding is later done several times, probably by several<br/> 
users. In such cases, it is desirable that the decoding operation be as fast as possible.<br/> 
The current SCL implementation of rANS is slowed down by the binary search for the symbol from the <br/>
cumulative frequency table. This project aims to reduce this compute complexity from Olog(M) to <br/>
constant time per symbol using the Alias method and subsequently speed up the decoding process. <br/> 

## Literature Review
1. rANS with static probability distributions
 https://fgiesen.wordpress.com/2014/02/18/rans-with-static-probability-distributions/
 
 This paper gives an overview of rANS and its limitations. It then proposes the use of<br/>
 tables for faster decoding.
 
 
2. Understanding ANS - 10 - Optimal normalized counts 
 http://cbloomrants.blogspot.com/2014/02/02-11-14-understanding-ans-10.html
 
 This paper provides insights on efficiently creating more accurate scaled probabilities<br/>
 required for rANS and other aritmatic coders in general to allow for lossless compression and <br/>
 decompression. 
 
 
3. Lab Notes: The Alias Method for Sampling from Discrete Distributions 
   http://pandasthumb.org/archives/2012/08/lab-notes-the-a.html



4. Darts, Dice, and Coins: Sampling from a Discrete Distribution
   https://www.keithschwarz.com/darts-dice-coins/
   
   This paper gives a thorough guide to several implementations of the alias sampling algorithm, including
   the optimal one implemented for this project.


## Alias Method for Sampling
The alias method allows constant time sampling from a static distribution.<br /> 
Since we are mainly concerned with decoding speed, we can relax our speed <br/>
requirements in the decoding stage, an alias table <br />
can be generated once at the encoder and be passed on together with the scaled <br />
scaled probability table, to the decoder. The tables are generated at O(n) where<br /> 
n is the length of the distribution. This then allows constant time decoding per <br/>
symbol and overal linear time for the entire decoding.<br />

As a result, the encoder simply needs to be modified to incoporate the table generation<br/>
while the decoder needs to accept the tables as input. 




### Sampler Pseudo-code

Initialization Step:<br />
 -Create arrays alias and and scaled prob tables of size n each.<br />
 -Create two bucket lists, under_sample and over_sample.<br />
  -Multiply each probability by n to get the scaled probability.<br />
  -For each scaled probability pi:<br />
      -If pi<1,<br />
        -add i to under_sample.<br />
      -Otherwise (pi≥1),<br />
         -add i to over_sample.<br />
  -While under_sample and over_sample are not empty:<br />
      -Remove the first element, u, from under_sample<br />
      -Remove the first element, o, from over_sample; <br />
      -Set alias[u]= o
      -Set prob[o] = (prob[0]+prob[u])−1. <br />
      -If prob[o]<1<br />
        -add u to under_sample.<br />
      -else:<br />
        -add u to oversample.<br />
  -While under_sample is not empty:<br />
      -Remove the first element, u, from under_sample and set prob[u] to 1<br />
  -While over_sample is not empty: <br />
      -Remove the first element, o, from over_sample and set prob[o] to 1<br />
 
Generation Step:<br />
  -Generate a fair die roll i from an n-sided die; <br />
  -Flip a biased coin that comes up heads with probability prob[i].<br />
  -If the coin comes up "heads," return i.<br />
  -Else, return alias[i].<br />
  
The full implementation and testing code can be found at https://github.com/anesum99/stanford_compression_library/blob/main/rANS_alias/vose_alias_sampler.py


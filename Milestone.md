# Milestone
## Project Statement
Project Overview
Often, data is compressed once while the decoding is later done several times, probably by several users. 
In such cases, it is desirable that the decoding operation be as fast as possible. 
The current SCL implementation of rANS is slowed down by the binary search for the symbol from the cumulative frequency table. 
This project aims to reduce this compute complexity from Olog(M) to constant time per symbol using the Alias method and subsequently speed up the decoding process. 

## Literature Review
## Alias Method for Sampling
### Pseudo-code


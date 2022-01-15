# Password evolution algorithm
An evolution algorithm to find an ASCII password. CURRENTLY UNFINISHED 

![example-gif](https://imgur.com/5Np8TVS)

## Process
After the first creation of the population. Then in the main loop mutations have
a 1% chance in every unit to happen. Then the bottom 50% get purged and the remaining
units pair up and reproduce. Then new units get randomly introduced at the end.

TLDR: creation > [mutation > bottom 50% die > reproduction > new units introduced]

## Setup
Install plotly 

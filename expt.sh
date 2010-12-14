#!/usr/bin/env bash
for top_pct in $(seq .1 .1 .3)
do
  for pct_twts in $(seq .0001 .0002 .0011)
  do 
    for iters in $(seq 1 1 5)
    do 
      python tweetParser.py $top_pct $pct_twts $iters
    done
  done
done

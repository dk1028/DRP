# DRP
directed reading program 

## Questions
Why does this estimator lower the variance compared to the original? 

Can you convince yourself that using delta and estimating on the unlabeled data makes sense (say with a picture). 

What is the subgradient for convex problem (definition)? 


This is the link for the latex file on overleaf: 
https://www.overleaf.com/9251721923hwfftnmjzggd#46e00b

## Goals Jan 31
- fix labeled data n = 100, see how the accuracy of the prediction effects the prediction powered inference. What happens when it is 100% accurate or 80% accurate etc.

- Try to work through the mathematics to understand why the coverage probability for the prediction powered inference is still bounded by alpha. That is is the confidence interval method "correct".

- Try to conceptualize the mathemaics. You can draw pictures (or understand the picture in the paper).

## Goals Feb 21
- read on convex optimization part (understand the algorithms) and understand how the algorithm reaches the optimal PP solution
- try to run a simulation where you mask 90% of the data, and use synthetic data for that part. How does PP inference perform depending on the accuracy of synthetic data? Compare to greedy regression or conservative regression. Repeat the simulated experiment 100-10000 times (up to you), and look at how often the confidence interval contains the true value (it should be the level of the confidence interval). (a lot of programming... make sure you have good plots).

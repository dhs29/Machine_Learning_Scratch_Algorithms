A Python program for optimizing the SVM hinge loss.
descent algorithm. The input and output should be the same as for
Least Squares Algorithm.

Test your program with the input data

1 1
1 2
1 3
3 1
3 2
3 3
50 2

and labels <to be provided>

0 0
0 1
0 2
1 3
1 4
1 5
1 6

Convert label 0 to -1 so that labels yi are either +1 or -1. This is
necessary for the gradient descent to work.

Use eta=.001 and stopping condition of while(abs(prevobj - obj) > .000000001).
Note the absolute value to account for instability in the gradient for hinge
loss. The converged solution with the hinge loss would be

w = (1.4605574252399243, -0.4595542036671061)
w0 = -2.0024682128830427
Dist to origin= 1.3078203832146862

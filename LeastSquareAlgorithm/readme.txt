A Python program that implements gradient descent for minimizing
the least squares loss. The input and output should be the same as for
nearest means and Naive-Bayes.

Test your program with the input data

0 0
0 1
1 0
1 1
10 10
10 11
11 10
11 11

and labels

0 0
0 1
0 2
0 3
1 4
1 5
1 6
1 7

Use eta=.001 and stopping condition of .001.

Your final w would be close to

w = 0.0889184232356005 0.0907934047968894

and distance of plane to origin would be about

abs(w0/||w||) = 7.09045903042441

If you change the stopping condition to 0, in other words
full convergence, then your final w would be

w = 0.0995024069539168 0.0995025677420564

and distance to origin

abs(w0/||w||) = 7.77817457926694
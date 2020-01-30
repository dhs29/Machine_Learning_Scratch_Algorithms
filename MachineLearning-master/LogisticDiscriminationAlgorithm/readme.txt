A Python program for the logistic discrimination gradient
descent algorithm. The input and output should be the same as for nearest
means and Naive-Bayes.

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

Do not convert negative labels to 0. They must remain 0 for the logistic
regression gradient descent.

Use eta=.01 and stopping condition of .0000001.

Your final w would be close to the one shown below. Note its similarity to
the perceptron output.

w = 0.957672135162093 0.956767618860693
||w||=1.35371348333622
distance to origin = -6.83744723331703

You may also try the data

1 2
2 1
2 2
2 3
4 1
4 2
4 3
50 2

and labels

0 0
0 1
0 2
0 3
1 4
1 5
1 6
1 7

For this example the output would be similar to the one below

w = 6.77850714487713 -1.06370810572314
||w||=6.86146005215591
distance to origin = -2.60844880003425
A Python program that determines the column with the
best split for the CART decision tree algorithm. (don't
have to write the CART algorithm in its entirety.)
A program that will traverse all columns in the
data and output the column and the threshold that gives the
lowest gini index.

The input should be the data file and labels as in previous
assignments. The output is the column number k and the split
value s.

We will test it on a simple example to determine if your program
gives the correct output. Test your program with a simple XOR example.


High level pseudocode:

    (1) For each column j:

	(1) Find the value that gives the best gini split of
	the data d into a partition of two sets

	(2) To evaluate the gini of a split use the formula

	gini = (lsize/rows)*(lp/lsize)*(1 - lp/lsize) + (rsize/rows)*(rp/rsize)*(1 - rp/rsize);

	where lsize is the size of the left partition, lp is the
	proportion of -1 labels in the left partition, rsize is the
	size of the right partition, rp is the proportion of -1
	labels in the right partition, and rows is the total number of
	datapoints in the dataset d (passed to the function)

    (2) Let column k give the best split s. Output k and s.

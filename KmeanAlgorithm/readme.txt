A Python program to output a k-means clustering. This program
would have similar structure to the nearest means program.

Follow the pseudocode given bellow.
1. Initialize: assign xi to C1 or C2 with equal probability and compute means:
    or assign some random point to m1 and m2(if k=2; if k=3 then m1 m2 m3)
2. Recompute clusters: assign xi to C1 if ||xi-m1||<||xi-m2||, otherwise assign to C2
3. Recompute means m1 and m2 (by step 2 we will get 2 clusters with some point)
4. Compute objective: difference between old mean and new mean from step 3.(this gives distance)
5. Compute objective of new clustering. If difference(difference between old means and new means) is smaller than
stopping condition(lets say 0.001) then stop, otherwise go to step 2.


The input to your program is a dataset and number of cluster k.
The output is in the same format of label files we have been using
in the course. So if the clustering is C0 = {0, 2, 3}, C1 = {1, 4}
and C2 = {5} then the output would be

0 0
1 1
0 2
0 3
1 4
2 5
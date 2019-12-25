# PLA
 Implement of PLA (感知机算法)
## generate data
Run the Program [DataEmit.py](DataEmit.py).
And the input should be like ：```DataEmit [w0,w1,w2] m n```
[w0 w1 w2] is the weight vector w.
m is the number of points with label “+”.
n is the number of points with label “-“.  
And the generated data will save in the file 'train.txt'
if u input :```DataEmit [w0,w1,w2] m n plot```, then the program will draw the line and the nodes
## PLA
Run the Program [PLA.py](PLA.py).
And the input should be like ：`PLA train.txt`
train.txt is the data file's name

python version: python3.7.2
package: numpy random matplotlib
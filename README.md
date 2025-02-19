## DSA Formative
This project allows you to perform basic operations on sparse matrices using Python. A sparse matrix is a matrix where most of the elements are zero, and we store only the non-zero values to save memory. The operations that are available are addition, substraction and multiplication.

*How it works:*
-it's important to understand the general conditions for each matrix operation and how it works usually: 
for addition/subtraction: You need the matrices to have the same size/dimensions (same number of rows and columns)
for multiplication: You need The number of columns in the first matrix to be equal to the number of rows in the second matrix.

-So the conditions for this app are: 
1.You can add or subtract matrices of any size. The operation will work by trimming the larger matrix to match the size of the smaller one. For example, if one matrix is 3x3 and the other is 2x2, the operation will only happen up to the size of the 2x2 matrix. Any extra rows or columns in the larger matrix are ignored.

2.This operation only works if the number of columns in the first matrix matches the number of rows in the second matrix. If this condition is not met, multiplication will not work. It's up to  the user to make sure the matrices meet this condition when performing multiplication.

*How to use it:*
-You need to have your input matrices saved in a .txt file, and put the file path in the code accordingly
-After preparing the matrices, you can choose the operation you want to perform:
Type 1 for Addition.
Type 2 for Subtraction.
Type 3 for Multiplication.
The result will be saved in a new file, like sum.txt, difference.txt, or product.txt, depending on what operation you choose.

*Challenges i faced*
-Initially, I used lists to store the matrices. However, I encountered errors when working with large files because lists consumed too much memory. To overcome this, I switched to using dictionaries to store the matrix values. This made the program more efficient.

-Initially, both addition and subtraction operations also faced a value error due to mismatched matrix sizes. The problem came from matrices of different sizes which i noticed by testing with matrix files that had similar sizes and worked. and I used a  feature that tims by ignoring the larger matrix extras to match the size of the smaller one. 

-The matrix multiplication operation only works if the general condition for matrix multiplication is met. Specifically, the number of columns in the first matrix must match the number of rows in the second matrix. It is up to the user to ensure that the matrices they provide follow this rule. If the condition is not met, multiplication will not be possible. I wasnt able to find a solution for this.

shout out to https://www.geeksforgeeks.org/sparse-matrix-representations-using-list-lists-dictionary-keys/ 

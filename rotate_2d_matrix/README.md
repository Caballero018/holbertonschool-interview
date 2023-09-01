# Rotate 2D Matrix 90 Degrees Clockwise

This Python function, rotate_2d_matrix(matrix), takes an n x n 2D matrix as input and rotates it 90 degrees clockwise in-place. This means that the original matrix will be modified, and the function doesn't return anything.

## Usage
You can use this function to rotate a 2D matrix as follows:

~~~
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)

# The matrix will now be rotated 90 degrees clockwise:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]

~~~

## Parameters

* **matrix**: This is the input 2D matrix that you want to rotate. It should have dimensions **n x n**, where **n** is the number of rows and columns, and it should not be empty.

## How it Works

1. First, the function transposes the matrix. Transposing a matrix means swapping elements across its main diagonal. This effectively turns rows into columns and vice versa.

2. After transposing, the function reverses each row of the matrix. This step rotates the matrix 90 degrees clockwise.

By following these two steps, the input matrix will be rotated 90 degrees clockwise in-place.

Feel free to use this function to rotate your 2D matrices as needed.
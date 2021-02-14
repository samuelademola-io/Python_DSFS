#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:05:11 2021

@author: damascus
"""

# %%

# LInear Algebra: Vectors
from typing import Callable
from typing import Tuple
import math
from typing import List

Vector = List[float]

height_weight_age = [70,    # inches,
                     170,   # pounds,
                     40]   # years

grades = [95,   # exam1
          80,   # exam2
          75,   # exam3
          62]  # exam4

# %%

# adding 2 Vectors


def add(v: Vector, w: Vector) -> Vector:
    """ Adds corresponding elements """
    assert len(v) == len(w), "Vectors must be in the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

# %%
# subtracting 2 Vectors


def substract(v: Vector, w: Vector) -> Vector:
    """ Subtracts corresponding elements """
    assert len(v) == len(w), "Vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert substract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

# %%
# Sum of Vectors


def vector_sum(vectors: List[Vector]) -> Vector:
    """ Sums all corresponding elements """
    # check that vectors is not empty
    assert vectors, "no vectors provided"

    # check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the -the element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

# %%
# Multiplying a vector by a scalar


def scalar_mutliply(c: float, v: Vector) -> Vector:
    """ Multiplies every element by c """
    return [c * v_i for v_i in v]


assert scalar_mutliply(2, [1, 2, 3]) == [2, 4, 6]

# %%
# Finding the mean of a vector


def vector_mean(vectors: List[Vector]) -> Vector:
    """ Computes the element-wise average """
    n = len(vectors)
    return scalar_mutliply(1/n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

# %%

# Dot Product of a Vector


def dot(v: Vector, w: Vector) -> float:
    """ Computes v_1 * w_1 + ... + v_n * w_n """
    assert len(v) == len(w), "vetors must be the same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32              # 1 * 4 + 2 * 5 + 3 * 6

# %%

# Compute a vector's Sum of Squares


def sum_of_squares(v: Vector) -> float:
    """ Returns v_1 * v_1 ... + v_n * v_n """
    return dot(v, v)


assert sum_of_squares([1, 2, 3]) == 14      # 1 * 1 + 2 * 2 + 3 * 3

# %%


def magnitude(v: Vector) -> float:
    """ Returns the magnitude (or length) pf v """
    return math.sqrt(sum_of_squares(v))  # math.sqrt is a square root function


assert magnitude([3, 4]) == 5

# %%

# Distance between 2 vectors
# https://math.stackexchange.com/questions/2615367/linear-algebra-find-distance-between-points-by-first-finding-vector


def squared_distance(v: Vector, w: Vector) -> float:
    """ Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2 """
    return sum_of_squares(substract(v, w))

# Different way


def distance(v: Vector, w: Vector) -> float:
    """ Computes the distance between v and w """
    return math.sqrt(squared_distance(v, w))

# %%

# LInear Algebra: Matrix
# Another type of Alias


Matrix = List[List[float]]

# A has 2 rows and 3 columns
A = [[1, 2, 3],
     [4, 5, 6]]

# B has 3 rows and 2 columns
B = [[1, 2],
     [3, 4],
     [5, 6]]

print(A[0])
print(B[0])


def shape(A: Matrix) -> Tuple[int, int]:
    """ Returns (# of rows of A, # of coluns of A) """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0       # nnumber of elements in 1st row
    return num_rows, num_cols


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)      # 2 rows, 3 columns

# %%


def get_rows(A: Matrix, i: int) -> Vector:
    """ Returns the i-th row of A (as a Vector) """
    # A[i] is alread the ith row
    return A[i]


def get_columns(A: Matrix, j: int) -> Vector:
    """ Returns the j-th column of A (as a Vector) """
    # Jth element of row A_i, for each row A_i
    return [A_i[j] for A_i in A]

 # %%


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    """ Returns a num_rows x cum_cols matrix whose (i, j).th entry is entry_fn(i, j) """
    # given i, creae a list.  [entry_fn(i, 0), ...] create one list for each
    return[[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identify_matrix(n: int) -> Matrix:
    """ Returns the n x n identify matrix """
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identify_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# user 0, 1, 2, 3, 4, 5, 6, 7, 8. 9

friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],            # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],            # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],            # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],            # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],            # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],            # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],            # user 6
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],            # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],            # user 8
                 [0, 1, 1, 0, 0, 0, 0, 0, 1, 0]]            # user 9

assert friend_matrix[0][2] == 1, "0 and 2 are freinds"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"

# only need to look at one row
friends_of_five = [i for i, is_friend in enumerate(
    friend_matrix[5]) if is_friend]

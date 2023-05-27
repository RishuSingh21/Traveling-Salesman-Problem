#!/usr/bin/env python
# coding: utf-8

# In[5]:


sol = 0


def valid_spot(board, row, col, dim):
    for i in range(row):
        if board[i][col][dim] == 1:
            return False

    # x-y plane
    i = row
    j = col
    k = dim
    while i >= 0 and j >= 0:
        if board[i][j][k] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    k = dim
    while i >= 0 and j < len(board):
        if board[i][j][k] == 1:
            return False
        i -= 1
        j += 1

    # y-z plane
    i = row
    j = col
    k = dim
    while j >= 0 and k >=0:
        if board[i][j][k] == 1:
            return False
        j -= 1
        k -= 1

    i = row
    j = col
    k = dim
    while j >= 0 and k < len(board):
        if board[i][j][k] == 1:
            return False
        j -= 1
        k += 1

    # z-x plane
    i = row
    j = col
    k = dim
    while i >= 0 and k >=0:
        if board[i][j][k] == 1:
            return False
        i -= 1
        k -= 1

    i = row
    j = col
    k = dim
    while i >= 0 and k <len(board):
        if board[i][j][k] == 1:
            return False
        i -= 1
        k += 1

    # all-planes
    i = row
    j = col
    k = dim
    while i >= 0 and j >= 0 and k >=0:
        if board[i][j][k] == 1:
            return False
        i -= 1
        j -= 1
        k -= 1

    i = row
    j = col
    k = dim
    while i >= 0 and j >= 0 and k <len(board):
        if board[i][j][k] == 1:
            return False
        i -= 1
        j -= 1
        k += 1

    i = row
    j = col
    k = dim
    while i >= 0 and j < len(board) and k >= 0:
        if board[i][j][k] == 1:
            return False
        i -= 1
        j += 1
        k -= 1

    i = row
    j = col
    k = dim
    while i >= 0 and j < len(board) and k < len(board):
        if board[i][j][k] == 1:
            return False
        i -= 1
        j += 1
        k += 1

    return True


def n_queen(board, row, col):
    global sol

    if row == len(board):
        sol += 1
        return

    elif col == len(board):
        n_queen(board, row + 1, 0)

    else:
        for i in range(len(board)):
            if valid_spot(board, row, col, i):
                board[row][col][i] = 1
                n_queen(board=board, row=row,  col=col+1)
                board[row][col][i] = 0


def run(n):
    global sol
    for i in n:
        sol = 0
        board = [[[0 for j in range(i)] for k in range(i)] for l in range(i)]
        n_queen(board, 0, 1)
        print(f'Number of solutions for n={i} is {sol * i ** 2}')


if __name__ == "__main__" :
    n = [2, 3, 4, 5]

    run(n)


# In[ ]:





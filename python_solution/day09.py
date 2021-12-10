# https://adventofcode.com/2021/day/8
from collections import Counter
from util import read
import numpy as np


def get_lowest_points(questions_mat: np.matrix):
    quetions_mat_left_one = np.append(
        questions_mat[:, 1:], values=questions_mat[:, -1] + 1, axis=1
    )

    quetions_mat_right_one = np.append(
        questions_mat[:, 0] + 1, values=questions_mat[:, :-1], axis=1
    )
    quetions_mat_up_one = np.append(
        questions_mat[0] + 1, values=questions_mat[:-1], axis=0
    )
    quetions_mat_down_one = np.append(
        questions_mat[1:], values=questions_mat[-1] + 1, axis=0
    )
    logical_mat = np.logical_and(
        np.logical_and(
            (questions_mat - quetions_mat_down_one) < 0,
            (questions_mat - quetions_mat_up_one) < 0,
        ),
        np.logical_and(
            (questions_mat - quetions_mat_right_one) < 0,
            (questions_mat - quetions_mat_left_one) < 0,
        ),
    )
    return logical_mat


def Q1_solution(questions_mat: np.matrix):
    logical_mat = get_lowest_points(questions_mat=questions_mat)
    return (questions_mat[logical_mat] + 1).sum()


def Q2_solution(question_mat: np.matrix):
    group_number = 1
    row_n, col_n = question_mat.shape
    basins_matrix = np.zeros(shape=question_mat.shape)
    for i in range(row_n):
        for j in range(col_n):
            if question_mat[i, j] == 9:
                group_number += 1
            else:
                if basins_matrix[i - 1, j] == 0:
                    basins_matrix[i, j] = group_number
                    if basins_matrix[i, j - 1] != 0:
                        basins_matrix[i, j] = basins_matrix[i, j - 1]
                else:
                    in_group = basins_matrix[i - 1, j]
                    basins_matrix[i, j] = in_group
                    if basins_matrix[i, j - 1] != in_group:
                        a = 1
                        while True:
                            if basins_matrix[i, j - a] == 0:
                                break
                            basins_matrix[i, j - a] = in_group
                            a += 1
    return basins_matrix


if __name__ == "__main__":
    raw_data = read(9, example=False)
    questions_mat: np.matrix = np.matrix(
        [[int(word) for word in datum] for datum in raw_data]
    )
    # Q1_ans = Q1_solution(quetions_mat)
    # print(Q1_ans)
    # print(np.where(get_lowest_points(questions_mat=quetions_mat)))
    AnsCounter: Counter[int] = Counter()
    Q2_mat = Q2_solution(questions_mat)
    for col in range(len(Q2_mat)):
        print(Q2_mat[col])
        AnsCounter += Counter(Q2_mat[col])

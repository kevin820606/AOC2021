from util import read
import numpy as np

raw_data = read(9, example=False)
quetions_mat = np.matrix([[int(word) for word in datum] for datum in raw_data])
quetions_mat_left_one = np.append(
    quetions_mat[:, 1:], values=quetions_mat[:, -1] + 1, axis=1
)

quetions_mat_right_one = np.append(
    quetions_mat[:, 0] + 1, values=quetions_mat[:, :-1], axis=1
)
quetions_mat_up_one = np.append(quetions_mat[0] + 1, values=quetions_mat[:-1], axis=0)
quetions_mat_down_one = np.append(quetions_mat[1:], values=quetions_mat[-1] + 1, axis=0)
print(quetions_mat)
print(quetions_mat_down_one)
print(quetions_mat_up_one)
print(quetions_mat_left_one)
print(quetions_mat_right_one)
logical_mat = np.logical_and(
    np.logical_and(
        (quetions_mat - quetions_mat_down_one) < 0,
        (quetions_mat - quetions_mat_up_one) < 0,
    ),
    np.logical_and(
        (quetions_mat - quetions_mat_right_one) < 0,
        (quetions_mat - quetions_mat_left_one) < 0,
    ),
)
print((quetions_mat[logical_mat] + 1).sum())

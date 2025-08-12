import numpy as np
from numpy.typing import NDArray

def solution(w: NDArray[np.float64], x: NDArray[np.float64], y_true: float, lambda_: float) -> float:
    x = np.array(x)
    w = np.array(w)

    if x.shape[0] == 0:
        return np.nan

    y_pred = x @ w

    ridge_loss = np.square(y_pred - y_true).sum() + lambda_ * np.square(w).sum()

    return ridge_loss

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution([1, 2], [1, 1], 4, 1))


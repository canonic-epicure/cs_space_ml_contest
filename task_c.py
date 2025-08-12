import math

def solution(sigma1: int, sigma2: int) -> float:
    return 1 / 2 + 1 / math.pi * math.asin(sigma1 / math.sqrt(sigma1 ** 2 + sigma2 ** 2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution(1, 1))

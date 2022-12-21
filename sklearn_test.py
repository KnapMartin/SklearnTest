from sklearn.datasets import load_digits
from traceback import print_exc

import matplotlib.pyplot as plt

def test():
    digits = load_digits()
    print("data shape:", digits.data.shape)


if __name__ == "__main__":
    try:
        test()
    except:
        print_exc()
        raise Exception("Err!")

import numpy as np

class Relu:
    def __init__(self):
        self.mask = None

    def forward(self,x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx

# 이해를 위한 확인용
if __name__ == "__main__":
    x = np.array([[1.0, -0.5],[-2.0, 3.0]])
    print(x)

    mask = (x <= 0)
    print(mask)

    out = x.copy()
    out[mask] = 0
    print(out)





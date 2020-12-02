import unittest
from rand7 import rand7
from collections import Counter
import matplotlib.pyplot as plt
import random as r
import numpy as np

class Test_Case_Rand7(unittest.TestCase):
    def test_rand7(self):
        ans = []
        for i in range(10000):
            ans.append(rand7())
        true = []
        for i in range(10000):
            true.append(r.randint(0,6))
        plt.hist(ans)
        plt.savefig("histo_ans.png")
        plt.cla()
        plt.hist(true)
        plt.savefig("histo_true.png")
        plt.cla()
        for i in range(7):
            self.assertAlmostEqual(sum([1 for x in ans if x == i]), sum([1 for x in true if x == 1]), delta=100)

if __name__ == '__main__':
    unittest.main()
import torch
from torch.testing._internal.common_utils import run_tests, TestCase

class TestBits16(TestCase):
    def test(self):
        # unsafe reinterpret cast from one type to another
        t = torch.zeros(20, dtype=torch.int16).view(torch.bits16)
        # define the factory function for empty directly on bits
        t1 = torch.empty(20, dtype=torch.bits16)

        # implement uint16 printer. unsafely coerce to int16, detect if it's
        # negative and determine twos complement

        # barebones mechanism on bits, or a clear guidance about how to go about
        # implementing the subclass

        # defualt printer for bits, something like hex notation



if __name__ == '__main__':
    run_tests()

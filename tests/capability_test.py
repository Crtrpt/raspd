import unittest
import capability.cpu_times as capability;

class TestCapability(unittest.TestCase):

    def test_cpu_times(self):
        c=capability.cpu_times();
        print(c.run());
        


if __name__ == '__main__':
    unittest.main()
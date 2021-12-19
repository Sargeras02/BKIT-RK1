import unittest
import RK

class TestCompOS(unittest.TestCase):
    def test_t1(self):
        excpRes = [('Сидоров', 110000, 'Windows'), ('Петров', 33000, 'Альфа-ОС'), ('Остров', 58000, 'Linux')]
        self.assertEqual(RK.task1(), excpRes)

    def test_t2(self):
        excpRes = [('macOS', 120000.0), ('Windows', 88000.0), ('Linux', 57000.0), ('Альфа-ОС', 33000.0)]
        self.assertEqual(RK.task2(), excpRes)

    def test_t3(self):
        excpRes = {'Альфа-ОС': ['Петров', 'Афанасьев', 'Кощеев']}
        self.assertEqual(RK.task3(), excpRes)

if __name__ == "__main__":
    unittest.main()
import unittest

from it import It
import operator as op


class ItTestCase(unittest.TestCase):
    def assertItEqual(self, a, b):
        return self.assertEqual(list(a), list(b))


    def test_map(self):
        self.assertItEqual(It([0, 1]).map(lambda x: x + 1),
                         [1, 2])
        

    def test_filter(self):
        self.assertItEqual(It([0, 1]).filter(bool),
                         [1])


    def test_reduce(self):
        self.assertEqual(It([0, 1]).reduce(op.mul), 0)


    def test_flatten(self):
        self.assertItEqual(It(([0, 1], range(2, 4))).flatten(), 
                           [0, 1, 2, 3])


    def test_flatten_string(self):
        self.assertEqual(It(['a' 'b']).flatten_string(), 'ab')


    def test_reject(self):
        self.assertItEqual(It([0, 1]).reject(bool),
                         [0])


    def test_find(self):
        self.assertEqual(It([0, 1]).find(bool), 1)


    def test_all(self):
        self.assertEqual(It([0, 1]).all(), False)


    def test_any(self):
        self.assertEqual(It([0, 1]).any(), True)


    def test_include(self):
        self.assertEqual(It([0, 1]).include(1), True)


    def test_invoke(self):
        self.assertItEqual(It([[0, 1]]).invoke('pop'), [[0]])


    def test_pluck(self):
        self.assertItEqual(It([0, 1]).pluck('denominator'), [1, 1])


    def test_max(self):
        self.assertEqual(It([0, 1]).max(), 1)


    def test_min(self):
        self.assertEqual(It([0, 1]).min(), 0)


    def test_sort(self):
        self.assertEqual(It([1,0]).sort(), [0, 1])


    def test_sort(self):
        self.assertEqual(It([1,0]).sort(), [0, 1])


    def test_len(self):
        self.assertEqual(len(It([1,0])), 2)


    def test_list(self):
        self.assertEqual(It(xrange(0, 1)).list(), [0])


    def test_set(self):
        self.assertEqual(It(xrange(0, 1)).set(), set([0]))


    def test_set(self):
        self.assertEqual(It(xrange(0, 1)).set(), set([0]))


class ItChainTestCase(unittest.TestCase):
    def assertItEqual(self, a, b):
        return self.assertEqual(list(a), list(b))


    def test_map(self):
        self.assertItEqual(It([0, 1]).chain().map(lambda x: x + 1).value(),
                         [1, 2])
        

    def test_filter(self):
        self.assertItEqual(It([0, 1]).chain().filter(bool).value(),
                         [1])


    def test_reduce(self):
        self.assertEqual(It([0, 1]).chain().reduce(op.mul).value(), 0)


    def test_flatten(self):
        self.assertItEqual(It(([0, 1], range(2, 4))).chain().flatten().value(), 
                           [0, 1, 2, 3])


    def test_flatten_string(self):
        self.assertEqual(It(['a' 'b']).chain().flatten_string().value(), 'ab')


    def test_reject(self):
        self.assertItEqual(It([0, 1]).chain().reject(bool).value(),
                         [0])


    def test_find(self):
        self.assertEqual(It([0, 1]).chain().find(bool).value(), 1)


    def test_all(self):
        self.assertEqual(It([0, 1]).chain().all().value(), False)


    def test_any(self):
        self.assertEqual(It([0, 1]).chain().any().value(), True)


    def test_include(self):
        self.assertEqual(It([0, 1]).chain().include(1).value(), True)


    def test_invoke(self):
        self.assertItEqual(It([[0, 1]]).chain().invoke('pop').value(), [[0]])


    def test_pluck(self):
        self.assertItEqual(It([0, 1]).chain().pluck('denominator').value(), [1, 1])


    def test_max(self):
        self.assertEqual(It([0, 1]).chain().max().value(), 1)


    def test_min(self):
        self.assertEqual(It([0, 1]).chain().min().value(), 0)


    def test_sort(self):
        self.assertEqual(It([1,0]).chain().sort().value(), [0, 1])


    def test_sort(self):
        self.assertEqual(It([1,0]).chain().sort().value(), [0, 1])


    def test_list(self):
        self.assertEqual(It(xrange(0, 1)).chain().list().value(), [0])


    def test_set(self):
        self.assertEqual(It(xrange(0, 1)).chain().set().value(), set([0]))



if __name__ == "__main__":
    unittest.main()
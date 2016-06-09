from unittest import TestCase
from bite.iterator import MemoryCachingAdapter
from bite.func import prev

class TestMemoryCachingAdaptor(TestCase):
    def setUp(self):
        self.it = MemoryCachingAdapter(iter('abc'))

    def test_prev(self):
        next(self.it)
        next(self.it)
        next(self.it)
        self.assertEqual(prev(self.it), 'b')
        self.assertEqual(prev(self.it), 'a')
        with self.assertRaises(StopIteration):
            print(prev(self.it))

    def test_next(self):
        self.assertEqual(next(self.it), 'a')
        self.assertEqual(next(self.it), 'b')
        self.assertEqual(next(self.it), 'c')
        with self.assertRaises(StopIteration):
            next(self.it)

    def test_next_prev(self):
        self.assertEqual(next(self.it), 'a')
        self.assertEqual(next(self.it), 'b')
        self.assertEqual(prev(self.it), 'a')
        self.assertEqual(next(self.it), 'b')

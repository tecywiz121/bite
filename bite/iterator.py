from abc import ABCMeta, abstractmethod

class CachingAdapter(metaclass=ABCMeta):
    def __init__(self, backing):
        self._backing = backing

    @abstractmethod
    def _store(self, v):
        pass

    @abstractmethod
    def _move_down(self):
        pass

    @abstractmethod
    def _move_up(self):
        pass

    @property
    @abstractmethod
    def _at_head(self):
        return False

    @property
    @abstractmethod
    def _at_tail(self):
        return False

    def __next__(self):
        if self._at_tail:
            self._store(next(self._backing))
        return self._move_down()

    def __prev__(self):
        if self._at_head:
            raise StopIteration()
        return self._move_up()

class MemoryCachingAdapter(CachingAdapter):
    def __init__(self, backing):
        super(MemoryCachingAdapter, self).__init__(backing)
        self._storage = []
        self._position = -1

    @property
    def _at_head(self):
        return 0 >= self._position

    @property
    def _at_tail(self):
        return self._position >= (len(self._storage)-1)

    def _move_up(self):
        self._position -= 1
        return self._storage[self._position]

    def _move_down(self):
        self._position += 1
        return self._storage[self._position]

    def _store(self, v):
        self._storage += [v]

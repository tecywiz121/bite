def prev(iterator, *args):
    '''
    Retrieve the previous item from the iterator by calling its prev() method.
    If default is given, it is returned if the iterator is exhausted, otherwise
    StopIteration is raised.
    '''
    if not hasattr(iterator, '__prev__'):
        n = iterator.__class__.__name__
        raise TypeError('{} object is not a bidirectional iterator'.format(n))
    try:
        return iterator.__prev__()
    except StopIteration:
        if args:
            return args[0]
        else:
            raise

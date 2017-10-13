import inspect

class key_memoized(object):
    def __init__(self, func):
       self.func = func
       self.cache = {}

    def __call__(self, *args, **kwargs):
        key = self.key(args, kwargs)
        if key not in self.cache:
            self.cache[key] = self.func(*args, **kwargs)
        return self.cache[key]

    def normalize_args(self, args, kwargs):
        spec = inspect.getargs(self.func.__code__).args
        return dict(kwargs.items() + zip(spec, args))

    def key(self, args, kwargs):
        a = self.normalize_args(args, kwargs)
        return tuple(sorted(a.items()))

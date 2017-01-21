import os.path
from functools import wraps, singledispatch


def ext_dispatcher(func):
    func = singledispatch(func)

    @wraps(func)
    def wrapper(*args, **kw):
        ext = os.path.splitext(args[0])[1]
        if ext in func.registry:
            return func.registry[ext](*args, **kw)
        return func(*args, **kw)
    wrapper.register = func.register
    wrapper.dispatch = func.dispatch
    wrapper.registry = func.registry

    return wrapper

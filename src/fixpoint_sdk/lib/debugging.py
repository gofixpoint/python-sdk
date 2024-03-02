from dataclasses import dataclass
import functools
import os
import typing


def _is_debug_mode() -> bool:
    debugmode = os.environ.get('DEBUG', 'off').lower()
    return debugmode in ['on', 'true', '1']


def dprint(*args, **kwargs):
    if not _is_debug_mode():
        return
    print(*args, **kwargs) 


@dataclass
class FnIO:
    name: str
    args: typing.List[str]
    kwargs: typing.Dict[str, str]
    output: str

    def to_dict(self):
        return {
            'name': self.name,
            'args': self.args,
            'kwargs': self.kwargs,
            'output': self.output,
        }
    
    def log(self):
        print(self.to_dict())


def debug_log_function_io(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not _is_debug_mode():
            return func(*args, **kwargs)
        return _log_fn_io(func, *args, **kwargs)

    return wrapper


def log_function_io(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return _log_fn_io(func, *args, **kwargs)

    return wrapper


def _log_fn_io(func, *args, **kwargs):
    args_repr = [repr(a) for a in args]
    kwargs = {k: repr(v) for k, v in kwargs.items()}
    out = func(*args, **kwargs)
    out_repr = repr(out)
    fnio = FnIO(name=func.__name__, args=args_repr, kwargs=kwargs, output=out_repr)
    fnio.log()
    return out

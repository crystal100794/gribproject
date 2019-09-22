import functools

def try_run_x_times(x, fn):
    @functools.wraps(fn)
    def new_fn(*args, **kwargs):
        for i in range(x):
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                print(e)
                pass
        raise Exception
    return new_fn
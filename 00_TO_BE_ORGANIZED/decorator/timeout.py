from functools import wraps
from threading import Thread


def timeout(timeperiod):
    def decorate(method):
        @wraps(method)
        def wrapper(*args, **kwargs):
            res = [Exception(f"method {method.__name__} timeout {timeperiod} sec exceeded.")]

            def new_method():
                try:
                    res[0] = method(*args, **kwargs)
                except Exception as e:
                    res[0] = e
            
            t = Thread(target=new_method)
            t.daemon = True  # when main thread is over, it will force the chrildren to stop

            try:
                t.start()
                t.join(timeperiod)
            except Exception as e:
                raise e
            
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return decorate


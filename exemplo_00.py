from utils_log import log_decorator
from timer_decorator import time_measure_decorator
import time

# pydantic
# pandera


@time_measure_decorator
def soma(x, y):
    time.sleep(2)
    return x + y

print(soma(2,3))
print(soma(2,7))


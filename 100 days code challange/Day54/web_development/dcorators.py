import time

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(1)
#         function()
#     return wrapper_function

# @delay_decorator
# def say_hello():
#     print("hello")

current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"{func.__name__} run speed: {end_time - start_time}s")
    return result
  return wrapper

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()

slow_function()
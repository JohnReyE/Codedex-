# Define a decorator function
def my_decorator(func):
  def wrapper():
    print('Before function execution')
    func()
    print('After function execution')
  return wrapper

# Apply the decorator to a function
@my_decorator
def say_hello():
  print('Hello, decorators!')

# Call the decorated function
say_hello()
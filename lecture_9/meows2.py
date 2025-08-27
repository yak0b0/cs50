def meow(n: int) -> str:  # this is a type hint
    ''' 
    Meow n times. 
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: IF n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    '''  # - DOCSTRING
    return "meow\n" * n
# py -m mypy lecture_9/meows2.py  _ how to use mypy


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

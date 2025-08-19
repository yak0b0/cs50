class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cookies must be a non-negative int")
        if (self.size + n) > self.capacity:
            raise ValueError("Capacity exceeded")
        self._size += n
        return self._size

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cookies must be a non-negative int")
        if self.size < n:
            raise ValueError("You will have negative cookies left")
        self._size -= n
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size


jar_of_cookies = Jar(capacity=3)
jar_of_cookies.deposit(3)
print(jar_of_cookies)
jar_of_cookies.withdraw(1)
print(jar_of_cookies.capacity)
print(jar_of_cookies.size)

class Jar:
    def __init__(self, capacity=12):
        if capacity > 12 or capacity < 0:
            raise ValueError()
        self._capacity = capacity
        self._n = 0

    def __str__(self):
        cookie = ""
        for i in range(self._n):
            cookie = cookie + "🍪"
        return cookie

    def deposit(self, n):
        if self._n + n > self._capacity:
            raise ValueError()
        self._n += n

    def withdraw(self, n):
        if self._n - n < 0:
            raise ValueError()
        self._n -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("@capacity.setter error")
        self._capacity = capacity

    @property
    def size(self):
        return self._n
    @size.setter
    def size(self, n):
        if n > self.capacity:
            raise ValueError("@size.setter error")
        self._n = n

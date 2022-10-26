from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.length = n
        self._stream = [0 for i in range(n+2)]
        self._ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self._stream[idKey] = (idKey, value)
        if idKey == self._ptr:
            _values = []
            for i in range(self._ptr, self.length):
                if self._stream[self._ptr]:
                    self._ptr += 1
                    _values.append(self._stream[self._ptr][1])
                else:
                    break
            return _values

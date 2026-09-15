import threading

class BoundedCounter:
    """
    Approach: use a threading.Lock to make the check-then-increment
    atomic. Without the lock, two threads could both read value < max
    at the same time and both increment, exceeding max (a classic
    check-then-act race condition).
    Time: O(1) per call, Space: O(1).
    """
    def __init__(self, max_value: int):
        self._max = max_value
        self._value = 0
        self._lock = threading.Lock()

    def increment(self) -> bool:
        with self._lock:
            if self._value >= self._max:
                return False
            self._value += 1
            return True

    def value(self) -> int:
        with self._lock:
            return self._value

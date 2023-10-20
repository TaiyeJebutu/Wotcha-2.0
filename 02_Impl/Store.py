from GenericStore import GenericStoreInterface
from abc import ABC, abstractmethod
from queue import Queue
from threading import Lock


class Store(ABC, GenericStoreInterface):
    TIMEOUT = 1

    def __init__(self):
        self._queue = Queue()
        self._timeout = Store.TIMEOUT
        self._lock = Lock()

    def add(self, data):
        with self._lock:
            self._queue.put(data, block=True, timeout=self._timeout)

    def get(self):
        if not self._queue.empty():
            with self._lock:
                return self._queue.get(block=False, timeout=self._timeout)

    def get_all(self) -> list:
        result = []
        with self._lock:
            while not self._queue.empty():
                data = self._queue.get()
                result.append(data)

        return result

"""
Problem 5: Implement HashMap with addToKey / addToValue (Q4 candidate)
Slot: Q4 | Probability: 8-15%

Design a HashMap supporting these operations in O(1):
    insert(key, value)  — add or overwrite entry
    get(key)            — retrieve value for key (None if missing)
    exists(key)         — check if key present
    addToKey(delta)     — add delta to ALL keys in the map
    addToValue(delta)   — add delta to ALL values in the map

Naive approach (iterate over all entries for addToKey/addToValue) is O(n) per op
and causes TLE. The trick is to maintain two global offsets:
    key_offset    — accumulated delta applied to all keys
    value_offset  — accumulated delta applied to all values

Internally, keys and values are stored shifted by the current offset.
When inserting key k with value v, store: internal_key = k - key_offset,
                                           internal_val = v - value_offset
When reading key k: look up k - key_offset, return stored_val + value_offset.

Pattern: Lazy delta accumulator (offset tracking).
LeetCode equivalents: 706 Design HashMap, 1146 Snapshot Array
"""


class HashMap:
    def __init__(self) -> None:
        self._data: dict[int, int] = {}
        self._key_offset: int = 0
        self._val_offset: int = 0

    def insert(self, key: int, value: int) -> None:
        self._data[key - self._key_offset] = value - self._val_offset

    def get(self, key: int) -> "int | None":
        internal = key - self._key_offset
        if internal in self._data:
            return self._data[internal] + self._val_offset
        return None

    def exists(self, key: int) -> bool:
        return (key - self._key_offset) in self._data

    def addToKey(self, delta: int) -> None:
        self._key_offset += delta

    def addToValue(self, delta: int) -> None:
        self._val_offset += delta

    def keys(self) -> list[int]:
        return [k + self._key_offset for k in self._data]

    def items(self) -> list[tuple[int, int]]:
        return [
            (k + self._key_offset, v + self._val_offset)
            for k, v in self._data.items()
        ]

    def __repr__(self) -> str:
        return f"HashMap({dict(self.items())})"


def solution(queries: list[list]) -> list:
    """
    Process a list of queries and return results of 'get' operations.
    Query format: [op, *args]
        ["insert", key, value]
        ["get", key]         -> appends result to output
        ["addToKey", delta]
        ["addToValue", delta]
    """
    hm = HashMap()
    results = []
    for q in queries:
        op = q[0]
        if op == "insert":
            hm.insert(q[1], q[2])
        elif op == "get":
            results.append(hm.get(q[1]))
        elif op == "addToKey":
            hm.addToKey(q[1])
        elif op == "addToValue":
            hm.addToValue(q[1])
    return results


if __name__ == "__main__":
    hm = HashMap()
    hm.insert(1, 10)
    hm.insert(2, 20)
    hm.insert(3, 30)
    print(f"Initial: {hm}")

    hm.addToValue(5)
    print(f"After addToValue(5): {hm}")
    assert hm.get(1) == 15
    assert hm.get(2) == 25
    assert hm.get(3) == 35

    hm.addToKey(10)
    print(f"After addToKey(10): {hm}")
    assert not hm.exists(1)
    assert hm.exists(11)
    assert hm.get(11) == 15
    assert hm.get(12) == 25
    assert hm.get(13) == 35

    hm.insert(11, 100)  # overwrite key 11 (internal: 11-10=1)
    assert hm.get(11) == 100
    print(f"After insert(11, 100): {hm}")

    print("\nQuery-based tests:")
    queries = [
        ["insert", 0, 0],
        ["addToValue", 100],
        ["addToKey", -1],
        ["get", -1],    # should be 100
        ["insert", 0, 5],
        ["get", 0],     # should be 5
    ]
    results = solution(queries)
    print(f"Results: {results}")
    assert results == [100, 5], f"FAIL: {results}"
    print("PASS")

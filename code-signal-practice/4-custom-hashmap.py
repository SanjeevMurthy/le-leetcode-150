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
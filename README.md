`PersistentDict` is a dict with save and load functions.

Example
=======
```python
from pdict import PersistentDict

fn = "test.json"

# Create new dict
pd1 = PersistentDict()

# Assign a value to a key
pd1["foo"] = random.randint(0, 100)

# Dict can also be accessed via .data.*
pd1.data.bar = "baz"

print(pd1)

# Save dict to file
pd1.save(fn)

# Create new dict and load from file
pd2 = PersistentDict(fn)

print(pd2)

print("is:", pd1 is pd2)
print("==:", pd1 == pd2)
```
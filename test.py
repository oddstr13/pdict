from pdict import PersistentDict as pdict
import random

fn = "test.json"

pd1 = pdict()
pd1["foo"] = random.randint(0, 100)
pd1.data.bar = "baz"
print(pd1)
pd1.save(fn)

pd2 = pdict(fn)
print(pd2)

print("is:", pd1 is pd2)
print("==:", pd1 == pd2)

del pd2["bar"]
print(pd2)
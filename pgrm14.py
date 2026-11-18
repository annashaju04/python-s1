a = {"a": 5, "b": 2, "c": 8, "d": 1}
print("Ascending:", dict(sorted(a.items(), key=lambda x: x[1])))
print("Descending:", dict(sorted(a.items(), key=lambda x: x[1], reverse=True)))

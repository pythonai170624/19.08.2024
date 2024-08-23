
########### set
# distinct
s = {1, 2, 3}
s.add(4)
print(s)

s.clear()
print(s)

s = {1, 2, 3}
s1 = s.copy()
print(s1)

# print(s[0])  #  Error


print({1, 2, 2, 2, 2, 2, 1, 1, 1})  # {1, 2}


s1 = {1, 2, 3, 4}
s1.discard(1)
print(s1)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
inter = set1.intersection(set2)  # inter becomes {3}
print('intersection', inter)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 & set2  # result is {3}
print('set1 & set2', result)

s = {1, 2, 3}
t = {40}
result1 = s.isdisjoint(t)  # True if nothing in common
print(result1)

s = {1, 2, 30}
t = {30}
result1 = s.isdisjoint(t)
print(result1)

s = {1, 5}
t = {1, 2, 3}
result = s.issubset(t)  # result is False
print(result)

s = {1, 2}
t = {1, 2, 3}
result = s.issubset(t)  # result is True
print(result)
s = {1, 2, 3}
t = {1, 2, 3}
print('set1 <= set2', s <= t)
s = {1, 2, 3}
t = {1, 2, 3}
print('set1 < set2', s < t)  # False
s = {1}
t = {1, 2, 3}
print('set1 < set2', s < t)  # True


s = {1, 2, 3}
t = {1, 2}
result = s.issuperset(t)  # result is True
# x > 3 , 3 < x
s = {1, 2, 3}
t = {1, 2}
result = s >= t  # result is True

# (s | t) - (s & t)

s = {1, 2, 3, 4}
t = {1, 2, 3}
result = s.issuperset(t)  # result is True

s = {1, 2, 3}
elem = s.pop()
print(elem)
print(s)

s = {1, 2, 3, 40, 100}
s.remove(40)
print(elem)
print(s)
print(3 in s)

s1 = {3, 4, 5}
s2 = {1, 2, 3, 4}
# remove from s1 all s2 items
print('difference', s1.difference(s2))  # s1 - s2
print('s1 - s2', s1 - s2)  # also minus

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 10, 20, 30, 40}
print('difference', s1.difference(s2))  # removing the smilier

s = {1, 2, 3, 4}
s2 = {3, 4, 5, 10, 20, 30, 40}
# take items which ONLY appear in ONE of the groups
# keeping the different
sym_diff = s.symmetric_difference(s2)  # sym_diff becomes {1, 2, 5, 10, 20, 30, 40}
print('symmetric', sym_diff)
s = {1, 2, 3, 4}
s2 = {3, 4, 5, 10, 20, 30, 40}
print("set1 ^ set2", set1 ^ set2)  # {1, 2, 5, 10, 20, 30, 40}



s1 = {1, 2, 3}
s2 = {2, 3, 4}
# updates the specific set
s1.update(s2)
# s1 == {1, 2, 3, 4} changes the original ser
print('update', s1.update())  # None
print('update', s1)

s1 = {1, 2, 3}
s2 = {3, 4}
# returns a new set
union_set2 = {1, 2, 3} | {3, 4}
union_set2 = s1 | s2
# s1 == {1, 2, 3} the original set remains the same
print('union', s1.union(s2))
print("{1, 2, 3} | {3, 4} = ", {1, 2, 3} | {3, 4})
#my_list: list[int | float] = [1, 4.5]

#### frozen set
fs = frozenset([1, 2, 3])
# fs.pop()  # Error
# fs.remove()  # Error


print({1, 2 , 3}.update({4}))

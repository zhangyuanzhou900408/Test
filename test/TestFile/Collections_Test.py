from collections import namedtuple
from collections import deque
from  collections import defaultdict
from collections import OrderedDict
#namedtuple可以用属性而不是索引来引用 tuple 的某个元素
point = namedtuple("point",["x","y"])
p = point(1,2)
print(p.x )
print(p.y)
#deque  插入元素
data = deque([1,2,3])
data.append("x")
data.insert(2,"b")
data.appendleft("c")
#data.pop("x")
print(data)
# defaultdict  不存在时，返回一个默认值
dd = defaultdict(lambda :"NA")
dd[1]="zhang"
print(dd[2])
#如果要保持 Key 的顺序，可以用 OrderedDict ：
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
from collections import Counter
c= Counter()
for ch in "yyzzsscccddedd":
    c[ch] = c[ch]+1
print(c)
#迭代器的学习
import itertools
#data = itertools.count(1)
#for i  in  data:
    #print(i)
# cs = itertools.cycle([1,2,3,4])
# for i in cs:
#     print(i)
# cs = itertools.repeat("2",6)
# for i in cs:
#     print(i)
# cs = itertools.chain("abc","def")
# for i in cs:
#     print(i)
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
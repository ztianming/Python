# Python 实用代码

## **1 重复元素判定**

以下方法可以检查给定列表是不是存在重复元素，它会使用 set() 函数来移除所有重复元素。

```python
def all_unique(lst):
	return len(lst)== len(set(lst))
x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
all_unique(x) # False
all_unique(y) # True
```

## **2 字符元素组成判定**

检查两个字符串的组成元素是不是一样的。

```python
from collections import Counter

def anagram(first, second):

	return Counter(first) == Counter(second)

anagram("abcd3", "3acdb") # True
```

## **3 内存占用**

下面的代码块可以检查变量 variable 所占用的内存。

```python
import sysvariable = 30

print(sys.getsizeof(variable)) # 24
```

## **4 字节占用**

下面的代码块可以检查字符串占用的字节数。

```python
def byte_size(string):
	return(len(string.encode('utf-8')))

byte_size('😀) # 4

byte_size('Hello World') # 11
```

## **5 打印 N 次字符串**

该代码块不需要循环语句就能打印 N 次字符串。

```python
n = 2
s ="Programming"

print(s * n)# ProgrammingProgramming
```

## **6 大写第一个字母**

以下代码块会使用 title() 方法，从而大写字符串中每一个单词的首字母。

```python
s = "programming is awesome"

print(s.title())# Programming Is Awesome
```

## **7 分块**

给定具体的大小，定义一个函数以按照这个大小切割列表。
```python

from math import ceil

def chunk(lst, size):

	return list(map(lambda x: lst[x * size:x * size + size],list(range(0, ceil(len(lst) / size)))))

chunk([1,2,3,4,5],2)# [[1,2],[3,4],5]
```

## **8 压缩**

这个方法可以将布尔型的值去掉，例如（False，None，0，“”），它使用 filter() 函数。
```python

def compact(lst):
	return list(filter(bool, lst))

compact([0, 1, False, 2, '', 3, 'a', 's', 34])# [ 1, 2, 3, 'a', 's', 34 ]
```
## **9 解包**

如下代码段可以将打包好的成对列表解开成两组不同的元组。

```python
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]

transposed = zip(*array)

print(transposed)# [('a', 'c', 'e'), ('b', 'd', 'f')]
```

## **10 链式对比**

我们可以在一行代码中使用不同的运算符对比多个不同的元素。
```python
a = 3print( 2 < a < 8) # True

print(1 == a < 2) # False
```

## **11 逗号连接**

下面的代码可以将列表连接成单个字符串，且每一个元素间的分隔方式设置为了逗号。
```python
hobbies = ["basketball", "football", "swimming"]

print("My hobbies are: " + ", ".join(hobbies))# My hobbies are: basketball, football, swimming
```

## **12 元音统计**

以下方法将统计字符串中的元音 (‘a’, ‘e’, ‘i’, ‘o’, ‘u’) 的个数，它是通过正则表达式做的。
```python
import re

def count_vowels(str):
	return len(len(re.findall(r'[aeiou]', str, re.IGNORECASE)))

count_vowels('foobar') # 3
count_vowels('gym') # 0
```

多个分割符切分字符串

```python
import re

line='hello,world'
# [] 内填入对应分割符号
lineLists = re.split('[，,.。？?]',line.strip())
```



## **13 首字母小写**

如下方法将令给定字符串的第一个字符统一为小写。
```python

def decapitalize(string):
	return str[:1].lower() + str[1:]

decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar') # 'fooBar'
```

## **14 展开列表**

该方法将通过递归的方式将列表的嵌套展开为单个列表。
```python

def spread(arg):
	ret = []
	for i in arg:
        if isinstance(i, list):
        	ret.extend(i)
        else:
        	ret.append(i)
	return ret
def deep_flatten(lst):
    result = []
    result.extend(spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result

deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]
```

## **15 列表的差**

该方法将返回第一个列表的元素，其不在第二个列表内。如果同时要反馈第二个列表独有的元素，还需要加一句 set_b.difference(set_a)。
```python
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)

difference([1,2,3], [1,2,4]) # [3]
```

## **16 通过函数取差**

如下方法首先会应用一个给定的函数，然后再返回应用函数后结果有差别的列表元素。
```python

def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]

from math import floor
difference_by([2.1, 1.2], [2.3, 3.4],floor) # [1.2]difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])# [ { x: 2 } ]
```

## **17 链式函数调用**

你可以在一行代码内调用多个函数。
```python
def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

a, b = 4, 5
print((subtract if a > b else add)(a, b)) # 9
```

## **18 检查重复项**

如下代码将检查两个列表是不是有重复项。
```python
def has_duplicates(lst):
	return len(lst) != len(set(lst))

x = [1,2,3,4,5,5]
y = [1,2,3,4,5]
has_duplicates(x) # True
has_duplicates(y) # False
```

## **19 合并两个字典**

下面的方法将用于合并两个字典。
```python
def merge_two_dicts(a, b):
    c = a.copy() # make a copy of a 
    c.update(b) # modify keys and values of a with the once from b
    return c

a={'x':1,'y':2}
b={'y':3,'z':4}
print(merge_two_dicts(a,b))#{'y':3,'x':1,'z':4}
```

在 Python 3.5 或更高版本中，我们也可以用以下方式合并字典：
```python
def merge_dictionaries(a, b)
	return {**a, **b}

a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b))# {'y': 3, 'x': 1, 'z': 4}
```

## **20 将两个列表转化为字典**

如下方法将会把两个列表转化为单个字典。

```python
def to_dictionary(keys, values):
	return dict(zip(keys, values))

keys = ["a", "b", "c"]
values = [2, 3, 4]
print(to_dictionary(keys, values))#{'a': 2, 'c': 4, 'b': 3}
```

## **21 使用枚举**

我们常用 For 循环来遍历某个列表，同样我们也能枚举列表的索引与值。
```python

list = ["a", "b", "c", "d"]
for index, element in enumerate(list): 
	print("Value", element, "Index ", index, )
# ('Value', 'a', 'Index ', 0)
# ('Value', 'b', 'Index ', 1)
#('Value', 'c', 'Index ', 2)
# ('Value', 'd', 'Index ', 3)
```

## **22 执行时间**

如下代码块可以用来计算执行特定代码所花费的时间。
```python

import time
start_time = time.time()
a = 1
b = 2
c = a + b
print(c) #3
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time) # ('Time: ', 1.1205673217773438e-05) 
```

## **23 Try else**

我们在使用 try/except 语句的时候也可以加一个 else 子句，如果没有触发错误的话，这个子句就会被运行。
```python
try:
	2*3
except TypeError:
	print("An exception was raised")
else:
	print("Thank God, no exceptions were raised.")

#Thank God, no exceptions were raised.
```

## **24 元素频率**

下面的方法会根据元素频率取列表中最常见的元素。
```python

def most_frequent(list):
	return max(set(list), key = list.count)

list = [1,2,1,2,3,2,1,4,2]
most_frequent(list)
```

## **25 回文序列**

以下方法会检查给定的字符串是不是回文序列，它首先会把所有字母转化为小写，并移除非英文字母符号。最后，它会对比字符串与反向字符串是否相等，相等则表示为回文序列。
```python


def palindrome(string):
    from re import sub
    s = sub('[W_]', '', string.lower())
    return s == s[::-1]

palindrome('taco cat') # True
```

## **26 不使用 if-else 的计算子**

这一段代码可以不使用条件语句就实现加减乘除、求幂操作，它通过字典这一数据结构实现：
```python

import operator
action = {"+": operator.add,"-": operator.sub,"/": operator.truediv,"*": operator.mul,"**": pow}
print(action['-'](50, 25)) # 25
```

## **27 Shuffle**

该算法会打乱列表元素的顺序，它主要会通过 Fisher-Yates 算法对新列表进行排序：
```python
from copy import deepcopy
from random import randint
def shuffle(lst):
	temp_lst = deepcopy(lst)
	m = len(temp_lst)
	while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
return temp_lst

foo = [1,2,3]
shuffle(foo) # [2,3,1] , foo = [1,2,3]
```
## **28 展开列表**

将列表内的所有元素，包括子列表，都展开成一个列表。
```python
def spread(arg):

    ret = []

    for i in arg:

    	if isinstance(i, list):

    		ret.extend(i)

    	else:

    		ret.append(i)

    return retspread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]
```

## **29 交换值**

不需要额外的操作就能交换两个变量的值。
```python
def swap(a, b):
	return b, a

a, b = -1, 14
swap(a, b) # (14, -1)
```

## **30 字典默认值**

通过 Key 取对应的 Value 值，可以通过以下方式设置默认值。如果 get() 方法没有设置默认值，那么如果遇到不存在的 Key，则会返回 None。
```python
d = {'a': 1, 'b': 2}
print(d.get('c', 3)) # 3
```

小数转分数

> Fraction(numerator=0, denominator=1) 

> 第一个参数是分子，默认为0；第二个参数为分母，默认为1。
>
> Fraction(4,3)
>
> 传入浮点数 Fraction(4,3)
>
> limit_denominator() 找到最佳近似值

```python
from fractions import Fraction
d = float(input())
res =str(Fraction(d).limit_denominator())
print(res)

```

## 判断是否是素数

```python
import math
def p(n):
    return math.factorial(n-1)**2%n

def is_prime(n):
    if n <= 1:    
        return False   
    i = 2   
    while i*i <= n:    
        if n % i == 0:    
            return False   
        i += 1   
    return True

def is_prime(num):
    p=n=1
    loc = locals()
    exec("p*=n*n;n+=1;"*~-int(num))
    p=loc['p']
    n=loc['n']
    # print(p,n)
    print(p%n)
    return p%n

def p(n):
  return[i for i in range(1,n)if n%i==0]==[1]
```

## 罗马数字转整数

```python
def romanToInt(s):
    roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    res=0
    for i in range(len(s)-1):
        if roman_dict[s[i]]<roman_dict[s[i+1]]:
            res-=roman_dict[s[i]]
        else:
            res+=roman_dict[s[i]]
   res += roman_dict[s[-1]]
   return res
```

## 整数转罗马数字

```python
def intToRoman(num):
    res = ""
    N=(1000,900,500,400,100,90,50,40,10,9,5,4,1)
    for i in range(len(N)):
 		c=n//N[i]
 		r+='M,CM,D,CD,C,XC,L,XL,X,IX,V,IV,I'.split(',')[i]*c
 		n-=N[i]*c
    return res

```

## 杨辉三角

\# Pascal's Triangle short

[0, 1]

[1, 0] get [1, 1]

[0,1,1]

[1,1,0] get [1,2,1]

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1,numRows):
            res.append(list(map(add, [0]+res[-1], res[-1]+[0])))
        return res if numRows else []
```



## 快速排序

```python
def quicksort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    left, pivot, right = partition(arr)
    return quicksort(left) + [pivot] + quicksort(right)

def partition(arr):
    # 选择pivot
    pivot, arr = arr[0], arr[1:]
    # 小于pivot部分
    left = [x for x in arr if x <= pivot]
    # 大于pivot部分
    right = [x for x in arr if x > pivot]
    return left, pivot, right
```

按指定长度分割字符串或list

```python
# obj: string or list
# length: the length of cut
def cut(obj, length):
    return [obj[i:i+length] for i in range(0,len(obj),length)]
cut("abcde", 2) #['ab', 'cd', 'e']
```



# 图的连通性判断-并查集

```python
pre = {}

def find(x):
    r = x
    while pre[r] != r:
        r = pre[r]
    i = x
    while i != r:  # 路径压缩，平衡树层次的效果
        j = pre[i]
        pre[i] = j
        i = j
    return r

def join(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        # root = min(fx, fy)  # 平衡树的层次的效果
        # pre[fx] = root
        # pre[fy] = root
        pre[fx] = fy


def judge(n, edges):
    '''
    判断是否连通
    :param n: 节点数
    :param edges: 边的集合
    :return: 是否连通
    >>> judge(4, [(0, 1), (2, 0),(2, 3)])
    True
    >>> judge(4, [(2, 0),(2, 3)])
    False
    '''
    for i in range(n):
        pre[i] = i
    for i in range(len(edges)):
        join(edges[i][0], edges[i][1])
    group = 0
    for i in range(n):
        if pre[i] == i:
            group += 1
    if group == 1:
        return True
    else:
        return False
print(judge(4, [(0, 1), (2, 0),(2, 3)])) # True
```

# 快速幂

```python
# base^power % mod
def fastPower(base, power, mod):
    res = 1
    while power > 0:
        if power&1:
        	res = (res*base)%mod
      	base = base **2 % mod
        power >>= 1
  	return res
```



# 正则表达式

```python
import re
# s:str, p:parten
def match(s, p):
    return re.fullmatch(p, s) != None
```



# 计算表达式

(+ 1 2 )

(+ 1 (+ 2 3))

(* (+ 1 2) (*3 4))

```python
#calculator expression

def cal_1 (s):
    s = s.strip().replace('(','',1)[::-1].replace(')','',1)[::-1].strip()
    if ' ' not in s :
        return float(s)  #just a number
    else:
        tmp = s.split(' ',1)
        opt = tmp[0].strip()
        temp = tmp[1].strip()
        left = 0       
        right = 0
        for i in range(len(temp)):
            if temp[i] == '(':
                left += 1
            if temp[i] == ')':
                right += 1
            if temp[i] == ' ' and left==right :
                break
        
        data1 = temp[:i]
        data2 = temp[i:]

        v1 = cal_1(data1)
        v2 = cal_1(data2)
        if opt == '+':
            return v1 + v2
        elif opt == '-':
            return v1 - v2
        elif opt == '*':
            return v1 * v2
        elif opt == '/':
            return v1 / v2
        elif opt == '%':
            return v1 % v2
        else:
            return 0


def cal_2 (s):
    def cal_exp (exp):
        def cal_exp_two (opt,a,b):
            a = float(a)
            b = float(b)
            if opt == '+':
                return a+b
            elif opt == '-':
                return a-b
            elif opt == '*':
                return a*b
            elif opt == '/':
                return a/b
            elif opt == '%':
                return a%b
            else:
                return 0
        result = exp[1]
        for i in range(2,len(exp)):
            result = cal_exp_two (exp[0],result,exp[i])
        return result
    s = s.replace('(',' ( ').replace(')',' ) ')
    left = s.split()
    right = []
    temp  = []
    while left:
        tmp_left = left.pop().strip()
        if tmp_left == '(':
            tmp_right = right.pop()
            while tmp_right != ')':
                temp.append (tmp_right)
                tmp_right = right.pop()
            right.append (cal_exp(temp))
            temp = []
        else:
            right.append (tmp_left)
    return right[-1]

print cal_1 ( '(- (+ 23 1) (* 3 4))')     #12.0
print cal_1 ( '(- (+ 1 2) (* 3 4))')      #-9
print cal_1 ( '(- 1 1)')                  #0
print cal_1 ( '(- 1 (* 12 12))' )         #-143.0
print cal_1 ( '(- (* 23 2) 12))' )        #34.0
print '----------------------'
#
print cal_2 ( '(- (+ 23 1) (* 3 4))')     #12.0
print cal_2 ( '(- (+ 1 2) (* 3 4))')      #-9
print cal_2 ( '(- 1 1)')                  #0
print cal_2 ( '(- 1 (* 12 12))' )         #-143.0
print cal_2 ( '(- (* 23 2) 12))' )        #34.0
print cal_2 ( '(- (* 23 2 2) 12 ))' )     #80.0


```


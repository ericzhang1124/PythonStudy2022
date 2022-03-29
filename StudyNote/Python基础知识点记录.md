# Python 基础的知识点记录（补充未知基础知识）

## 字符串的`isdigit()`方法
> isdigit()方法用来判断一个字符串中是否有非数字元素，若存在返回False否则返回Ture
```python
"10".isdigit() # => return True
"text".isdigit() # => return False
"-10".isdigit() # => return False, because "-" is not digit
"0.1".isdigit() # => return False, because "." is not digit
```

## set数据类型
> 相比较于list，无序 & 不重复 (不过他们都是可变对象，可以添加或移除元素)
```python
my_set = {'hello', 'kitty', 'is', 'kawayi', 'is'}
# 无序 - 意味着元素位置不固定，无法向list一样使用 my_set[index]这样的方式获取元素
# 无序 - 同样意味着当使用 for set_element in my_set:方式遍历元素时，每次获取的元素顺序不固定

# 不重复 - 该数据类型会自动将重复元素剔除

# dict里的key的构成其实就是set，set就相当于没有value的dict
```

## module & package
> module Just a python file with defined(class, function, variable),This Python 特性产物
> package can look as a collection of modules, thoese modules has dictionary construct
--
>> `import` function is find the module file and get all the file defined element(variable, class,function)
    > import build-in-module (such as   `import time`)
    > import build-in-package-moudle(such as `import html.parser`)
    > import third-party-package-moudle(just as import build-in-package-moudle)
>> `from import` function is find the module file and get one or more clarity element(variable, class,function)
    > from <module> import <element(variable, class,function)>(such as `from html.parser import HTMLParser`)


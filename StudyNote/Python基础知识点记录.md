# Python 基础的知识点记录（补充未知基础知识）

## 字符串的`isdigit()`方法
> isdigit()方法用来判断一个字符串中是否有非数字元素，若存在返回False否则返回Ture
```python
"10".isdigit() # => return True
"text".isdigit() # => return False
"-10".isdigit() # => return False, because "-"
"0.1".isdigit() # => return False, because "." 
```


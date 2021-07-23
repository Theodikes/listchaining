## Methods for iterable JavaScript objects in Python

The most commonly used methods of iterable objects in JavaScript are: arrays, dictionaries, strings, and so on in Python.

```python
>>> import jsmethods
>>> a = [1, 2, 3, 4, 5]
>>> a.map(lambda x: x * 2)
[2, 4, 6, 8, 10]
>>> b = a.map(lambda x: x * 2)
>>> a
[1, 2, 3, 4, 5]
>>> b
[2, 4, 6, 8, 10]
>>> nested = [1, 2, [3, [4, 5]]]
>>> nested.flat(2).filter(lambda x: x > 2).map(lambda x: x ** 2)
[9, 16, 25]
```



All functionality is taken from the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects) and implemented in python by adding methods to the built-in class. All new methods do not directly modify class instances, but create copies (if required). All methods have chaining functionality, that is, they can be called sequentially, and at the same time the instance with which the next method works will be the value returned by the previous function.




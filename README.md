## Methods for iterable JavaScript objects in Python

The most commonly used methods of Javascript arrays and chaining in Python - just import the module!

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



All functionality is taken from the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods) and implemented in python by adding methods to the built-in class. All new methods do not directly modify class instances, but create copies (if required). All methods have chaining functionality, that is, they can be called sequentially, and at the same time the instance with which the next method works will be the value returned by the previous function (obviously apart from methods returning boolean or number).

#### Differences from JavaScript

Some methods, due to the peculiarities of Python or the developer's ideas, have not been added or their functionality is slightly different from that described on MDN. Below is a list of them and a description of the differences.

##### All methods:

- All camelCase functions are translated according to PEP 8 to snake_case: for example `Array.lastIndexOf` -> `list.last_index_of`
- All methods that modify the object for which they are called have not been added, since such modifyings contradict the main idea of this library
- The names of all methods of JavaScript objects that match the names of the built-in methods of the corresponding objects in Python have been changed because the library does not overwrite built-in methods

##### Array / List methods:

- `Array.indexOf` not added because python has a built-in analog: `list.index`
- `Array.pop` & `Array.shift` and `Array.push` & `Array.unshift` not added because these methods modify the original object. In addition, there is a built-in analogue for any of these functions in python: `list.pop` & `list.pop(0)` and `list.append` & `list.insert(0, v)`, respectively
- `Array.reverse` -> `list.reversed`, and now this method does not modify the array, but returns an reversed copy
- `Array.sort` -> `list.sorted`, and now this method does not modify the array, but returns an sorted copy. In addition, the method takes as an argument not a function for comparison, but the standard arguments of the `sorted` built-in function in Python
- `list.join` has an additional argument that `Array.join` does not have: a boolean parameter `cast_types` indicating whether non-string objects will be cast to string when concatenated, since the standard Python join function will simply throw an error if any of the being objects being merged have non-string type
- `list.concat`  has an additional argument that `Array.join` does not have: a boolean parameter `expand_strings` indicating if adding a string to the array needs to "expand" it as an array of individual characters or just add it to the array entirely
- `Array.splice` not added because this method changes the contents of an array in place
- `list.last_index_of` if the element you are looking for is not in the array, it will throw an error instead of returning -1






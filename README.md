## Methods for iterable JavaScript objects in Python

The most commonly used methods of iterable objects in JavaScript are: arrays, dictionaries, strings, and so on. All functionality is taken from the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects) and implemented in python by adding methods to the built-in class.

All new methods do not directly modify class instances, but create copies (if required). All methods have chaining functionality, that is, they can be called sequentially, and at the same time the instance with which the next method works will be the value returned by the previous function: for example, arr.flat ().filter(some_func).map(some_func2) is a valid construction.




Enflux Questions
================

These are my solutions to the Enflux Pre-Interview Questions along with any
observations or notes about the questions themselves.

Array Diff
----------

There are two different solutions presented for this problem one will work in
all scenarios and the other will only work if every integer in the arrays is
unique. The unique solution uses simple set math to produce the addition and
deletion arrays while the generalized solution makes a copy and removes values
as they occur in the opposite array.

### Running

The arrays are currently defined in code for the example as the functions accept
two different arrays they can be easily changed and ran either in code or in
the interpreter.

#### Running from Interpreter

```python
>>> import array_diff
>>> array_diff.get_additions_from_arrays([1,3], [1,2,3])
[2]
```

Social Network Analysis
-----------------------

The social network analysis uses sys.argv to pull in the postId's to be checked.
By default it's loading the csv from 'social_network.csv'.

### Running

```
> python social_network.py 1 7
1: 350
7: 480
```

#### Loading data from a different file

```python
>>> import os
>>> import social_network
>>> data = social_network.load_data_from_csv(os.path.join("/path/to/loc", "my.csv"))
>>> print social_network.get_followers(data, 1)
350
```

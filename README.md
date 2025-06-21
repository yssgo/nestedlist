# nestedlist
`array = nested_list([12,6,7], int)`  is an emulation of `int array[12][6][7];` in c.
# install

```bash
pip install git+https://github.com/yssgo/nestedlist.git
```

# usage

* Python code
```python
from __future__ import print_function
from pprint import pprint
from nestedlist import nested_list
def p_print(prompt, ob):
    print(prompt, end=' ')
    pprint(ob, sort_dicts=False)
a = nested_list([1,2])
p_print('nested_list([1,2]) =', a)
b = nested_list([3,4,2], int)
p_print('nested_list([3,4,2], int) =', b)
c = nested_list([2,3], int, 300)
p_print('nested_list([2,3], int, 300) =', c)
d = nested_list([2,3], dict, k1="qwer", k2=12345)
p_print('nested_list([2,3], dict, k1="qwer", k2=12345) =', d)
```

* Terminal:

```shell
~/my/sandbox $ py dltest.py
nested_list([1,2]) = [[None, None]]
nested_list([3,4,2], int) = [[[0, 0], [0, 0], [0, 0], [0, 0]],
 [[0, 0], [0, 0], [0, 0], [0, 0]],
 [[0, 0], [0, 0], [0, 0], [0, 0]]]
nested_list([2,3], int, 300) = [[300, 300, 300], [300, 300, 300]]
nested_list([2,3], dict, k1="qwer", k2=12345) = [[{'k1': 'qwer', 'k2': 12345},
  {'k1': 'qwer', 'k2': 12345},
  {'k1': 'qwer', 'k2': 12345}],
 [{'k1': 'qwer', 'k2': 12345},
  {'k1': 'qwer', 'k2': 12345},
  {'k1': 'qwer', 'k2': 12345}]]
~/my/sandbox $
```

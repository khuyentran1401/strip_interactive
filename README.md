# Strip Interactive Python String

Have you ever come across an online tutorial that shows interactive Python code like this:

```python
>>> import numpy as np
>>> print(np.array([1,2,3]))
array([1, 2, 3])
```

and wished to run only the inputs like below?

```python
import numpy as np
print(np.array([1,2,3]))
```

That is when strip-interactive comes in handy. 

## Usage
To use strip-interactive, simply add the code you want to run to `run_interactive` method.

```python
from strip_interactive import run_interactive

code = """
>>> import numpy as np
>>> print(np.array([1,2,3]))
array([1, 2, 3])
"""

outputs = run_interactive(code)
```

Output:
```bash
[1 2 3]
```
You can also get the clean code (without inputs and `>>>`) using `get_clean_code` method.

```python
from strip_interactive import get_clean_code

code = """
>>> import numpy as np
>>> print(np.array([1,2,3]))
array([1, 2, 3])
"""

inputs = get_clean_code(code)
print(inputs)
```
Output:
```bash
import numpy as np
print(np.array([1,2,3]))
```
## Installation
```bash
pip install run-interactive
```

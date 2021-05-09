from strip_interactive import run_interactive, get_clean_code

code = """
>>> import numpy as np
>>> print(np.array([1,2,3]))
array([1, 2, 3])
"""

outputs = run_interactive(code)
inputs = get_clean_code(code)
print(inputs)
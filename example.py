from strip_interactive import run_interactive

code = """
>>> import numpy as np
>>> print(np.array([1,2,3]))
array([1, 2, 3])
"""

print(run_interactive(code))
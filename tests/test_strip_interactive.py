from strip_interactive.strip_interactive import *
import numpy as np 


def test_split_lines():
    interactive_code = """
>>> import numpy as np
>>> np.array([1,2,3])
array([1, 2, 3])
"""
    assert InteractiveRunner._split_lines(interactive_code) == ['', '>>> import numpy as np', 
                                            '>>> np.array([1,2,3])',
                                            'array([1, 2, 3])', '']

def test_split_lines_with_dots():
    interactive_code = """
>>> def say_hello():
...     print('Hello')
>>> say_hello()
Hello
"""
    assert InteractiveRunner._split_lines(interactive_code) == ['', '>>> def say_hello():', 
                                            "...     print('Hello')",
                                            ">>> say_hello()", 'Hello', '']

def test_remove_outputs():
    lines = ['>>> import numpy as np', 
            '>>> np.array([1,2,3])',
            'array([1, 2, 3])']
    assert InteractiveRunner._remove_outputs(lines) == ['import numpy as np', 
                                    'np.array([1,2,3])']

def test_remote_outputs_with_dots():
    lines = ['>>> def say_hello():', 
            "...     print('Hello')",
            ">>> say_hello()", 'Hello']
    assert InteractiveRunner._remove_outputs(lines) == ['def say_hello():', 
                                            "    print('Hello')",
                                            "say_hello()"]

def test_run_inputs():
    inputs = ["import numpy as np", "print(np.array([1,2,3]))"]
    assert InteractiveRunner._run_inputs(inputs) == '[1 2 3]\n'

def test_run_inputs_with_dots():
    inputs = ['def say_hello():', "    print('Hello')", "say_hello()"]
    assert InteractiveRunner._run_inputs(inputs) == 'Hello\n'

def test_run_interactive():
    interactive_code = """
>>> import numpy as np
>>> print(np.array([1,2,3]))
[1 2 3]
"""
    assert InteractiveRunner(interactive_code).run_interactive() == '[1 2 3]\n'

def test_run_interactive_with_dots():
    interactive_code = """
>>> def say_hello():
...     print('Hello')
>>> say_hello()
Hello
"""
    assert InteractiveRunner(interactive_code).run_interactive() == 'Hello\n'

def test_run_interactive_more_complicated():
    interactive_code = """
>>> import pandas as pd
>>> import numpy as np
>>> print(np.array([0, 1, 2]))
[0 1 2]
>>> df = pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]})
>>> print(df)
   col1  col2
0     1     4
1     2     5
2     3     6
"""
    assert InteractiveRunner(interactive_code).run_interactive() == '[0 1 2]\n   col1  col2\n0     1     4\n1     2     5\n2     3     6\n'

def test_run_interactive_much_more_complicated():
    interactive_code = """
>>> import simpy
>>> env = simpy.Environment()
>>> bcs = simpy.Resource(env, capacity=2)

>>> def car(env, name, bcs, driving_time, charge_duration):
...     # Simulate driving to the BCS
...     yield env.timeout(driving_time)
...
...     # Request one of its charging spots
...     print('%s arriving at %d' % (name, env.now))
...     with bcs.request() as req:
...         yield req
...
...         # Charge the battery
...         print('%s starting to charge at %s' % (name, env.now))
...         yield env.timeout(charge_duration)
...         print('%s leaving the bcs at %s' % (name, env.now))
>>> for i in range(4):
...     env.process(car(env, 'Car %d' % i, bcs, i*2, 5))
>>> env.run()
"""

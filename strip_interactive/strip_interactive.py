import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


class InteractiveRunner:
    def __init__(self, interactive_code: str):
        self.interactive_code = interactive_code
    
    @staticmethod
    def _split_lines(interactive_code: str):
        lines = interactive_code.split("\n")
        return lines


    @staticmethod
    def _remove_outputs(lines: list):
        inputs = []
        for line in lines:
            if line.startswith('>>>'):
                line = line.replace('>>> ', '')
                inputs.append(line)
            elif line.startswith('...'):
                line = line.replace('... ', '')
                if line != '...':
                    inputs.append(line)
        return inputs

    def get_clean_code(self):
        lines = self._split_lines(self.interactive_code)
        inputs = self._remove_outputs(lines)
        inputs = "\n".join(inputs)
        return inputs

    def run_inputs(self):
        inputs = self.get_clean_code()
        with stdoutIO() as s:
            exec(inputs)
        return s.getvalue()

def run_interactive(code: str):
    outputs = InteractiveRunner(code).run_inputs()
    print(outputs)
    return outputs

def get_clean_code(code: str):
    return InteractiveRunner(code).get_clean_code()




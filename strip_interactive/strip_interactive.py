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

    @staticmethod
    def _run_inputs(inputs: str):
        inputs = "\n".join(inputs)
        with stdoutIO() as s:
            exec(inputs)
        return s.getvalue()

    def run_interactive(self):
        lines = self._split_lines(self.interactive_code)
        inputs = self._remove_outputs(lines)
        outputs = self._run_inputs(inputs)
        return outputs



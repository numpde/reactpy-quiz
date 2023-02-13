from dashboard.components.quiz.commons import *


@component
def pipe(input: State, output: State, depth=0):
    if (depth == input.value) or (depth >= 10):
        output.set_value(-depth)
    else:
        return pipe(input, output, depth + 1)

    variables['pipe'] = locals()

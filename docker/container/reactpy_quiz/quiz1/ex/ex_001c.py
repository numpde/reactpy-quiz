from dashboard.components.quiz.commons import *


@component
def pipe(input: State, output: State):
    output.set_value(output.value + 1)
    output.set_value(output.value - 1)

    variables['pipe'] = locals()

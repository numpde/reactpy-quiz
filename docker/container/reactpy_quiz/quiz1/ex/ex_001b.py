from dashboard.components.quiz.commons import *


@component
def pipe(input: State, output: State):
    output.set_value(output.value + input.value)
    output.set_value(output.value - input.value)

    variables['pipe'] = locals()

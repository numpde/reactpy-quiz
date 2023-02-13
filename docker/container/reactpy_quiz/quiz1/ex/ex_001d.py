from dashboard.components.quiz.commons import *


@component
def pipe(input: State, output: State):
    output.set_value(lambda x: x + 1)
    output.set_value(lambda x: x - 1)

    variables['pipe'] = locals()

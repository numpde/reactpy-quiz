from dashboard.components.quiz.commons import *


@component
def pipe(input: State, output: State):
    output.set_value(datetime.now())

    variables['pipe'] = locals()

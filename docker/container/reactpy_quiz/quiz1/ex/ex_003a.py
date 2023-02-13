from dashboard.components.quiz.commons import *


@component
def pipe(input: State, output: State):
    x = use_ref(datetime.now())
    output.set_value(0)

    variables['pipe'] = locals()

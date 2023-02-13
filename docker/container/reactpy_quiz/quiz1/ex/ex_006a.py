from dashboard.components.quiz.commons import *


@component
def pipe(input: State, output: State):
    use_effect(
        lambda: output.set_value(datetime.now()),
        dependencies=[input.value]
    )

    variables['pipe'] = locals()

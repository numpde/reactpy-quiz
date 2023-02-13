from dashboard.components.quiz.commons import *


@component
def pipe(input: State, output: State):
    x = use_state(input.value)

    use_effect(
        lambda: output.set_value(datetime.now()),
        dependencies=[x.value]
    )

    variables['pipe'] = locals()

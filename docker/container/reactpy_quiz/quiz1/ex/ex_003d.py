from dashboard.components.quiz.commons import *


@component
def pipe(input: State, output: State):
    x = use_state(datetime.now())
    output.set_value(x.value)

    use_effect(
        lambda: None,
        dependencies=[input.value]
    )

    variables['pipe'] = locals()

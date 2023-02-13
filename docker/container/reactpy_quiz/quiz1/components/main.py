from pathlib import Path
from string import Template
from uuid import uuid4

from idom import component
from quiz1.commons import *

# style = (Path(__file__).parent / "styles.css").open(mode="r").read()


@component
def clicker(input: State):
    variables['clicker'] = locals()
    return html.button(
        f"Input: {input.value}",
        on_click=increment(input),
    )


@component
def main(pipe):
    input: State = use_state(0)
    output: State = use_state(0)
    variables['main'] = locals()

    return html.div(
        html.div(clicker(input)),
        html.div(pipe(input, output)),
        html.div(f"Output: ", output.value if input.value else "?"),
    )


@component
def show_code(f, show_debug=False):
    code = inspect.getsource(f)

    vars = variables.get(f.__name__)

    code = \
        [
            line
            for line in code.splitlines()
            if ('variables' not in line)
        ]

    while not code[-1].strip():
        code.pop()

    if show_debug:
        code += \
            [
                "",
            ] + [
                f"    # {k} = {v}"
                for (k, v) in vars.items()
            ]

    code = "\n".join(["    :::python", "    "] + ["    " + (x or "") for x in code])

    prefix = f"code-{f.__name__}"

    return \
        html.div(
            html.div(
                id=f"{prefix}-trg",
            ),
            html.input(
                id=f"{prefix}-src",
                type="hidden",
                input="text",
                value="asdasdad",  # markdown(code, extensions=["codehilite"]),
            ),
            html.script(
                # Copy html from input to div
                Template("""
                    let trg = document.getElementById('${prefix}-trg')
                    let src = document.getElementById('${prefix}-src')
                    trg.innerHTML = src.value
                """).safe_substitute(
                    prefix=prefix,
                ),

                key=uuid4().hex,
            )
        )


@component
def Main():
    examples = sorted(Path(__file__).parent.glob("ex_*.py"))
    current_example = use_state(0)
    do_show_debug = use_state(False)

    example_file = examples[current_example.value].stem
    pipe = importlib.import_module(example_file).pipe

    trigger = use_state(datetime.now())

    def on_click_prev(event):
        do_show_debug.set_value(False)
        current_example.set_value(lambda n: max(0, n - 1))

    def on_click_next(event):
        do_show_debug.set_value(False)
        current_example.set_value(lambda n: min(len(examples) - 1, n + 1))

    def metro(event):
        trigger.set_value(datetime.now())

    return \
        html.div(
            html.style(
                # style
            ),
            html.div(
                html.div(
                    html.div(
                        "Predict the output based on the input."
                    ),
                    html.div(
                        html.a(
                            "prev",
                            href="#",
                            on_click=on_click_prev,
                        ),

                        f" - {example_file} - ",

                        html.a(
                            "next",
                            href="#",
                            on_click=on_click_next,
                        ),
                    ),

                    html.div(
                        html.a(
                            "debug: {}".format("on" if do_show_debug.value else "off"),
                            href="#",
                            on_click=(lambda event: do_show_debug.set_value(lambda x: not x)),
                        )
                    ),

                    style={'text-align': "center"},
                ),

                html.div(
                    html.div(
                        "main:"
                    ),
                    html.div(
                        main(pipe=pipe, key=f"example-{current_example.value}"),
                        style={'display': "inline-block", 'padding': "0.5em", 'margin': "0.5em",
                               'border': "1px solid black"},
                    ),
                    style={'text-align': "center", 'margin': "0.5em"},
                ),

                html.div(
                    html.div(
                        show_code(pipe, show_debug=do_show_debug.value),
                        show_code(clicker, show_debug=do_show_debug.value),
                        show_code(main, show_debug=do_show_debug.value),
                        style={'display': "inline-block", 'width': "80%", 'padding': "0.5em", 'margin': "0.5em",
                               'border': "1px solid black", 'overflow-x': "scroll", 'text-align': "left"},
                    ),

                    style={'text-align': "center", 'margin': "0.5em"},
                ),

                html.input(id="callback", type="hidden", on_click=metro),
                html.script(
                    """
                    setInterval(
                        function() {
                            let callback = document.getElementById("callback");
                            //callback.click();
                        },
                        1200
                    );
                    """
                ),
            ),
        )

# from pathlib import Path
# from sanic import Sanic
# from sanic.response import file
#
# from idom import component, html
# from idom.backend.sanic import Options, configure
#
# app = Sanic("Main")
#
#
# @app.route("/")
# async def index(request):
#     return await file(str(Path(__file__).parent / "index.html"))
#
#
# @app.route("/styles.css")
# async def css(request):
#     return await file(str(Path(__file__).parent / "styles.css"))
#
#
# @component
# def view1():
#     return html.code("This text came from an IDOM App")
#
#
# configure(app, view1, Options(url_prefix="/_idom"))
#
# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port=5001)

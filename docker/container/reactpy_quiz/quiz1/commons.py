import inspect
import importlib
from datetime import datetime
from functools import partial

from idom import use_state, html, component, use_memo, use_ref, run, use_effect, use_context
from idom.core.types import State


def increment(x: State):
    def f(event=None):
        x.set_value(lambda n: n + 1)

    return f


variables = {}

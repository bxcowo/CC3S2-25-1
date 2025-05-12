import pytest

from features.steps.belly_steps import step_when_wait_time_description
from src.belly import Belly

class Context:
    def __init__(self) -> None:
        self.belly = Belly()

def test_parse_regex_validation():
    context = Context()
    sentence = "Quince horas, 16 minutos y 200 segundos"
    step_when_wait_time_description(context, sentence)

    assert context.belly.tiempo_esperado != 0

def test_parse_regex_hours():
    context = Context()
    sentence = "Veinte horas"
    step_when_wait_time_description(context, sentence)

    assert context.belly.tiempo_esperado == 20

def test_parse_regex_huge_minutes():
    context = Context()
    sentence = "8122039821 minutos"
    step_when_wait_time_description(context, sentence)

    assert context.belly.tiempo_esperado == (8122039821/60)

def test_parse_regex_none_seconds():
    context = Context()
    sentence = "cero segundos"
    step_when_wait_time_description(context, sentence)

    assert context.belly.tiempo_esperado == 0

def test_parse_regex_minutes_seconds():
    context = Context()
    sentence = "Cuarenta minutos y 13 segundos"
    step_when_wait_time_description(context, sentence)

    assert context.belly.tiempo_esperado == ((40/60) + (13/3600))

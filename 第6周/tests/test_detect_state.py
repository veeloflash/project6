import json
import os
import pytest
from src.statement import detect_state

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYWORD_FILE = os.path.join(ROOT_DIR, "state_keywords.json")


def test_detect_state_cannot_start():
    result = detect_state("No sé por dónde empezar")
    assert result["primary_state"] == "cannot_start"
    assert "cannot_start" in result["matched_states"]


def test_detect_state_concept_confusion():
    result = detect_state("No entiendo el concepto")
    assert result["primary_state"] == "concept_confusion"
    assert result["matched_states"] == ["concept_confusion"]


def test_detect_state_stuck_on_step():
    result = detect_state("¿Cómo sigo?")
    assert result["primary_state"] == "stuck_on_step"
    assert "stuck_on_step" in result["matched_states"]


def test_detect_state_expression_difficulty():
    result = detect_state("No sé cómo expresarlo")
    assert result["primary_state"] == "expression_difficulty"
    assert "expression_difficulty" in result["matched_states"]


def test_detect_state_empty_input():
    result = detect_state("")
    assert result == {
        "error": "Invalid input: text cannot be empty.",
        "matched_states": []
    }


def test_detect_state_mixed_status():
    result = detect_state("No entiendo y no sé cómo seguir")
    assert result["primary_state"] == "concept_confusion"
    assert result["matched_states"] == ["concept_confusion", "stuck_on_step"]


def test_detect_state_no_state_found():
    result = detect_state("Este texto no está relacionado")
    assert result == {
        "error": "No state found.",
        "matched_states": []
    }


def test_keyword_file_exists():
    assert os.path.exists(KEYWORD_FILE)
    with open(KEYWORD_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict)
    assert "cannot_start" in data

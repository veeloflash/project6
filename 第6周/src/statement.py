import json
import os


def _load_state_keywords():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    keyword_path = os.path.join(base_dir, "state_keywords.json")
    with open(keyword_path, "r", encoding="utf-8") as f:
        return json.load(f)


STATE_PRIORITY = [
    "cannot_start",
    "concept_confusion",
    "stuck_on_step",
    "expression_difficulty",
]


def detect_state(user_input):
    if not user_input or not user_input.strip():
        return {
            "error": "Invalid input: text cannot be empty.",
            "matched_states": []
        }

    text = user_input.lower()
    keywords = _load_state_keywords()
    matched_states = []

    for state_name, terms in keywords.items():
        if any(term in text for term in terms):
            matched_states.append(state_name)

    if not matched_states:
        return {
            "error": "No state found.",
            "matched_states": []
        }

    for state_name in STATE_PRIORITY:
        if state_name in matched_states:
            primary_state = state_name
            break

    return {
        "primary_state": primary_state,
        "matched_states": matched_states
    }

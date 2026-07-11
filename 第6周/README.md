# Week 6 Assignment for the Large Project

## Task Description

This project implements a user state detection module based on Spanish keywords to identify four main difficulty states during the learning process:

- `cannot_start`: unable to begin
- `concept_confusion`: does not understand the concept
- `stuck_on_step`: stuck at a step
- `expression_difficulty`: difficulty expressing ideas

## How to Run

1. Install dependencies (optional; the default setup uses pure Python with no extra dependencies):
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Run the main program:
   ```bash
   python main.py
   ```
3. Enter `exit` or `quit` to exit the program.

## Core Logic

- Keyword settings are stored in `state_keywords.json` for easier maintenance.
- `detect_state(text)` returns a result containing:
  - `primary_state`: the highest-priority main state
  - `matched_states`: all states that were matched
  - When the input is empty or no match is found, it returns an error message.

## Tests

Run the tests:

```bash
python -m pytest
```

The tests cover:

- empty input validation
- recognition of the four states
- priority handling for multi-state input
- unrelated text returning no state
- existence check for the keyword configuration file

## Known Limitations

- The current matching is a simple keyword-based rule system and does not include machine learning.
- In real questionnaire scenarios, broader corpus coverage and context understanding may be needed.
- If one input matches multiple states, the current implementation returns the primary state according to a strict priority order.

## Suggestions for Week 7 Integration

You can later connect the return structure of `detect_state()` to `decide_action(state)`:

```python
result = detect_state(user_input)
if "primary_state" in result:
    next_action = decide_action(result["primary_state"])
```

def detect_state(user_input):
    
    start_keywords = [
        "empezar", "inicio", "primer paso", "cómo empezar",
        "no sé cómo empezar", "no tengo ni idea", "hint"
    ]

    concept_keywords = [
        "qué es", "significa", "concepto", "definición",
        "no entiendo", "me explicas", "problema matemáticas",
        "asignatura redes"
    ]

    step_keywords = [
        "siguiente", "después", "luego", "seguir",
        "cómo seguir", "luego cómo se sigue"
    ]

    express_keywords = [
        "cómo se dice", "cómo decir", "palabras", "frase",
        "no sé expresarlo", "no sé cómo decirlo", "cómo expresarlo", "explicar lo"
    ]
    state=[]
    if any(keyword in user_input.lower() for keyword in start_keywords):
        state.append("1")
    if any(keyword in user_input.lower() for keyword in concept_keywords):
        state.append("2")
    if any(keyword in user_input.lower() for keyword in step_keywords):
        state.append("3")
    if any(keyword in user_input.lower() for keyword in express_keywords):
        state.append("4")
    if state == []:
        return "No state found."
    else:
        return state
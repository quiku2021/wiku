from interface.standard import QuestionsRequest
from api_openia import questions_request

questions = [
    "¿Cuál es la referencia?",
    "¿Qué tipo de documento es?",
    "¿Cuál es el número de expediente?",
    "¿Enumerame todos los hechos?",
    "¿Cuál es su tema principal?",
    "¿Cuál fue el magistrado?",
    "¿Qué sala es la responsable?",
]

async def ask_questions(questions_request: QuestionsRequest)-> [str]:
    text = clean_text(questions_request.text)
    questions = questions_request.questions
    text = text[:10000]
    response = questions_request({'text': text, 'questions': questions})
    return response
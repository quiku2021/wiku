from interface.standard import QuestionsRequest
from models.api_openia import questions_request
import models.hugging_face as hf

# Función con OpenIA
# def ask_questions(request: QuestionsRequest)-> [str]:
#     request.text = request.text[:1000]
#     response = questions_request(request)
#     return response

# Función con Hugging Face
def ask_questions(request: QuestionsRequest)-> [str]:
    request.text = request.text[:1000]
    response = hf.hugging_face(request)
    return response
from transformers import pipeline
from interface.standard import QuestionsRequest

text2text_generator = pipeline("text2text-generation", model="t5-base", revision="686f1db")

def hugging_face(request: QuestionsRequest):
    answers = []
    for question in request.questions:
        answer = f"question:{question}\ncontext{request.text}"
        answers.append(text2text_generator(answer))
    return answers
import openai
from interface.standard import QuestionsRequest
from helpers.text import clean_text

openai.api_key = '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'

async def questions_request(questions_request: QuestionsRequest)-> [str]:
    answers = []
    for question in questions:
        prompt = f"{text}\n\nQuestion: {question}\nAnswer:"
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )
        answer = response.choices[0].text.strip()
        answers.append(answer)
    
    return answers
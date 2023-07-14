import openai
from interface.standard import QuestionsRequest

openai.api_key = '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'

def questions_request(request: QuestionsRequest)-> [str]:
    answers = []
    try:
        for question in request.questions:
            prompt = f"{request.text}\n\nQuestion: {question}\nAnswer:"
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
    except Exception as e:
        print(f"Error: {str(e)}")  
        return e      
    return answers
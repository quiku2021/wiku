from pydantic import BaseModel
from pathlib import Path

class QuestionsRequest(BaseModel):
    text: str
    questions: list[str]

class Save_file(BaseModel):
    status: bool
    url_file: Path
    
class Validate_format(BaseModel):
    status: bool
    type_file: str
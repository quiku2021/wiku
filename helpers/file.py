import main
from interface.types import type_extension
from interface.standard import Save_file, Validate_format
from fastapi import UploadFile, File
from pathlib import Path
import os
import shutil
from helpers.text import convert_pdf_to_text, convert_docx_to_text, convert_pptx_to_text, convert_rtf_to_text, convert_text_to_object, clean_text

def save_file(file: UploadFile = File(...)) -> Save_file:
    is_valid_format = validate_format(str(file.filename))
    if is_valid_format.status:
        file_destination = Path(main.url_location, "static", "documents", file.filename)
        if not os.path.exists(file_destination):
            os.makedirs(os.path.dirname(file_destination), exist_ok=True)
            with open(file_destination, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        return Save_file(status= True, url_file= file_destination)
    return Save_file(status= False, url_file= '')

def validate_format(extension_name:str) -> Validate_format:
    status = False
    type_file = ''
    for ext in type_extension:
        if extension_name.endswith(type_extension[ext]):
            status = True
            type_file = type_extension[ext]
            break
    return Validate_format(status=status, type_file= type_file)

def file_converter(url_file:Path):
    file = validate_format(str(url_file))
    if file.status:
        if file.type_file == type_extension['PDF']:
            text = convert_pdf_to_text(url_file)
        elif file.type_file == type_extension['WORD']:
            text = convert_docx_to_text(url_file)
        elif file.type_file == type_extension['PWP']:
            text = convert_pptx_to_text(url_file)
        elif file.type_file == type_extension['RTF']:
            text = convert_rtf_to_text(url_file)
        return convert_text_to_object(clean_text(text))
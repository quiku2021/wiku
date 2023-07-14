from fastapi import APIRouter, HTTPException, status, UploadFile, File
from interface.items import Item
from interface.standard import Save_file
from helpers.file import file_converter, save_file

router = APIRouter()
router = APIRouter(prefix="/items",
                tags=["items"],
                responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

@router.get("/")
async def items():
    return "items_list"

@router.get("/{id}")
async def item(id: int):
    pass

@router.post("/")
async def create_item(id: int, file: UploadFile = File(...)):
    response = save_file(file)
    if response.status: 
        data = file_converter(response.url_file)
    return data

@router.delete("/{id}")
async def item(id: int):
    pass
 

from fastapi import APIRouter, Depends
from .auth import auth
from auth_lib.fastapi import UnionAuth
from pydantic import Field
from app.schema import BaseModel
from app.utils import run


router = APIRouter()


class Input(BaseModel):
    repo_url: str = Field(
        description='url репозитория, строка',
        example='https://github.com/profcomff/print-api.git'
    )
    commit_hash: str = Field(        
        description='хеш коммита, строка',
        example='f7cf8ea038edfb31cc8f7dd880dbb53e61980d8c')

class SendOutput(BaseModel):
    code: int = Field(
        description='exit-code выполнения скрипта',
        example='0'
    )


@router.post(
    "/run",
    response_model = SendOutput
)
async def run_script(inp: Input, user: UnionAuth = Depends(auth)):
    """запускает баш скрипт, зависящий от переданных параметров"""
    code= await run(f"./script.sh {inp.commit_hash} {inp.repo_url}")
    return {
        'code': code
    }

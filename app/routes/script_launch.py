from fastapi import APIRouter, Depends
from .auth import auth
from auth_lib.fastapi import UnionAuth
from pydantic import Field
from app.schema import BaseModel
from app.utils.scripts import run


router = APIRouter()


class Input(BaseModel):
    repo_url: str = Field(
        description='url of repository, str',
        example='https://github.com/profcomff/print-api.git'
    )
    commit_hash: str = Field(        
        description='commit hash, str',
        example='f7cf8ea038edfb31cc8f7dd880dbb53e61980d8c')

class SendOutput(BaseModel):
    code: int = Field(
        description='exit-code of the script you launched',
        example='0'
    )


@router.post(
    '/{action:str}',
    response_model = SendOutput
)
async def run_script(action: str, inp: Input, user: UnionAuth = Depends(auth)):
    """runs a bash script, located in scripts/{action}. The script takes 2 arguments: commit_hash and repo_url"""
    code= await run(f"./scripts/{action}.sh   --repo_url {inp.repo_url} --commit_hash {inp.commit_hash}")
    return {
        'code': code
    }

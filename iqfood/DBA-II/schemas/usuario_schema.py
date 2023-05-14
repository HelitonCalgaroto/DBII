from typing import Optional
from pydantic import BaseModel, EmailStr

class UsuariosSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        orm_mode = True

class UsuarioSchemaCreate(UsuariosSchema):
    senha: str

class UsuarioSchemaUp(UsuariosSchema):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional [bool]
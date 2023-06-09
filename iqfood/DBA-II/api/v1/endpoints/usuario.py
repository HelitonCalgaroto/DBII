<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException, status, Response
=======
from fastapi import APIRouter, Depends, HTTPException, Response, status
>>>>>>> 832ce3b2250a9447fa443bbb9906a723e922956f
from typing import List
from sqlalchemy.future import select
from core.deps import get_session
from sqlalchemy.exc import IntegrityError

from sqlalchemy.ext.asyncio import AsyncSession
from schemas.usuario_schema import UsuarioSchemaCreate, UsuarioSchemaUp, UsuariosSchemaBase
from models.usuario_model import UsuarioModel

router = APIRouter()

@router.get('/', response_model=List[UsuariosSchemaBase])
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios: List[UsuariosSchemaBase] = result.scalars().unique().all()
        return usuarios
    
@router.get('/{usuario_id}', 
            response_model=UsuariosSchemaBase,
            status_code=status.HTTP_200_OK)
async def get_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario: UsuariosSchemaBase = result.scalars().one_or_none()
        
        if usuario:
            return usuario
        else:
            raise HTTPException(detail="Usuario nao encontrado",
                                status_code=status.HTTP_404_NOT_FOUND)

@router.post('/singup', status_code=status.HTTP_201_CREATED,
            response_model=UsuariosSchemaBase)
async def post_usuario(usuario: UsuarioSchemaCreate,
                    db: AsyncSession = Depends(get_session)):
    novo_usuario: UsuarioModel = UsuarioModel(nome=usuario.nome,
                                            sobrenome=usuario.sobrenome,
                                            email=usuario.email,
                                            senha=usuario.senha,
                                            eh_admin=usuario.eh_admin)
    async with db as session:
        try:
            session.add(novo_usuario)
            await session.commit()
            return novo_usuario
        except IntegrityError as e:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='Ja existe esse e-mail cadastrado, {e}')
                
@router.put('/{usuario_id}',
            response_model=UsuariosSchemaBase,
            status_code=status.HTTP_202_ACCEPTED)
async def put_usuario(usuario_id: int,
                    usuario: UsuarioSchemaUp,
                    db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_up: UsuariosSchemaBase = result.scalars().unique().one_or_none()
        
        if usuario_up:
            if usuario.nome:
                usuario_up.nome = usuario.nome
            if usuario.sobrenome:
                usuario_up.sobrenome = usuario.sobrenome
            if usuario.email:
                usuario_up.email = usuario.email
            if usuario.senha:
                usuario_up.senha = usuario.senha
            if usuario.eh_admin:
                usuario_up.eh_admin = usuario.eh_admin
            await session.commit()
            return usuario_up
        else:
            raise HTTPException(detail="Usuario nao encontrado",
                                status_code=status.HTTP_404_NOT_FOUND)
            
@router.delete('/{usuario_id}', status_code=status.HTTP_404_NOT_FOUND)
async def delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_del: UsuariosSchemaBase = result.scalars().one_or_none()
        
        if usuario_del:
            await session.delete(usuario_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Usuario nao encontrado",
                                status_code=status.HTTP_404_NOT_FOUND)

@router.get('/{usuario_id}', response_model=UsuariosSchemaBase, status_code=status.HTTP_200_OK)
async def get_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario: UsuariosSchemaBase = result.scalars().one_or_none()

        if usuario:
            return usuario
        else:
            raise HTTPException(detail="Usuario não encontrado", status_code=status.HTTP_404_NOT_FOUND)
from fastapi import APIRouter, Response, status

from app.api.deps import SessionDep
from app.models.legacy import Cliente, Usuario
from app.schemas.personas import (
    ClienteCreate,
    ClienteRead,
    ClienteUpdate,
    UsuarioCreate,
    UsuarioRead,
    UsuarioUpdate,
)
from app.services import CRUDService

router = APIRouter()
clientes = CRUDService[Cliente, ClienteCreate, ClienteUpdate](Cliente, "idCliente")
usuarios = CRUDService[Usuario, UsuarioCreate, UsuarioUpdate](Usuario, "idUsuario")


@router.get("/clientes", response_model=list[ClienteRead])
async def list_clientes(session: SessionDep, offset: int = 0, limit: int = 50):
    return await clientes.list(session, offset, limit)


@router.post("/clientes", response_model=ClienteRead, status_code=status.HTTP_201_CREATED)
async def create_cliente(payload: ClienteCreate, session: SessionDep):
    return await clientes.create(session, payload)


@router.get("/clientes/{cliente_id}", response_model=ClienteRead)
async def get_cliente(cliente_id: int, session: SessionDep):
    return await clientes.get(session, cliente_id)


@router.patch("/clientes/{cliente_id}", response_model=ClienteRead)
async def update_cliente(cliente_id: int, payload: ClienteUpdate, session: SessionDep):
    return await clientes.update(session, cliente_id, payload)


@router.delete("/clientes/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cliente(cliente_id: int, session: SessionDep):
    await clientes.delete(session, cliente_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/usuarios", response_model=list[UsuarioRead])
async def list_usuarios(session: SessionDep, offset: int = 0, limit: int = 50):
    return await usuarios.list(session, offset, limit)


@router.post("/usuarios", response_model=UsuarioRead, status_code=status.HTTP_201_CREATED)
async def create_usuario(payload: UsuarioCreate, session: SessionDep):
    return await usuarios.create(session, payload)


@router.get("/usuarios/{usuario_id}", response_model=UsuarioRead)
async def get_usuario(usuario_id: int, session: SessionDep):
    return await usuarios.get(session, usuario_id)


@router.patch("/usuarios/{usuario_id}", response_model=UsuarioRead)
async def update_usuario(usuario_id: int, payload: UsuarioUpdate, session: SessionDep):
    return await usuarios.update(session, usuario_id, payload)

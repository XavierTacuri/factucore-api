from fastapi import APIRouter, Depends, status

from app.api.deps import SessionDep, require_roles
from app.schemas.auth import CurrentUserResponse
from app.schemas.clients import ClientCreate, ClientRead, ClientUpdate
from app.services.clients import clients


router = APIRouter()
AllowedClientUser = Depends(require_roles(["admin", "cajero"]))


@router.post("", response_model=ClientRead, status_code=status.HTTP_201_CREATED)
async def create_client(
    payload: ClientCreate,
    session: SessionDep,
    current_user: CurrentUserResponse = AllowedClientUser,
):
    return await clients.create(session, payload)


@router.get("", response_model=list[ClientRead])
async def list_clients(
    session: SessionDep,
    offset: int = 0,
    limit: int = 50,
    current_user: CurrentUserResponse = AllowedClientUser,
):
    return await clients.list(session, offset, limit)


@router.get("/cedula/{cedula}", response_model=ClientRead)
async def get_client_by_cedula(
    cedula: str,
    session: SessionDep,
    current_user: CurrentUserResponse = AllowedClientUser,
):
    return await clients.get_by_cedula(session, cedula)


@router.patch("/cedula/{cedula}", response_model=ClientRead)
async def update_client_by_cedula(
    cedula: str,
    payload: ClientUpdate,
    session: SessionDep,
    current_user: CurrentUserResponse = AllowedClientUser,
):
    return await clients.update_by_cedula(session, cedula, payload)

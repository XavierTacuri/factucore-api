from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import SessionDep, get_current_active_user, require_roles
from app.schemas.auth import CurrentUserResponse
from app.schemas.users import UserCreate, UserRead, UserUpdate
from app.services.users import users


router = APIRouter()


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, session: SessionDep):
    return await users.create(session, payload)


@router.get("", response_model=list[UserRead])
async def list_users(
    session: SessionDep,
    offset: int = 0,
    limit: int = 50,
    current_user: CurrentUserResponse = Depends(require_roles(["admin"])),
):
    return await users.list(session, offset, limit)


@router.get("/{idUsuario}", response_model=UserRead)
async def get_user(
    idUsuario: int,
    session: SessionDep,
    current_user: CurrentUserResponse = Depends(get_current_active_user),
):
    if current_user.rolNombre.lower() != "admin" and current_user.idUsuario != idUsuario:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permisos insuficientes",
        )
    return await users.get(session, idUsuario)


@router.patch("/{idUsuario}", response_model=UserRead)
async def update_user(
    idUsuario: int,
    payload: UserUpdate,
    session: SessionDep,
    current_user: CurrentUserResponse = Depends(require_roles(["admin"])),
):
    return await users.update(session, idUsuario, payload)

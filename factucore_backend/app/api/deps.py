from typing import Annotated
from collections.abc import Sequence

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.core.security import decode_access_token
from app.models.legacy import Rol, Usuario
from app.schemas.auth import CurrentUserResponse


SessionDep = Annotated[AsyncSession, Depends(get_session)]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def _credentials_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )


async def get_current_user(
    session: SessionDep,
    token: Annotated[str, Depends(oauth2_scheme)],
) -> CurrentUserResponse:
    payload = decode_access_token(token)
    if payload is None:
        raise _credentials_exception()

    subject = payload.get("sub")
    if subject is None:
        raise _credentials_exception()

    try:
        user_id = int(subject)
    except (TypeError, ValueError):
        raise _credentials_exception() from None

    result = await session.execute(
        select(Usuario, Rol)
        .join(Rol, Usuario.idRol == Rol.idRol)
        .where(Usuario.idUsuario == user_id)
    )
    row = result.one_or_none()
    if row is None:
        raise _credentials_exception()

    user, rol = row
    return CurrentUserResponse(
        idUsuario=user.idUsuario,
        userUsuario=user.userUsuario,
        userNombre=user.userNombre,
        userApellido=user.userApellido,
        userMail=user.userMail,
        userEstado=user.userEstado,
        idRol=user.idRol,
        rolNombre=rol.rolNombre,
    )


async def get_current_active_user(
    current_user: Annotated[CurrentUserResponse, Depends(get_current_user)],
) -> CurrentUserResponse:
    if current_user.userEstado is not True:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario desactivado",
        )
    return current_user


def require_roles(allowed_roles: Sequence[str]):
    normalized_roles = {role.lower() for role in allowed_roles}

    async def role_checker(
        current_user: Annotated[CurrentUserResponse, Depends(get_current_active_user)],
    ) -> CurrentUserResponse:
        if current_user.rolNombre.lower() not in normalized_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permisos insuficientes",
            )
        return current_user

    return role_checker

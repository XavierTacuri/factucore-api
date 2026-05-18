from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from app.api.deps import SessionDep, get_current_active_user, require_roles
from app.core.security import create_access_token, verify_password
from app.models.legacy import Rol, Usuario
from app.schemas.auth import CurrentUserResponse, LoginRequest, TokenResponse


router = APIRouter()


def _public_user_response(user: Usuario, rol: Rol) -> CurrentUserResponse:
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


def _invalid_credentials_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Usuario o contrasena incorrectos",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest, session: SessionDep):
    result = await session.execute(
        select(Usuario, Rol)
        .join(Rol, Usuario.idRol == Rol.idRol)
        .where(Usuario.userUsuario == payload.username)
    )
    row = result.one_or_none()
    if row is None:
        raise _invalid_credentials_exception()

    user, rol = row
    if not verify_password(payload.password, user.userClave):
        raise _invalid_credentials_exception()

    if user.userEstado is not True:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario desactivado",
        )

    access_token = create_access_token(
        subject=str(user.idUsuario),
        username=user.userUsuario,
        role=rol.rolNombre,
    )
    return TokenResponse(
        access_token=access_token,
        user=_public_user_response(user, rol),
    )


@router.get("/me", response_model=CurrentUserResponse)
async def read_me(
    current_user: CurrentUserResponse = Depends(get_current_active_user),
):
    return current_user


@router.get("/admin-check", response_model=CurrentUserResponse)
async def admin_check(
    current_user: CurrentUserResponse = Depends(require_roles(["admin"])),
):
    return current_user

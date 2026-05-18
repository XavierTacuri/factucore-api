from fastapi import HTTPException, status
from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.models.legacy import Rol, Usuario
from app.schemas.users import UserCreate, UserRead, UserUpdate


class UserService:
    def _to_read(self, user: Usuario, rol: Rol) -> UserRead:
        return UserRead(
            idUsuario=user.idUsuario,
            userCedula=user.userCedula,
            userNombre=user.userNombre,
            userApellido=user.userApellido,
            userFono=user.userFono,
            userDireccion=user.userDireccion,
            userMail=user.userMail,
            userUsuario=user.userUsuario,
            userEstado=user.userEstado,
            idRol=user.idRol,
            rolNombre=rol.rolNombre,
        )

    async def list(self, session: AsyncSession, offset: int = 0, limit: int = 50) -> list[UserRead]:
        result = await session.execute(
            select(Usuario, Rol)
            .join(Rol, Usuario.idRol == Rol.idRol)
            .offset(offset)
            .limit(limit)
        )
        return [self._to_read(user, rol) for user, rol in result.all()]

    async def get(self, session: AsyncSession, user_id: int) -> UserRead:
        result = await session.execute(
            select(Usuario, Rol)
            .join(Rol, Usuario.idRol == Rol.idRol)
            .where(Usuario.idUsuario == user_id)
        )
        row = result.one_or_none()
        if row is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado",
            )
        user, rol = row
        return self._to_read(user, rol)

    async def create(self, session: AsyncSession, payload: UserCreate) -> UserRead:
        rol = await session.get(Rol, payload.idRol)
        if rol is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Rol no encontrado",
            )

        existing_result = await session.execute(
            select(Usuario).where(
                or_(
                    Usuario.userUsuario == payload.userUsuario,
                    Usuario.userMail == payload.userMail,
                )
            )
        )
        existing_user = existing_result.scalar_one_or_none()
        if existing_user is not None:
            if existing_user.userUsuario == payload.userUsuario:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="userUsuario ya existe",
                )
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="userMail ya existe",
            )

        user = Usuario(
            userCedula=payload.userCedula,
            userNombre=payload.userNombre,
            userApellido=payload.userApellido,
            userFono=payload.userFono,
            userDireccion=payload.userDireccion,
            userFecha="",
            userMail=payload.userMail,
            userUsuario=payload.userUsuario,
            userClave=hash_password(payload.password),
            userEstado=True,
            userPrincipal=False,
            idRol=payload.idRol,
        )

        session.add(user)
        await session.commit()
        await session.refresh(user)

        return self._to_read(user, rol)

    async def update(self, session: AsyncSession, user_id: int, payload: UserUpdate) -> UserRead:
        result = await session.execute(
            select(Usuario, Rol)
            .join(Rol, Usuario.idRol == Rol.idRol)
            .where(Usuario.idUsuario == user_id)
        )
        row = result.one_or_none()
        if row is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado",
            )

        user, rol = row
        for key, value in payload.model_dump(exclude_unset=True).items():
            setattr(user, key, value)

        session.add(user)
        await session.commit()
        await session.refresh(user)

        return self._to_read(user, rol)


users = UserService()

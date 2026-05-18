from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.legacy import Cliente
from app.schemas.clients import ClientCreate, ClientRead, ClientUpdate


def validate_ecuadorian_id_number(cedula: str) -> bool:
    # TODO: Implement Ecuadorian ID validation algorithm later.
    return True


class ClientService:
    def _to_read(self, client: Cliente) -> ClientRead:
        return ClientRead(
            idCliente=client.idCliente,
            cedula=client.cedula,
            cli_nombre=client.cli_nombre,
            cli_apellido=client.cli_apellido,
            cli_telefono=client.cli_telefono,
            cli_direccion=client.cli_direccion,
            cli_mail=client.cli_mail,
            cli_descripcion=client.cli_descripcion,
        )

    async def list(self, session: AsyncSession, offset: int = 0, limit: int = 50) -> list[ClientRead]:
        result = await session.execute(select(Cliente).offset(offset).limit(limit))
        return [self._to_read(client) for client in result.scalars().all()]

    async def get_by_cedula(self, session: AsyncSession, cedula: str) -> ClientRead:
        client = await self._get_model_by_cedula(session, cedula)
        return self._to_read(client)

    async def create(self, session: AsyncSession, payload: ClientCreate) -> ClientRead:
        cedula = payload.cedula.strip()
        if not cedula:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="La cedula no puede estar vacia",
            )
        if not validate_ecuadorian_id_number(cedula):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Cedula invalida",
            )

        existing = await session.execute(select(Cliente).where(Cliente.cedula == cedula))
        if existing.scalar_one_or_none() is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Ya existe un cliente con esa cedula",
            )

        client = Cliente(
            cedula=cedula,
            cli_nombre=payload.cli_nombre,
            cli_apellido=payload.cli_apellido,
            cli_telefono=payload.cli_telefono,
            cli_direccion=payload.cli_direccion,
            cli_mail=str(payload.cli_mail) if payload.cli_mail is not None else "",
            cli_descripcion=payload.cli_descripcion,
        )
        session.add(client)
        await session.commit()
        await session.refresh(client)
        return self._to_read(client)

    async def update_by_cedula(
        self,
        session: AsyncSession,
        cedula: str,
        payload: ClientUpdate,
    ) -> ClientRead:
        data = payload.model_dump(exclude_unset=True)
        if not data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Debe enviar al menos un campo para actualizar",
            )

        client = await self._get_model_by_cedula(session, cedula)
        for key, value in data.items():
            setattr(client, key, str(value) if key == "cli_mail" and value is not None else value)

        session.add(client)
        await session.commit()
        await session.refresh(client)
        return self._to_read(client)

    async def _get_model_by_cedula(self, session: AsyncSession, cedula: str) -> Cliente:
        result = await session.execute(select(Cliente).where(Cliente.cedula == cedula))
        client = result.scalar_one_or_none()
        if client is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente no encontrado",
            )
        return client


clients = ClientService()

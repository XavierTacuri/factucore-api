from typing import Any, Generic, TypeVar

from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel


ModelT = TypeVar("ModelT", bound=SQLModel)
CreateT = TypeVar("CreateT", bound=BaseModel)
UpdateT = TypeVar("UpdateT", bound=BaseModel)


class CRUDService(Generic[ModelT, CreateT, UpdateT]):
    def __init__(self, model: type[ModelT], pk_name: str):
        self.model = model
        self.pk_name = pk_name

    async def list(self, session: AsyncSession, offset: int = 0, limit: int = 50) -> list[ModelT]:
        result = await session.execute(select(self.model).offset(offset).limit(limit))
        return list(result.scalars().all())

    async def get(self, session: AsyncSession, object_id: int) -> ModelT:
        obj = await session.get(self.model, object_id)
        if obj is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recurso no encontrado")
        return obj

    async def create(self, session: AsyncSession, payload: CreateT) -> ModelT:
        obj = self.model(**payload.model_dump())
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def update(self, session: AsyncSession, object_id: int, payload: UpdateT) -> ModelT:
        obj = await self.get(session, object_id)
        data: dict[str, Any] = payload.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(obj, key, value)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(self, session: AsyncSession, object_id: int) -> None:
        obj = await self.get(session, object_id)
        await session.delete(obj)
        await session.commit()

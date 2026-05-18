from fastapi import APIRouter, status

from app.api.deps import SessionDep
from app.schemas.users import UserCreate, UserRead
from app.services.users import users


router = APIRouter()


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, session: SessionDep):
    return await users.create(session, payload)

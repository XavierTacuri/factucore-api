from fastapi import APIRouter, status

from app.api.deps import SessionDep
from app.models.legacy import Proforma
from app.schemas.proformas import ProformaCreate, ProformaRead, ProformaUpdate
from app.services import CRUDService

router = APIRouter()
proformas = CRUDService[Proforma, ProformaCreate, ProformaUpdate](Proforma, "idProforma")


@router.get("", response_model=list[ProformaRead])
async def list_proformas(session: SessionDep, offset: int = 0, limit: int = 50):
    return await proformas.list(session, offset, limit)


@router.post("", response_model=ProformaRead, status_code=status.HTTP_201_CREATED)
async def create_proforma(payload: ProformaCreate, session: SessionDep):
    return await proformas.create(session, payload)


@router.get("/{proforma_id}", response_model=ProformaRead)
async def get_proforma(proforma_id: int, session: SessionDep):
    return await proformas.get(session, proforma_id)


@router.patch("/{proforma_id}", response_model=ProformaRead)
async def update_proforma(proforma_id: int, payload: ProformaUpdate, session: SessionDep):
    return await proformas.update(session, proforma_id, payload)

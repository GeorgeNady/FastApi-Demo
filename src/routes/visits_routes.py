from fastapi import APIRouter
from src.models.visit_model import Visit

router = APIRouter(prefix='/api/v1/visits', tags=['Visits'])


@router.get('')
async def find_all_visits():
    return ''


@router.get("/{id}")
async def find_visit_by_id(id: int):
    return ''


@router.post('')
async def create_visit(visit: Visit):
    return ''


@router.put("/{id}")
async def update_visit(id: int, visit: Visit):
    return ''


@router.delete("/{id}")
async def delete_visit(id: int):
    return ''

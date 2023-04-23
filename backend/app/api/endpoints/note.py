from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.session import get_db
from backend.app.schemas.note import NoteModel
from backend.app.models.note import Note, CreateNote, NoteUpdate
from backend.app.crud.note import get_note_by_id, delete_note, update_note, create_note

note_router = APIRouter()


@note_router.post('/note', response_model=NoteModel)
def create_notes(note: CreateNote, db: Session = Depends(get_db)) -> Note:
    created_note = create_note(db, note)
    return created_note


@note_router.get('/note/{note_id}', response_model=NoteModel)
def get_note(note_id: int, db: Session = Depends(get_db)) -> Note:
    if db_note := get_note_by_id(db, note_id):
        return db_note
    else:
        raise HTTPException(status_code=404, detail=f"Note does\'t with id={note_id} exist")


@note_router.put('/note/{note_id}', response_model=NoteModel)
def update_notes(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)) -> Note:
    if db_note := get_note_by_id(db, note_id):
        updated_note = update_note(db, db_note, note)
        return updated_note
    else:
        raise HTTPException(status_code=404, detail=f"Note does\'t with id={note_id} exist")


@note_router.delete('/note/{note_id}')
def delete_notes(note_id: int, db: Session = Depends(get_db)):
    if db_note := get_note_by_id(db, note_id):
        delete_note(db, db_note)
        return {"detail": f"Note with id={note_id} has been deleted"}
    else:
        raise HTTPException(status_code=404, detail=f"Note does\'t with id={note_id} exist")

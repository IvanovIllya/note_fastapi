from sqlalchemy.orm import Session

from backend.app.schemas.note import NoteCreateModel
from backend.app.core.config import Settings

from backend.app.crud.note import create_init_note


settings = Settings()


def init_db(db: Session):
    create_note(db)


def create_note(db: Session):
    for note in settings.INIT_NOTES:
        db_note = NoteCreateModel(
            title=note['title'],
            text=note['text']
        )
        create_init_note(db, db_note)
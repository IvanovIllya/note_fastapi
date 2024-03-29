from pydantic import BaseModel


class NoteBaseModel(BaseModel):
    title: str
    text: str


class NoteCreateModel(NoteBaseModel):
    pass


class NoteModel(NoteBaseModel):
    id: int

    class Config:
        orm_mode = True


class NoteUpdateModel(NoteBaseModel):
    pass

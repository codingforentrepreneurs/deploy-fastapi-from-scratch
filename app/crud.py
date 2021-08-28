# create retrieve update and delete
from sqlalchemy.orm import Session

from models import Entry
from schema import EntryCreateSchema

def create_entry(db:Session, entry_obj:EntryCreateSchema):
    """
    1. Validate incoming data via EntryCreateSchema
    2. Save (commit) data to database
    3. Return stored data
    """
    obj = Entry(**entry_obj.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj



def get_entries(db:Session):
    return db.query(Entry).all()
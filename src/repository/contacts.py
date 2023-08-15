from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Contact
from src.schemas import ContactsSchema, ContactsUpdateSchema


async def get_contacts(limit: int, offset: int, db: AsyncSession):
    sq = select(Contact).offset(offset).limit(limit)
    contacts = await db.execute(sq)
    return contacts.scalars().all()


async def get_contact(contacts_id: int, db: AsyncSession):
    sq = select(Contact).filter_by(id=contacts_id)
    contact = await db.execute(sq)
    return contact.scalar_one_or_none()


async def create_contact(body: ContactsSchema, db: AsyncSession):
    contact = Contact(name=body.name, surname=body.surname, email=body.email, phone=body.phone, bd=body.bd, city=body.city, notes=body.notes)
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


async def update_contact(todo_id: int, body: ContactsUpdateSchema, db: AsyncSession):
    sq = select(Contact).filter_by(id=todo_id)
    result = await db.execute(sq)
    contact = result.scalar_one_or_none()
    if contact:
        contact.name = body.name
        contact.surname = body.surname
        contact.email = body.email
        contact.phone = body.phone
        contact.bd = body.bd
        contact.city = body.city
        contact.notes = body.notes
        await db.commit()
        await db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: AsyncSession):
    sq = select(Contact).filter_by(id=contact_id)
    result = await db.execute(sq)
    contact = result.scalar_one_or_none()
    if contact:
        await db.delete(contact)
        await db.commit()
    return contact
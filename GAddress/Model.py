from peewee import *
import  datetime
db = SqliteDatabase('addressbook.db')



class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    timestamp = DateTimeField(default=datetime.datetime.now)

    def find_user_group(self):
        return Group.select().join(PersonGroup, on=PersonGroup.GroupModel).where(PersonGroup.PersonModel == self)

    def find_user_email(self):
        return Email.select().where(Email.PersonModel == self)

    def find_user_phone(self):
        return PhoneNumber.select().where(PhoneNumber.PersonModel == self)


class Address(BaseModel):
    PersonModel = ForeignKeyField(Person)
    address = CharField(max_length=150)
    timestamp = DateTimeField(default=datetime.datetime.now)


class Email(BaseModel):
    PersonModel = ForeignKeyField(Person)
    email = CharField()
    timestamp = DateTimeField(default=datetime.datetime.now)


class PhoneNumber(BaseModel):
    PersonModel = ForeignKeyField(Person)
    phone = CharField(max_length=10)
    timestamp = DateTimeField(default=datetime.datetime.now)
    indexes = (
        # create a unique on from/to/date
        (('PersonModel', 'phone'), True)
    )


class Group(BaseModel):
    group_name = CharField(max_length=10,unique=True)
    timestamp = DateTimeField(default=datetime.datetime.now)
    def find_group_member(self):
        return Person.select().join(PersonGroup, on=PersonGroup.GroupModel).where(PersonGroup.GroupModel == self)



class PersonGroup(BaseModel):
    PersonModel = ForeignKeyField(Person)
    GroupModel = ForeignKeyField(Group)
    timestamp = DateTimeField(default=datetime.datetime.now)
    indexes = (
        # create a unique on from/to/date
        (('PersonModel', 'GroupModel'), True)
    )


def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Person, Address, Email, PhoneNumber, Group, PersonGroup], safe=True)
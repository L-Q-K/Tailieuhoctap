from mongoengine import Document,StringField,IntField
from faker import Faker

class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()


def dump_data():
    f = Faker()
    for i in range(10):
        girl_type = GirlType(name= f.name(),
                            image ="https://scontent.fhan2-2.fna.fbcdn.net/v/t1.0-9/21231970_1268874116568075_7579785202963276134_n.jpg?oh=7c1cf863453941e309f6924888435fe6&oe=5A42ED82",
                            description= f.text())
        #girl_type.save()

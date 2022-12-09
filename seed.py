from app import app
from models import Pet, db


pet1 = Pet(name='Frank', species='Dog', photo_url='http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcQfpVsa4UHm3fFJpQgij7Ir-ATJZUgwMSbW_Jy2e0w7br_TJtUg65LxQrdhN66WfyXly7eMMUqH_e1mMCQ',
           age=5, notes='A good boy', available=False)
pet2 = Pet(name='Mittens', species='Cat', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSm8ErlMlPdnS5zbhJ2KL339H-cCsjrxjMl8A&usqp=CAU',
           age=1, notes='The Devil', available=True)
pet3 = Pet(name='Ham', species='Porcupine',
           age=1, available=True)


with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all([pet1, pet2, pet3])
    db.session.commit()

    db.session.close()

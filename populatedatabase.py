from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import SportCategory, Base, SportingItem, User

engine = create_engine('sqlite:///sportcatalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
User1 = User(name="Schevon Joseph", email="chevtech123@gmail.com",
             picture='''https://pbs.twimg.com/profile_images/2671170543/
             18debd694829ed78203a5a36dd364160_400x400.png''')
session.add(User1)
session.commit()
# Insert a sports category record into the db
sportsCategory1 = SportCategory(name="Soccer", userId=1)

session.add(sportsCategory1)
session.commit()

# Insert a Sporting Item record into the db
sportingItem1 = SportingItem(name="Goal Keeping Gloves", userId=1,
                             description="Gloves provides a better grip",
                             sport=sportsCategory1)

session.add(sportingItem1)
session.commit()

sportingItem2 = SportingItem(name="Soccer cleats", userId=1,
                             description="Soccer Cleats are made of rubber",
                             sport=sportsCategory1)

session.add(sportingItem2)
session.commit()

sportingItem3 = SportingItem(name="Shin Guards", userId=1,
                             description="Provides protection to player shins",
                             sport=sportsCategory1)

session.add(sportingItem3)
session.commit()

sportingItem4 = SportingItem(name="Socks", userId=1,
                             description="Socks are usually knee length",
                             sport=sportsCategory1)

session.add(sportingItem4)
session.commit()

sportingItem5 = SportingItem(name="Shorts", userId=1,
                             description="Soccer shorts are  above the knee",
                             sport=sportsCategory1)

session.add(sportingItem5)
session.commit()

sportsCategory2 = SportCategory(name="BaseBall", userId=1)

session.add(sportsCategory2)
session.commit()

sportingItem6 = SportingItem(name="BaseBall Gloves", userId=1,
                             description="Assist  in catching baseballs",
                             sport=sportsCategory2)

session.add(sportingItem6)
session.commit()

sportingItem7 = SportingItem(name="BaseBall Bat", userId=1,
                             description="Small wooded or metal club",
                             sport=sportsCategory2)

session.add(sportingItem7)
session.commit()

sportingItem8 = SportingItem(name="BaseBall ", userId=1,
                             description="Assist players in catching balls",
                             sport=sportsCategory2)

session.add(sportingItem8)
session.commit()

sportingItem9 = SportingItem(name="BaseBall Helmet", userId=1,
                             description="A protective head gear",
                             sport=sportsCategory2)

session.add(sportingItem9)
session.commit()

sportingItem10 = SportingItem(name="Bat Bag", userId=1,
                              description="Item used to house baseball bats",
                              sport=sportsCategory2)

session.add(sportingItem10)
session.commit()

print "added menu items!"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import SportCategory, Base, SportingItem,User

engine = create_engine('sqlite:///sportcatalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
User1 = User(name="Schevon Joseph", email="chevtech123@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()
# Menu for UrbanBurger
sportsCategory1 = SportCategory(name="Soccer",userId=1)

session.add(sportsCategory1)
session.commit()

sportingItem1 = SportingItem(name="Goal Keeping Gloves", userId=1,description="Goalie Gloves provides a better grip on the ball",
                      sport=sportsCategory1)

session.add(sportingItem1)
session.commit()

sportingItem2 = SportingItem(name="Soccer cleats",userId=1, description="Soccer Cleats are like baseball cleats but are short and made of rubber",
                      sport=sportsCategory1)

session.add(sportingItem2)
session.commit()

sportingItem3 = SportingItem(name="Shin Guards", userId=1,description="Provides protection to players' shins",
                      sport=sportsCategory1)

session.add(sportingItem3)
session.commit()

sportingItem4 = SportingItem(name="Socks",userId=1, description="Socks are usually thick and knee length",
                      sport=sportsCategory1)

session.add(sportingItem4)
session.commit()

sportingItem5 = SportingItem(name="Shorts", userId=1,description="Soccer shorts are just above the knee in length",
                      sport=sportsCategory1)

session.add(sportingItem5)
session.commit()

sportsCategory2 = SportCategory(name="BaseBall",userId=1)

session.add(sportsCategory2)
session.commit()

sportingItem6 = SportingItem(name="BaseBall Gloves",userId=1, description="Assist players in catching and fielding baseballs",
                      sport=sportsCategory2)

session.add(sportingItem6)
session.commit()

sportingItem7 = SportingItem(name="BaseBall Bat",userId=1, description="Small wooded or metal club used to hit the ball thrown by the pitcher",
                      sport=sportsCategory2)

session.add(sportingItem7)
session.commit()

sportingItem8 = SportingItem(name="BaseBall ", userId=1,description="Assist players in catching and fielding baseballs",
                      sport=sportsCategory2)

session.add(sportingItem8)
session.commit()

sportingItem9 = SportingItem(name="BaseBall Helmet",userId=1, description="A protective head gear worn by batters",
                      sport=sportsCategory2)

session.add(sportingItem9)
session.commit()

sportingItem10 = SportingItem(name="Bat Bag",userId=1, description="Item used to house baseball bats",
                      sport=sportsCategory2)

session.add(sportingItem10)
session.commit()

print "added menu items!"

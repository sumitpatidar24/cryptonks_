from createdb import db

db.mycur.execute("select * from bitcoin")
for x in db.mycur:
    print(x)
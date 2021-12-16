import mysql.connector as mc

class db:
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="root",
        database = "mainDB"
    )
    mycur = mydb.cursor()

    # mycur.execute("CREATE DATABASE mainDB")
    # mycur.execute("CREATE TABLE bitcoin (Id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, Price FLOAT, Min FLOAT, Max FLOAT,Date DATE, Time TIME)")
    # mycur.execute("ALTER TABLE bitcoin AUTO_INCREMENT=1")
    # mycur.execute("INSERT INTO bitcoin (Price, Min, Max) VALUES(100, 80, 120)")

    # sql = "INSERT INTO bitcoin (Price, Min, Max) VALUES (%s, %s, %s)"
    # val = [
    #     (100, 80, 190),
    #     (120, 40, 123),
    #     (130, 32, 180),
    #     (130, 55, 170),
    #     (150, 22, 160),
    #     (160, 84, 183),
    #     (105, 86, 176),
    #     (66, 60, 157),
    #     (130, 70, 143)
    # ]
    # mycur.executemany(sql, val)
    # mydb.commit()

    def insert(self, price, min, max):
        # if currdate is None and currtime is None:
        self.mycur.execute(f"INSERT INTO bitcoin (Price, Min, Max, Date, Time) VALUES ({price}, {min}, {max}, curdate(), curtime())")
        # else:
            # self.mycur.execute(f"INSERT INTO bitcoin (Price, Min, Max, Date, Time) VALUES ({price}, {min}, {max}, {currdate}, {currtime})")
        self.mydb.commit()


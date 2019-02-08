def db_configure():
    from application import pymysql

    database = pymysql.connect (
        host="localhost",
        user = "username",
        passwd = "password",
        db = "indotel",
        cursorclass=pymysql.cursors.DictCursor)

    return database

import pymysql

class Base:
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"

    )
    fcursor =bd.cursor()
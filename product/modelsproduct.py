from django.db import connection

class Product:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from products")
            datas = cursor.fetchall()
        return datas

    def create(self, product):
        with connection.cursor() as cursor:
            sql = """insert into products(categoryid,modelnumber,modelname,unitcost,productimage,description)
                            values(%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, product)
        
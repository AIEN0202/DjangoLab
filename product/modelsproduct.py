from django.db import connection

class Product:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from products")
            datas = cursor.fetchall()
        return datas
    
    def single(self, id):
        with connection.cursor() as cursor:
            cursor.execute("select * from products where productid=%s",(id,))
            data = cursor.fetchone()
        return data


    def create(self, product):
        with connection.cursor() as cursor:
            sql = """insert into products(categoryid,modelnumber,modelname,unitcost,productimage,description)
                            values(%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, product)
        
    def update(self, product):
        with connection.cursor() as cursor:
            sql = """update products set categoryid=%s, modelnumber=%s, modelname=%s,
                         unitcost=%s, productimage=%s, description=%s where productid=%s"""
            cursor.execute(sql,product)

    def delete(self, id):
        with connection.cursor() as cursor:
            sql = "delete from products where productid=%s"
            cursor.execute(sql,(id,))
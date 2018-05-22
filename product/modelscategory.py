from django.db import connection

class Category:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from categories")
            datas = cursor.fetchall()
        return datas

    # def create(self):
    #     pass

    # def update(self):
    #     pass
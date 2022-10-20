import mysql.connector
__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='//asdf1234@#--,,',
                                  host='127.0.0.1',
                                      database='grocery_store1',
                                      auth_plugin='mysql_native_password')
    return __cnx
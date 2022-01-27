

import mysql.connector as mysql
from algorithm import Sign

mysql_instance = mysql.connect(host='localhost', username='lucasf1', password='mysqluser1', database='lucasf1_bdd_1st')
mysql_cursor = mysql_instance.cursor()
table_pessoas = []
table_pessoas_json = []

Sign.mysql_select_table(_exec=mysql_cursor, temporary_database=table_pessoas)
Sign.json(target_table=table_pessoas, json_table=table_pessoas_json)

# Lista de tuplas
for object_ in table_pessoas:
    print(object_)

print('\n-----------------------------------------------------------------------------------------------------------\n')

# Lista de dicionários
for object_ in table_pessoas_json:
    print(object_)

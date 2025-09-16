import mysql.connector as sqlcon

mycon=sqlcon.connect(host='localhost',
                    user='root',
                    passwd='9@5Pra524')
mycur=mycon.cursor()

def create_db():
    create_database='CREATE DATABASE BLO'
    mycur.execute(create_database)

def select_db():
    select_database='USE BLO'
    mycur.execute(select_database)

def create_tb():
    create_table="""CREATE TABLE blo_cred
    (number bigint not null primary key,
    password varchar(15) not null,
    part_number int not null unique,
    name varchar(30) not null)"""
    mycur.execute(create_table)

def insert_user_passwd():
    insert_cred="""INSERT INTO blo_cred (number,password,part_number,name)
    values
    (9669677324,'Pr@teek524',99999,'Admin')"""
    mycur.execute(insert_cred)

# Revoking functions in their sequence
create_db()
select_db()
create_tb()
insert_user_passwd()

mycon.commit()
mycon.close()
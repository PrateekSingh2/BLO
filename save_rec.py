import mysql.connector as sqlcon

mycon=sqlcon.connect(host='localhost',
                    user='root',
                    passwd='9@5Pra524',
                    database='BLO')
mycur=mycon.cursor()

if __name__=='__main__':
    BLO.form6i()

global BLO.form6i.get_it()
import BLO
#epic_number_generate,name_fetch,fname_fetch,gender_fetch,date_fetch
query="INSERT INTO card_rec(epic,name,fname,gen,DOG) VALUES('{}','{}','{}','{}','{}')".format(epic_number_generate,name_fetch,fname_fetch,gender_fetch,date_fetch)

mycon.close()
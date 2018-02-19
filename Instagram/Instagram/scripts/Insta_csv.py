import MySQLdb
import csv
import os
import datetime

class Instagram(object):
    def __init__(self):
        user = 'root' # your username
        passwd = '' # your password
        host = 'localhost' # your host
        db = 'SAMPLE_INSTAGRAM' # db names must be in string variables can be used without s trings yesyes oops i forgot. :)
        self.con = MySQLdb.connect(user=user, host=host, db=db, passwd = passwd)
        self.cursor = self.con.cursor()
        self.filename = 'SampleInstagram.csv' # need to specify the file name for CSV
        self.fields = ['fullname', 'username', 'title','propicurl', 'logging_page_id','mutual_followers','biography'] 
        
    def main(self):
        try:
            query = 'SELECT * from Insta'
            self.cursor.execute(query)
            sql_data = self.cursor.fetchall()
            with open(self.filename, 'w+') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(self.fields)
                for sql_data1 in sql_data:
                    sql_data1=tuple(sql_data1)
                    csvwriter.writerow(sql_data1)
            self.cursor.close()
            self.con.close()
        except Exception, e:
                print str(e)

if __name__ == '__main__':
        Instagram().main()


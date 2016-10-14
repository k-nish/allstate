#coding:utf-8
from config import MYSQL
import mysql.connector
import glob, os
from contextlib import closing

files = glob.glob("*.csv")

db = mysql.connector.connect(**MYSQL)

with closing(db.cursor()) as dbcur:
    dbcur.execute("SET character_set_database=utf8;")
    for file in files:
        size = os.path.getsize(file)
        if size == 0:
            continue
        table = file.split(".")[0]
        dbcur.execute("TRUNCATE TABLE {}".format(table))
        sql = "LOAD DATA LOCAL INFILE '{0}' INTO TABLE {1} FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' IGNORE 1 LINES;".format(file, table)
        dbcur.execute(sql)


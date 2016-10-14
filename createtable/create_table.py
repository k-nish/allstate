# coding:utf-8
import mysql.connector
from config import MYSQL

dbcon = mysql.connector.connect(**MYSQL)
dbcur = dbcon.cursor()

dbcur.execute('''
    drop table if exists train;
    ''')

sql = '''
    create table train (
    id int,
    ''' + ','.join(['cat%03d varchar(31)' % (i,) for i in range(1,117)]) + ''',
    ''' + ','.join(['cont%02d float' % (i,) for i in range(1,15)]) + ''',
    loss float,
    primary key (id))
    engine = myisam default charset = utf8;
    '''

dbcur.execute(sql)

sql = '''
    create table test (
    id int,
    ''' + ','.join(['cat%03d varchar(31)' % (i,) for i in range(1,117)]) + ''',
    ''' + ','.join(['cont%02d float' % (i,) for i in range(1,15)]) + ''',
    primary key (id))
    engine = myisam default charset = utf8;
    '''

dbcur.execute(sql)
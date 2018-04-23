import pymysql
from sys import argv

tasks_list = []

def init():
    # initialize the task list
    try:
        # open the file
        #txt = open(filename)

        #SQL
        connection = pymysql.connect(user="root",password="dodo",database="lab5",host="localhost")
        sql = """
        SELECT todo
        FROM task
        WHERE done=FALSE;
        """
        cursor = connection.cursor()
        cursor.execute(sql)
        tasks_list = cursor.fetchall()
        cursor.close()
        connection.close()
        #fine sql
    except IOError:
        # File not found! We work with an empty list
        print("File not found!")
    return

def checkPresente(connection,testo):
    sql = """
        SELECT id
        FROM task
        WHERE (todo=%s)
        """
    cursor = connection.cursor()
    cursor.execute(sql, (testo,))
    trovato = cursor.fetchone()
    if trovato > 0:
        return trovato
    return -1


def newTask(testo):
    connection = pymysql.connect(user="root",password="dodo",database="lab5",host="localhost")
    cursor = connection.cursor()
    trovato = checkPresente(connection,testo)
    if trovato == -1:
        sql = """
        INSERT INTO task(todo,done)
        VALUES (%s,FALSE)
        """
        cursor.execute(sql, (testo,) )
        tasks_list.append(testo)
    cursor.close()
    connection.close()
    return #fai qualcosa se non trova

def showTasks():
    return tasks_list

def removeTask(testo):
    connection = pymysql.connect(user="root",password="dodo",database="lab5",host="localhost")
    presente = checkPresente(connection,testo)
    cursor = connection.cursor()
    if presente!=-1:
        sql = """
        UPDATE task
        SET done = 1
        WHERE todo = %s
        """
        cursor.execute(sql, (testo,) )
    #else:
    #errore

if __name__ == '__main__':
    # main program
    pass

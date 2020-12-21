import sqlite3

def connect():
    conn = sqlite3.connect('lolgraphp.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS lolgraphp (ID INTEGER PRIMARY KEY , EA text , ER text , ja1 text ,ja2 text,ja3 text,ja4 text,ja5 text,jr1 text,jr2 text,jr3 text,jr4 text,jr5 text)")
    conn.commit()
    conn.close()

def insert(ID, EA, ER,ja1,ja2,ja3,ja4, ja5,jr1,jr2,jr3,jr4,jr5):
    conn = sqlite3.connect('lolgraphp.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO lolgraphp VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)" , (ID, EA, ER, ja1,ja2,ja3,ja4, ja5,jr1,jr2,jr3,jr4,jr5))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('lolgraphp.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM lolgraphp")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(ID):
    conn = sqlite3.connect('lolgraphp.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM lolgraphp WHERE ID=? ", (ID,))
    conn.commit()
    conn.close()

def search(ID='' , EA='', ER='', ja1='',ja2='',ja3='',ja4='', ja5='',jr1='',jr2='',jr3='',jr4='',jr5=''):
    conn = sqlite3.connect('lolgraphp.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM lolgraphp WHERE ID=? OR EA=? OR ER=? OR ja1=? OR ja2=? OR ja3=? OR ja4=? OR ja5=? OR jr1=? OR jr2=? OR jr3=? OR jr4=? OR jr5=?" , (ID,EA, ER, ja1,ja2,ja3,ja4, ja5,jr1,jr2,jr3,jr4,jr5))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()

from sqlite3 import *


def createdb():
    sql = []
    sql.append(
        """CREATE TABLE IF NOT EXISTS competitions (
                id integer PRIMARY KEY,
                tournament text(30),
    	        compname text(30),
                compdate text(10),
                compstatus text(10),
                groups text(8),
                places text(3)
    );"""
    )

    sql.append(
        """CREATE TABLE IF NOT EXISTS tournaments (
                tournament text(30) PRIMARY KEY           
    );"""
    )

    sql.append(
        """CREATE TABLE IF NOT EXISTS ranklist (
    	        firstname text(20),
                surname text(30),
                pick text(5),
                points integer,
                position integer,
                tournament text(30),
                PRIMARY KEY(firstname, surname, pick, tournament)            
    );"""
    )

    sql.append(
        """CREATE TABLE IF NOT EXISTS players (
                rank_id integer,
                competition_id integer,
                group_name text(1),
                id integer,
                position integer,
                PRIMARY KEY(competition_id, rank_id)
    );"""
    )

    conn = connect("ttmanager.db")
    c = conn.cursor()

    for item in sql:
        c.execute(item)

    conn.commit()
    conn.close()


def compscontent() -> tuple:  # beolvassa a tárolt versenyek adatait
    try:
        conn = connect("ttmanager.db")
        sql = """SELECT id, compname, tournament, compdate, compstatus, groups, places 
                FROM competitions 
                ORDER BY tournament, compdate;"""
        cur = conn.cursor()
        cur.execute(sql)
        cc = cur.fetchall()
    except IndexError:
        cc = []
    conn.close()
    return cc


def tournaments() -> list:  # beolvassa a tárolt versenysorozatokat
    try:
        conn = connect("ttmanager.db")
        sql = """SELECT * FROM tournaments;"""
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cc = [x[0] for x in result]
    except IndexError:
        cc = []
    conn.close()
    return cc


def athletes(tournament) -> list:  # beolvassa a tárolt versenysorozatokat
    try:
        conn = connect("ttmanager.db")
        sql = """SELECT surname || ' ' || firstname || ' ' || pick, position FROM ranklist
                WHERE tournament=? ORDER BY position;"""
        cur = conn.cursor()
        cur.execute(sql, (tournament,))
        result = cur.fetchall()
        cc = result
    except IndexError:
        cc = []
    conn.close()
    return cc


def insert_new_tournament(name):
    conn = connect("ttmanager.db")
    cur = conn.cursor()
    sql = "INSERT INTO tournaments VALUES (?);"
    cur.execute(sql, (name,))
    conn.commit()
    conn.close()


def isexists_comp(name):
    conn = connect("ttmanager.db")
    cur = conn.cursor()
    sql = """SELECT compname FROM competitions WHERE (compname=?)"""
    savedcomps = cur.execute(sql, (name,)).fetchone()
    return savedcomps != None


def insert_newcomp(competition):
    conn = connect("ttmanager.db")
    sql = """INSERT INTO competitions 
            (id, compname, tournament, compdate, compstatus, groups, places)
             VALUES (?,?,?,?,?,?,?)"""
    try:
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM competitions;")
        num = cur.fetchall()
        competition.id = num[0][0] + 1
        cur.execute(
            sql,
            (
                competition.id,
                competition.name,
                competition.tournament,
                competition.date,
                competition.status,
                competition.firstround,
                competition.secondround,
            ),
        )
        conn.commit()
    except Error:
        print("nem tudtam létrehozni a versenyt")
    conn.close()


def add_to_ranklist(firstname, surname, pick, position, tournament):
    conn = connect("ttmanager.db")
    sql = """INSERT INTO ranklist 
            (firstname, surname, pick, position, tournament)
             VALUES (?,?,?,?,?)"""
    try:
        cur = conn.cursor()
        cur.execute(
            sql, (firstname, surname, pick, position, tournament),
        )
        conn.commit()
        success = True
    except Error:
        success = False
    conn.close()
    return success


def delete_old_datas(comp_id):
    conn = connect("ttmanager.db")
    sql = "DELETE FROM players WHERE competition_id=?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (comp_id,))
        conn.commit()
        success = True
    except Error:
        success = False
    conn.close()
    return success


def store_players(comp_id, player_id, group, id):
    conn = connect("ttmanager.db")
    sql = """INSERT INTO players 
            (rank_id, competition_id, group_name, id)
             VALUES (?,?,?,?)"""
    try:
        cur = conn.cursor()
        cur.execute(
            sql, (player_id, comp_id, group, id),
        )
        conn.commit()
        success = True
    except Error:
        success = False
    conn.close()
    return success


def read_players(comp_id):
    groups = []
    conn = connect("ttmanager.db")
    try:
        cur = conn.cursor()
        sql = "SELECT DISTINCT group_name FROM players WHERE competition_id=?"
        cur.execute(sql, (comp_id,))
        result = cur.fetchall()
        for item in result:
            groups.append(item[0])
        ath = {i: [] for i in groups}
        sql = """SELECT players.group_name, 
                surname || ' ' || firstname || ' ' || pick, ranklist.position FROM ranklist 
                INNER JOIN players ON players.rank_id = ranklist.position
                WHERE players.competition_id=?
                ORDER BY players.group_name, players.id"""
        cur.execute(sql, (comp_id,))
        result = cur.fetchall()
        for item in result:
            ath[item[0]].append(item[1:])
    except Error:
        ath = {}
    conn.close()
    return ath

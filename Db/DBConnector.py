import _sqlite3

class DBConnector():
    conn = _sqlite3.connect('biblioteca.db')
    c = conn.cursor()

    c.execute(
        'CREATE TABLE IF NOT EXISTS usuario (\
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
            nome TEXT NOT NULL)')

    c.execute(
        'CREATE TABLE IF NOT EXISTS livro (\
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
            titulo TEXT NOT NULL, \
            autor TEXT NOT NULL, \
            ano INTEGER NOT NULL, \
            status INTEGER NOT NULL, \
            locatario_id INTEGER, \
            FOREIGN KEY (locatario_id) REFERENCES usuario(id))')

    conn.commit()

    def query(self, query, params=()):
        self.c.execute(query, params)
        return self.c.fetchall()

    def exec(self, query, params=()):
        self.c.execute(query, params)
        self.conn.commit()
        return self.c.lastrowid

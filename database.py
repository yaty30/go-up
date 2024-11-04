import sqlite3

class Database:
    database = "data.db"
    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    def get(self, sql):
        self.cursor.execute(sql)

        rows = self.cursor.fetchall()
        
        self.conn.close()
        
        return rows
    
    def insert(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()
        
        
    def create_table(self, table_name, params):
        sql = f"CREATE TABLE {table_name} "
        sql += "(\n" + ", \n".join([col["name"] + " " + col["datatype"] for col in params]) + "\n)"
        
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()
        

if __name__ == "__main__":
    # create wallet table
    sql = """CREATE TABLE WALLET (
                ID VARCHAR(255),
                ACTIVE NUMERIC, 
                CREATE_DATE DATE
            )"""
    Database().create_table("WALLET", 
            [
                { "name": "ID", "datatype": "VARCHAR(255)"},
                { "name": "ACTIVE", "datatype": "NUMERIC"},
                { "name": "CREATE_DATE", "datatype": "DATE"},
            ]                
            )
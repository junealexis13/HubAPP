import os
import sqlite3


class Auth:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        #initialize DB
        userDB = os.path.join(os.getcwd(),"database","user.db")
        self.conn_user = sqlite3.connect(userDB)
        self.cur = self.conn_user.cursor()
        
    def run_cmd(self, cmd: str):
        out = self.cur.execute(cmd)
        return out
    
    def new_DB(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS auth(userID INTEGER PRIMARY KEY, employee_ID VARCHAR(255), username VARCHAR(255), password VARCHAR(255), user_alias VARCHAR(255), first_name text, surname text);''')
        self.conn_user.commit()
        self.cur.close()
        
    def add_user(self, info: list):
        self.cur.execute(f"INSERT INTO Users (userID, employee_ID, employee_ID, username, password address, email, phone_number) VALUES (?,?,?,?,?,?)",info)
        self.conn_user.commit()
        self.cur.close()
        
    def show_db(self):
        self.cur.execute("SELECT * FROM sqlite_master WHERE type='table';")
        tables = self.cur.fetchall()
        return tables
    
    def close_instance(self):
        self.conn_user.close()
    
if __name__ == "__main__":
    auth = Auth("junealexis13","Junealexis_13")
    for x in auth.run_cmd("SELECT * FROM auth"):
        print(x)
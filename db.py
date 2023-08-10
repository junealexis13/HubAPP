import os, glob
import pandas as pd
import sqlite3

class User():
    def __init__(self):
        userDB = os.path.join(os.getcwd(),"database","user.db")
        self.conn_user = sqlite3.connect(userDB)
        self.cur = self.conn_user.cursor()

    def new_DB(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Users (userID INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR(255), surname VARCHAR(255), employee_ID VARCHAR(255), address VARCHAR(255), email VARCHAR(255), phone_number VARCHAR(255));''')
        self.conn_user.commit()
        self.cur.close()
            
    def add_user(self, info: list):
        self.cur.execute(f"INSERT INTO Users (first_name, surname, employee_ID, address, email, phone_number) VALUES (?,?,?,?,?,?)",info)
        self.conn_user.commit()
        self.cur.close()
        
    def update_user(self, userID, update_info: dict = None):
        info_type = list(update_info.keys())
        cmd = "UPDATE Users SET " 
        val = list()
        for i,(X,Y) in enumerate(update_info.items()):
            if len(update_info) != i+1:
                cmd += f"{X} = ?, "
                val.append(Y)
            elif len(update_info) == i+1:
                cmd += f"{X} = ? "
                val.append(Y)

        val.append(userID)
        cmd += f"WHERE userID = ?"
        self.cur.execute(cmd, val)
        self.conn_user.commit()
    
    def run_cmd(self, cmd: str):
        out = self.cur.execute(cmd)
        return out
        
    def show_db(self):
        self.cur.execute("SELECT * FROM sqlite_master WHERE type='table';")
        tables = self.cur.fetchall()
        return tables
    
    def close_instance(self):
        self.conn_user.close()
    
class DTR:
    def __init__(self, emp_ID: int):
        self.employee_ID = int(emp_ID)
        self.df = pd.read_excel(glob.glob(os.path.join(os.getcwd(),"data_files","*"))[0])
    
    def fetch_employee(self):
        emp = self.df.loc[self.df['Emp ID'] == self.employee_ID]
        name = emp["Display Name"].unique()
        return f"| EMP_ID: {self.employee_ID} \n| Name: {name[0]}"
        
    def fetch_data(self):
        return self.df.loc[self.df['Emp ID'] == self.employee_ID]


if __name__ == "__main__":
    #init db
    active = True
    while active:
        ID = int(input("Enter ID: "))
        try:
            dtr = DTR(ID)
            print(dtr.fetch_employee())
        except IndexError:
            print('Employee not found')
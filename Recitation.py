import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\ASUS\Downloads\Database2.accdb;')
    print("Connected to a Database")

    Fullname = "Sangco, Jerrold Cornelius"
    Assignment = 95
    Laboratory = 90
    Quiz = 100
    Exam = 88
    user_id = 10

    record = connect.cursor()
    record.execute('UPDATE Table1 SET Fullname = ?, Assignment = ?, Laboratory = ?,Quiz = ?, Exam =?, WHERE id=?',(Fullname, Assignment, Laboratory,Quiz, Exam, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")
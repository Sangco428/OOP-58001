import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Waywaya\Downloads\Database1.accdb;')
    print("Connected to a Database")

    user_id = 11
    Inventors = "Group 5"
    Invention="Laboratory Activity 9"
    Date_of_Invention=2022
    Description="The activity was conducted to insert a data into the database using pycharm"

    record = connect.cursor()
    record.execute('INSERT INTO tblInventor VALUES(?,?,?,?,?)', (user_id, Inventors, Invention, Date_of_Invention, Description))
    record.commit()
    print("Data is Inserted")

except pyodbc.Error as e:
    print("Error in Connection")
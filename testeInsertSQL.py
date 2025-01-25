import sqlite3

try:
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO scanface_facelogin ( `verified`, `distance`, `threshold`, `model`, `detector_backend`, `similarity_metric`, `facial_areas`, `time` ) VALUES ( "True", "0.552401273947962", "0.68", "VGG-Face", "opencv", "cosine", "{'img1': {'x': 354, 'y': 197, 'w': 224, 'h': 224, 'left_eye': [526, 285], 'right_eye': [429, 280]}, 'img2': {'x': 164, 'y': 361, 'w': 840, 'h': 840, 'left_eye': [714, 676], 'right_eye': [419, 678]}}", "3.28" )"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
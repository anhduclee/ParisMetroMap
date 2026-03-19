import database

if __name__ == "__main__":
    database.init_db()
    database.insert_data()
    database.select_table("edges")
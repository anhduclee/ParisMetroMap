import database
from algorithm import haversine

if __name__ == "__main__":
    database.init_db()
    database.insert_nodes()
    database.insert_edges()
    database.select_table("edges")
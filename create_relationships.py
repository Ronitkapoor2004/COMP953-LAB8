"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from random import randint, choice 
from faker import Faker

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Add the Relationships Table"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS relationships ( id INTEGER PRIMARY KEY, 
    person1_id INTEGER NOT NULL, 
    person2_id INTEGER NOT NULL, 
    type TEXT NOT NULL, 
    start_date DATE NOT NULL, 
    FOREIGN KEY (person1_id) REFERENCES people (id), 
    FOREIGN KEY (person2_id) REFERENCES people (id) ); 
    """
    cursor.execute(create_table_sql)
    conn.commit() 
    conn.close()

    return

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Populate the Relationships Table"
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    insert_relationship_sql = """
    INSERT INTO relationships ( person1_id, person2_id, type, start_date )
    VALUES (?, ?, ?, ?);
    """

    faker = Faker()
    
    for i in range(0,100):

        individual1_id = randint(1, 200)
        individual2_id = randint(1, 200)

        while individual2_id == individual1_id:
            individual2_id = randint(1, 200)

        relationship_type = choice(('friend', 'spouse', 'partner', 'relative'))
        relationship_start_date = faker.date_between(start_date='-50y', end_date='today')

        new_connection = (individual1_id, individual2_id, relationship_type, relationship_start_date)

        cursor.execute(insert_relationship_sql, new_connection)

    conn.commit()
    conn.close()
    return 

if __name__ == '__main__':
   main()

import mysql.connector
from mysql.connector import errorcode
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost", 
            user="root",
            password="Password",
            database="movies"
        )
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)
        return None  


def show_films(cursor, title):
    conn=get_db_connection()
    if not conn:
        print("Failed to connect to the database.")
        return
    else:
   
    #Disply selected fields from the film table 
         print(f"\n---{title}---")

    try:
        #SQL query spanning multiple lines for readability
        query = ("SELECT f.film_name as Name, f.film_director as Director, g.genre_name as"
        " Genre FROM film f INNER JOIN genre g ON f.genre_id = g.genre_id",
        "INNER JOIN studio s ON f.studio_id = s.studio_id")

        cursor.execute(query)
        #fetch all results from the executed query
        films=cursor.fetchall()
        if films:
        #print header
            print(f"{'Name':<30} {'Director':<20} {'Genre':<15} {'Studio':<20 }")
            print("-" * 85)
        #iterate and print each film's details
            for film in films:
                print(f"{film[0]:<30} {film[1]:<20} {film[2]:<15} {film[3]:<20}")
        else:
            print("No films found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def connect_to_db():
            # Connect to the MySQL database and return the connection and cursor 
    try:
        Connection = mysql.connector.connect(

                    host="localhost",
                    user= "root",
                    password="password",
                    database="movies"
        )
        return Connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Invalid username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                        print("Database does not exist.")
        else:
                        print(err)
        return None

def main():
    conn=connect_to_db()
    if not conn:
                 print("Failed to connect to the database.")
    return
    cursor=conn.cursor()
                          
                          
     #2. Insert a new film record
    print("\n Inserting a new film record...")

    #Assumeing'Sci-Fi' genre_id is 4 and 'Universal Studios' studio_id is 2
    insert_query = ("INSERT INTO film (film_name, film_director, genre_id, studio_id) VALUES (%s, %s, %s, %s)")
    new_film_data = ("Inception", "Christopher Nolan", 4, 2)
    cursor.execute(insert_query, new_film_data)
    conn.commit()
    print("New film record inserted successfully.")

    
     #3. Update'Alien' to 'Horror' 
    print("\n Updating 'Alien' genre to 'Horror'...")
    #Assuming 'Horror' genre_id =3 (adjust IDs as necessary)

    update_query = ("UPDATE film SET genre_id = %s WHERE film_name = %s")
    cursor.execute(update_query, (3, "Alien"))
    conn.commit()
    print("Film genre updated successfully.")
    show_films(cursor, "Updated Film List")

    #4. Delete 'The Gladiator' record
    print("\n Deleting 'The Gladiator' record...")
    delete_query = ("DELETE FROM film WHERE film_name = %s")
    delete_data = ("Gladiator",)
    cursor.execute(delete_query, delete_data)
    conn.commit()
    print("Film record deleted successfully.")
    show_films(cursor, "Display After Deletion")

   
if __name__ == "__main__":
          main()


                        
               
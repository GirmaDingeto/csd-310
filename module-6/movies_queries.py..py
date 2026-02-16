import mysql.connector
try:
   db=mysql.connector.connect(
      host="localhost",
      user="ROOT",
      password="PASSWORD",
      database="movies",
      raise_on_warnings=True
   )
   cursor=db.cursor()
   #---Query 1: All fields from the studio table---
   print("---DISPLAYING ALL STUDIO RECORDS---")
   cursor.execute("SELECT * FROM Studio")
   studios = cursor.fetchall()
   for studio in studios:
       print("studio_id: {}, studio_name: {}, studio_description: {}".format(studio[0], studio[1], studio[2]))

    #---Query 2: All fields from the genre table---
       print("---DISPLAYING ALL GENRE RECORDS---") 
   cursor.execute("SELECT * FROM Genre")
   genres = cursor.fetchall()
   for genre in genres:
       print("genre_id: {}, genre_name: {}".format(genre[0], genre[1], genre[2]))

    #---Query 3: Film names with runtime <120 minutes---
       print("---DISPLAYING FILMS WITH RUNTIME LESS THAN 120 MINUTES---")
       
   cursor.execute("SELECT film_name,film_runtime FROM Film WHERE film_runtime < 120")
   movies = cursor.fetchall()
   for movie in movies:
       print("film_name: {}, film_runtime: {}".format(movie[0], movie[1]))

  #---Query 4: Films names and Directors grouped by Director---
       print("---DISPLAYING FILMS AND DIRECTORS GROUPED BY DIRECTOR---")
       #Note:Using ORDER BY to ensure logical grouping in the output

   cursor.execute("SELECT film_name, film_director FROM film GROUP BY film_director, film_name")
   director_list = cursor.fetchall()
   for row in director_list:
         print("film_director: {}, film_name: {}".format(row[0], row[1], row[2]))

except mysql.connector.Error as err:
   print("Error: {}".format(err))
finally:
 if'db' in locals() and db.is_connected():
       cursor.close()
       db.close()
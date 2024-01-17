# 0x0E. SQL - More queries

In SQL, a primary key is a field in a table which uniquely identifies each row/record in that table. It must contain unique values and it cannot contain null values. These keys are fundamental to maintaining the integrity of your data. The primary key constraint ensures that no duplicate or null values are entered in the primary key field(s). The foreign key constraint ensures that the values in a column (or a group of columns) match the values in a column of another table.
JOIN and UNION are used to combine rows from two or more tables.
JOIN is used to combine rows from two or more tables based on a related column between them. There are several types of JOINs: INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.
UNION is used to combine the result-set of two or more SELECT statements. Each SELECT statement within UNION must have the same number of columns, the columns must also have similar data types, and they must also be in the same order.
As for granting privileges, SQL provides commands like GRANT and REVOKE to provide or remove permissions to/from users. You can grant different types of permissions, like SELECT, INSERT, UPDATE, DELETE, etc., on a particular table or all tables to a user or a group of users.
Remember, it's important to manage these privileges carefully to maintain the security of your database.


## Files/Tasks


|      Tasks          |Files               |
|----------------|-------------------------------|
|0. My privileges!|`0-privileges.sql`|
|1. Root user|`1-create_user.sql`|            
|2. Read user|`2-create_read_user.sql`|
|3. Always a name|`3-force_name.sql`            
|4. ID can't be null|`4-never_empty.sql`|
|5. Unique ID|`5-unique_id.sql`            
|6. States table|`6-states.sql`|
|7. Cities table|`7-cities.sql`            
|8. Cities of California|`8-cities_of_california_subquery.sql`|
|9. Cities by States|`9-cities_by_state_join.sql`            
|10. Genre ID by show|`10-genre_id_by_show.sql`|
|11. Genre ID for all shows|`11-genre_id_all_shows.sql`            
|12. No genre|`12-no_genre.sql`|
|13. Number of shows by genre|`13-count_shows_by_genre.sql`            
|14. My genres|`14-my_genres.sql`|
|15. Only Comedy|`15-comedy_only.sql`            
|16. List shows and genres|`16-shows_by_genre.sql`|


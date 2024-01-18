-- This sctipt t uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT title
FROM tv_shows
RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;

-- Lists all genres of the show "Dexter" Using the database "hbtn_0d_tvshows"
SELECT tv_genres.name FROM tv_show_genres JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name;

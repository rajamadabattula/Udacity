# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY NOT NULL,
    start_time TIMESTAMP NOT NULL,
    user_id INTEGER NOT NULL,
    level VARCHAR(10) NOT NULL,
    song_id VARCHAR(20) ,
    artist_id VARCHAR(20)  ,
    session_id INTEGER NOT NULL,
    location VARCHAR(50) NOT NULL,
    user_agent VARCHAR(150) NOT NULL
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender CHAR(1) NOT NULL,
    level VARCHAR(10) NOT NULL
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR(20) PRIMARY KEY NOT NULL,
    title VARCHAR(100) NOT NULL,
    artist_id VARCHAR(20) NOT NULL ,
    year INTEGER NOT NULL,
    duration FLOAT NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR(20) PRIMARY KEY NOT NULL ,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    lattitude FLOAT,
    longitude FLOAT
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY NOT NULL,
    hour INTEGER NOT NULL,
    day INTEGER NOT NULL,
    week INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    weekday INTEGER NOT NULL
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(songplay_id) DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, lattitude, longitude)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT ss.song_id, ss.artist_id FROM songs ss 
JOIN artists ars on ss.artist_id = ars.artist_id
WHERE ss.title = %s
AND ars.name = %s
AND ss.duration = %s
;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
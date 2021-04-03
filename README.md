# Project: Data Modeling with Postgres

A startup named Sparkify wants to analyze user activities using their song and
user data. The current data is spread among several JSON files, making it hard
to query and analyze.

This project aims to create an ETL pipeline to load song and user data to a
Postgres database, making it easier to query and analyze data.

## Datasets

Data is currently collected for song and user activities, in two directories:
`data/log_data` and `data/song_data`, using JSON files.

### Song dataset format

```json
{
  "num_songs": 1,
  "artist_id": "ARGSJW91187B9B1D6B",
  "artist_latitude": 35.21962,
  "artist_longitude": -80.01955,
  "artist_location": "North Carolina",
  "artist_name": "JennyAnyKind",
  "song_id": "SOQHXMF12AB0182363",
  "title": "Young Boy Blues",
  "duration": 218.77506,
  "year": 0
}
```

### Log dataset format

```json
{
  "artist": "Survivor",
  "auth": "Logged In",
  "firstName": "Jayden",
  "gender": "M",
  "itemInSession": 0,
  "lastName": "Fox",
  "length": 245.36771,
  "level": "free",
  "location": "New Orleans-Metairie, LA",
  "method": "PUT",
  "page": "NextSong",
  "registration": 1541033612796,
  "sessionId": 100,
  "song": "Eye Of The Tiger",
  "status": 200,
  "ts": 1541110994796,
  "userAgent": "\"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36\"",
  "userId": "101"
}
```

## Schema

### Fact tables

#### Songplays

Records in log data associated with song plays i.e. records with `page` set to
`NextSong`.

|   Column    |            Type             | Nullable |
| ----------- | --------------------------- | -------- |
| songplay_id | integer                     | not null |
| start_time  | timestamp without time zone | not null |
| user_id     | integer                     | not null |
| level       | character varying           | not null |
| song_id     | character varying(18)       |          |
| artist_id   | character varying(18)       |          |
| session_id  | integer                     | not null |
| location    | character varying           | not null |
| user_agent  | character varying           | not null |

Primary key: songplay_id

### Dimension tables

#### Users

Users in the app.

|   Column   |       Type        | Nullable |
| ---------- | ----------------- | -------- |
| user_id    | integer           | not null |
| first_name | character varying | not null |
| last_name  | character varying | not null |
| gender     | character(1)      | not null |
| level      | character varying | not null |

Primary key: user_id

#### Songs

Songs in music database.

|  Column   |         Type          | Nullable |
| --------- | --------------------- | -------- |
| song_id   | character varying(18) | not null |
| title     | character varying     | not null |
| artist_id | character varying(18) | not null |
| year      | integer               | not null |
| duration  | double precision      | not null |

Primary key: song_id

#### Artists

Artists in music database.

|  Column   |         Type          | Nullable |
| --------- | --------------------- | -------- |
| artist_id | character varying(18) | not null |
| name      | character varying     | not null |
| location  | character varying     | not null |
| latitude  | double precision      |          |
| longitude | double precision      |          |

Primary key: artist_id

#### Time

Timestamps of records in songplays broken down into specific units.

|   Column   |            Type             | Nullable |
| ---------- | --------------------------- | -------- |
| start_time | timestamp without time zone | not null |
| hour       | integer                     | not null |
| day        | integer                     | not null |
| week       | integer                     | not null |
| month      | integer                     | not null |
| year       | integer                     | not null |
| weekday    | integer                     | not null |
Project Design

Database Design is very optimized because with a ew number of tables and doing specific join, we can get the most information and do analysis

ETL Design is also simplified have to read json files and parse accordingly to store the tables into specific columns and proper formatting

Database Script

Writing "python create_tables.py" command in terminal, it is easier to create and recreate tables

Jupyter Notebook

etl.ipynb, a Jupyter notebook is given for verifying each command and data as well and then using those statements and copying into etl.py and running it into terminal using "python etl.py" and then running test.ipynb to see whether data has been loaded in all the tables

Relevant Files Provided

test.ipnb displays the first few rows of each table to let you check your database

create_tables.py drops and created your table

etl.ipynb read and processes a single file from song_data and log_data and loads into your tables in Jupyter notebook

etl.py read and processes a single file from song_data and log_data and loads into your tables in ET

sql_queries.py containg all your sql queries and in imported into the last three files above
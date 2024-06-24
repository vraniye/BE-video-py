CREATE_VIDEO_TABLE = (
    'CREATE TABLE IF NOT EXISTS video_data (id SERIAL PRIMARY KEY, file_name VARCHAR(255), uuid VARCHAR(255), image_path TEXT, mpd_path TEXT);'
)

INSERT_VIDEO = (
    'INSERT INTO video_data (file_name, uuid, image_path, mpd_path) VALUES (%s, %s, %s, %s);'
)

GET_ALL_VIDEO_UUID = (
    'SELECT uuid FROM video_data ORDER BY uuid DESC;'
)

GET_PATHS_BY_UUID = (
    'SELECT mpd_path, image_path FROM video_data WHERE uuid = %s;'
)
CREATE_VIDEO_TABLE = (
    'CREATE TABLE IF NOT EXISTS video_data (id SERIAL PRIMARY KEY, file_name VARCHAR(255), uuid VARCHAR(255), image_path TEXT, mpd_path TEXT);'
)

INSERT_VIDEO = (
    'INSERT INTO video_data (file_name, uuid, image_path, mpd_path) VALUES (%s, %s, %s, %s);'
)
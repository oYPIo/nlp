CREATE TABLE IF NOT EXISTS input_data (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS output_data (
    id INTEGER PRIMARY KEY,
    text TEXT NOT NULL,
    prediction TEXT
);
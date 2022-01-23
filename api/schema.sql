-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS places;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    name TEXT,
    lastname TEXT,
    email TEXT UNIQUE,
    phone TEXT UNIQUE,
    adress TEXT,
    adress_number INTEGER,
    complement TEXT,
    city TEXT,
    state TEXT,
    country TEXT
);

CREATE TABLE places (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    adress TEXT NOT NULL,
    adress_number INTEGER NOT NULL,
    complement TEXT,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    country TEXT NOT NULL,
    onwer_id INTEGER NOT NULL,
    posted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    FOREIGN KEY (onwer_id) REFERENCES user (id)
);
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    title TEXT,
    company TEXT,
    location TEXT,
    url TEXT,
    score REAL,
    status TEXT
);

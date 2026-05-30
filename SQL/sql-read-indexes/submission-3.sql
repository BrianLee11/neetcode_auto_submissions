CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT
);
-- Do not modify above this line. --

SELEcT *
FROM pg_indexes
WHERE tablename = 'pokemon';

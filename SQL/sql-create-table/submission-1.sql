/* Relational databases store data in tables.
A table consists of rows and columns.
*/

CREATE TABLE videos(
    id INTEGER,
    name TEXT,
    created_AT DATE,
    published BOOLEAN
/*  This is the schema of the table.
 It's analogous to a class definition in
 object-oriented programming.
 */
);


-- Do not modify below this line --
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_name = 'videos';

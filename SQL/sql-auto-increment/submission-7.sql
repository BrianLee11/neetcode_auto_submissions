-- DROP TABLE IF EXISTS
DROP TABLE IF EXISTS gov_employee;

-- CREATE SEQUENCE that starts at 1000 and increments by 3
CREATE SEQUENCE gov_id START with 1000 INCREMENT BY 3;

-- CREATE TABLE
CREATE TABLE gov_employee(
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    gov_id INTEGER DEFAULT nextval('gov_id'),
    name TEXT
);

-- Do not modify below this line --
INSERT INTO gov_employee (name) 
  VALUES
      ('John Doe'),
      ('Jane Doe'),
      ('Jim Beam');

SELECT * FROM gov_employee;

-- Create a table called products
CREATE TABLE products(

    -- name of type TEXT and must not be NULL, with a default value of 'Unknown'
    name TEXT NOT NULL DEFAULT 'Unknown',

    -- price of type INTEGER and must not be NULL
    price INTEGER NOT NULL,

    -- quantity of type INTEGER which has a default value of 0
    quantity INTEGER DEFAULT 0
);

-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';

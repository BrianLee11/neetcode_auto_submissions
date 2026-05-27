-- Create a table called products
CREATE TABLE products(

    -- name of type TEXT and must not be NULL, with a default value of 'Unknown'
    name TEXT NOT NULL DEFAULT 'Unknown',
    price INTEGER NOT NULL,
    quantity INTEGER DEFAULT 0
);

-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';

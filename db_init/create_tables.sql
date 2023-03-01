CREATE TABLE IF NOT EXISTS "user"(
    user_id serial PRIMARY KEY,
    "name"  VARCHAR (50) UNIQUE NOT NULL,
    age SMALLINT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT true
);
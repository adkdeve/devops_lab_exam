CREATE TABLE IF NOT EXISTS guestbook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    message VARCHAR(255)
);

INSERT INTO guestbook (name, message) VALUES ('Admin', 'Welcome to the DevOps Guestbook!');
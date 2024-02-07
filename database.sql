create database checktor ;
use checktor;
-- Create users table
CREATE TABLE users (
    id INT PRIMARY KEY auto_increment,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    full_name VARCHAR(100),
    password VARCHAR(100)
);

-- Insert example data
INSERT INTO users (username, email, full_name, password) VALUES
('john_doe', 'john@example.com', 'John Doe', 'password123'),
('jane_smith', 'jane@example.com', 'Jane Smith', 'abc123');

select * from users;
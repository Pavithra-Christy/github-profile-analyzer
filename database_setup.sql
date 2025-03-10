CREATE DATABASE github_analysis;
USE github_analysis;

CREATE TABLE users (
    username VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    bio TEXT,
    public_repos INT,
    followers INT,
    following INT,
    github_url VARCHAR(255)
);

CREATE TABLE repositories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    repo_name VARCHAR(100),
    language VARCHAR(50),
    repo_url VARCHAR(255),
    FOREIGN KEY (username) REFERENCES users(username)
);
 

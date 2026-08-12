CREATE DATABASE IMDB;
USE IMDB;
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);
CREATE TABLE Movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    release_year INT,
    plot TEXT
);
CREATE TABLE Media (
    media_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    media_type ENUM('Video', 'Image'),
    url VARCHAR(255),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) ON DELETE CASCADE
);
CREATE TABLE Genres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(50) UNIQUE
);
CREATE TABLE Movie_Genres (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
);
CREATE TABLE Reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    user_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 10),
    comment TEXT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
CREATE TABLE Artists (
    artist_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);
CREATE TABLE Artist_Skills (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    artist_id INT,
    skill_name VARCHAR(50),
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);
CREATE TABLE Movie_Cast_Roles (
    cast_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    artist_id INT,
    role_name VARCHAR(50), -- e.g., 'Actor', 'Director', 'Producer'
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);
INSERT INTO Movies (title, release_year, plot) VALUES ('Inception', 2010, 'A thief who steals corporate secrets...');

INSERT INTO Media (movie_id, media_type, url) VALUES 
(1, 'Image', 'poster.jpg'),
(1, 'Video', 'trailer.mp4');

INSERT INTO Genres (genre_name) VALUES ('Sci-Fi'), ('Action'), ('Thriller');
INSERT INTO Movie_Genres (movie_id, genre_id) VALUES (1, 1), (1, 2);

INSERT INTO Users (username, email) VALUES ('Cinephile99', 'bob@example.com');
INSERT INTO Reviews (movie_id, user_id, rating, comment) VALUES (1, 1, 10, 'Mind-bending masterpiece!');

INSERT INTO Artists (name) VALUES ('Leonardo DiCaprio');
INSERT INTO Artist_Skills (artist_id, skill_name) VALUES (1, 'Acting'), (1, 'Producing');

INSERT INTO Movie_Cast_Roles (movie_id, artist_id, role_name) VALUES 
(1, 1, 'Actor'),
(1, 1, 'Executive Producer');

SELECT 
    m.title AS Movie_Title,
    a.name AS Artist_Name,
    GROUP_CONCAT(mcr.role_name SEPARATOR ', ') AS Roles
FROM 
    Movies m
JOIN 
    Movie_Cast_Roles mcr ON m.movie_id = mcr.movie_id
JOIN 
    Artists a ON mcr.artist_id = a.artist_id
WHERE 
    m.title = 'Inception'
GROUP BY 
    m.movie_id, a.artist_id;
SELECT * FROM Movies;
SELECT * FROM Genres;
SELECT * FROM Movie_Genres;
SELECT * FROM Media;
SELECT * FROM Artists;
SELECT * FROM Artist_Skills;
SELECT * FROM Movie_Cast_Roles;
SELECT * FROM Users;
SELECT * FROM Reviews;
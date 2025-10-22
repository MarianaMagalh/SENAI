drop database filmes;
CREATE DATABASE filmes;
USE filmes;

CREATE TABLE Linguagem(
	linguagemID INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(255)
);
INSERT INTO Linguagem (tipo) 
VALUES 
	('Inglês'),
	('Português'),
	('Espanhol'),
	('Francês'),
	('Mandarim');
    
SELECT * FROM Linguagem;


CREATE TABLE Pais(
	paisID INT PRIMARY KEY AUTO_INCREMENT,
    numIdentificar INT
);
INSERT INTO Pais (numIdentificar) 
VALUES 
	(1),  -- EUA
	(55), -- Brasil
	(34), -- Espanha
	(33), -- França
	(86); -- China
    
SELECT * FROM Pais;


CREATE TABLE GeneroFIlme(
	generoID INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(255)
);
INSERT INTO GeneroFilme (tipo) 
VALUES 
	('Ação'),
	('Drama'),
	('Comédia'),
	('Terror'),
	('Romance'),
	('Ficção Científica'),
	('Aventura'),
	('Animação'),
	('Suspense'),
	('Documentário');
    
SELECT * FROM GeneroFilme;


CREATE TABLE Produtora(
	produtoraID INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    ceo VARCHAR(255),
    origem VARCHAR(255)
);
INSERT INTO Produtora (nome, ceo, origem) 
VALUES 
    ('Warner Bros.', 'Kevin Tsujihara', 'EUA'), 
    ('Disney', 'Bob Iger', 'EUA'),        
    ('Paramount', 'Shari Redstone', 'EUA'),  
    ('Legendary', 'Thomas Tull', 'EUA'),     
    ('Universal', 'Donna Langley', 'EUA'),  
    ('Summit Entertainment', 'Rob Friedman', 'EUA');
    
SELECT * FROM Produtora;


CREATE TABLE Ator(
	atorID INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    sobrenome VARCHAR(255),
    genero VARCHAR(255),
    nacionalidade VARCHAR(255)
);
INSERT INTO Ator (nome, sobrenome, genero, nacionalidade) 
VALUES 
	('Leonardo', 'DiCaprio', 'Masculino', 'Americano'),
	('Kate', 'Winslet', 'Feminino', 'Britânica'),
	('Heath', 'Ledger', 'Masculino', 'Australiano'),
	('Christian', 'Bale', 'Masculino', 'Britânico'),
	('Uma', 'Thurman', 'Feminino', 'Americana'),
	('John', 'Travolta', 'Masculino', 'Americano'),
	('Robert', 'De Niro', 'Masculino', 'Americano'),
	('Joe', 'Pesci', 'Masculino', 'Americano'),
	('Harrison', 'Ford', 'Masculino', 'Americano'),
	('Karen', 'Allen', 'Feminino', 'Americana'),
	('Idris', 'Elba', 'Masculino', 'Britânico'),
	('Margot', 'Robbie', 'Feminino', 'Australiana'),
	('Saoirse', 'Ronan', 'Feminino', 'Irlandesa'),
	('Timothée', 'Chalamet', 'Masculino', 'Americano'),
	('Daniel', 'Day-Lewis', 'Masculino', 'Britânico'),
	('Wagner', 'Moura', 'Masculino', 'Brasileiro'),
	('Alice', 'Braga', 'Feminino', 'Brasileira'),
	('Penélope', 'Cruz', 'Feminino', 'Espanhola'),
	('Javier', 'Bardem', 'Masculino', 'Espanhol'),
	('Tony', 'Leung', 'Masculino', 'Chinês'),
    ('Kristen', 'Stewart', 'Feminino', 'Americana');
    
SELECT * FROM Ator;


CREATE TABLE Diretor(
	diretorID INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    sobrenome VARCHAR(255),
    genero VARCHAR(150),
    nacionalidade VARCHAR(150)
);
INSERT INTO Diretor (nome, sobrenome, genero, nacionalidade) 
VALUES 
	('James', 'Cameron', 'Masculino', 'Canadense'),
	('Kathryn', 'Bigelow', 'Feminino', 'Americana'),
	('Christopher', 'Nolan', 'Masculino', 'Britânico'),
	('Greta', 'Gerwig', 'Feminino', 'Americana'),
	('Quentin', 'Tarantino', 'Masculino', 'Americano'),
	('Patty', 'Jenkins', 'Feminino', 'Americana'),
	('Martin', 'Scorsese', 'Masculino', 'Americano'),
	('Sofia', 'Coppola', 'Feminino', 'Americana'),
	('Steven', 'Spielberg', 'Masculino', 'Americano'),
	('Ava', 'DuVernay', 'Feminino', 'Americana'),
	('Guillermo', 'del Toro', 'Masculino', 'Mexicano'),
	('Chloé', 'Zhao', 'Feminino', 'Americana'),
	('Alejandro', 'González Iñárritu', 'Masculino', 'Mexicano'),
	('Jane', 'Campion', 'Feminino', 'Nova Zelândia'),
	('Fernando', 'Meirelles', 'Masculino', 'Brasileiro'),
	('Agnès', 'Varda', 'Feminino', 'Francesa'),
	('Pedro', 'Almodóvar', 'Masculino', 'Espanhol'),
	('Céline', 'Sciamma', 'Feminino', 'Francesa'),
	('Wong', 'Kar-wai', 'Masculino', 'Chinês'),
	('Lynne', 'Ramsay', 'Feminino', 'Britânica'),
    ('Catherine', 'Hardwicke', 'Feminino', 'Americana');

SELECT * FROM Diretor;


CREATE TABLE Filme(
	filmeID INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255),
    orcamento DECIMAL,
    tempoDuracao VARCHAR(255),
    ano DATE,
    poster TEXT,
    diretorID INT,
    FOREIGN KEY (diretorID) REFERENCES Diretor(diretorID),
    atorID INT,
    FOREIGN KEY (atorID) REFERENCES Ator(atorID),
    linguagemID INT,
    FOREIGN KEY (linguagemID) REFERENCES Linguagem(linguagemID),
    paisID INT,
    FOREIGN KEY (paisID) REFERENCES Pais(paisID),
    generoID INT,
    FOREIGN KEY (generoID) REFERENCES GeneroFilme(generoID),
    produtoraID INT,
    FOREIGN KEY (produtoraID) REFERENCES Produtora(produtoraID)
);
INSERT INTO Filme (titulo, orcamento, tempoDuracao, ano, poster, diretorID, atorID, linguagemID, paisID, generoID, produtoraID) 
VALUES 
	('Titanic', 200000000.00, '194 min', '1997-12-19', 'https://upload.wikimedia.org/wikipedia/pt/2/22/Titanic_poster.jpg', 1, 1, 1, 1, 2, 1),
	('The Dark Knight', 185000000.00, '152 min', '2008-07-18', 'https://m.media-amazon.com/images/S/pv-target-images/e9a43e647b2ca70e75a3c0af046c4dfdcd712380889779cbdc2c57d94ab63902.jpg', 3, 3, 1, 1, 1, 2),
	('Pulp Fiction', 8000000.00, '154 min', '1994-10-14', 'https://upload.wikimedia.org/wikipedia/pt/thumb/8/82/Pulp_Fiction_cover.jpg/250px-Pulp_Fiction_cover.jpg', 5, 5, 1, 1, 3, 3),
	('Goodfellas', 25000000.00, '145 min', '1990-09-19', 'https://m.media-amazon.com/images/M/MV5BN2E5NzI2ZGMtY2VjNi00YTRjLWI1MDUtZGY5OWU1MWJjZjRjXkEyXkFqcGc@._V1_.jpg', 7, 7, 1, 1, 2, 3),
	('Indiana Jones and the Raiders of the Lost Ark', 18000000.00, '115 min', '1981-06-12', 'https://m.media-amazon.com/images/S/pv-target-images/29513c1a6a165ad70745e3a7769a3785042bbe35fbc1ecd6bbd1480df137ef1e.png', 9, 9, 1, 1, 7, 2),
	('Pan''s Labyrinth', 18000000.00, '118 min', '2006-10-20', 'https://m.media-amazon.com/images/M/MV5BOTc1NTAxMWItMWFlNy00MmU2LTkwMTMtNzMwOTg5OTQ5YTFiXkEyXkFqcGc@._V1_.jpg', 11, 1, 1, 1, 6, 4),
	('Birdman', 18000000.00, '119 min', '2014-10-17', 'https://m.media-amazon.com/images/M/MV5BODAzNDMxMzAxOV5BMl5BanBnXkFtZTgwMDMxMjA4MjE@._V1_FMjpg_UX1000_.jpg', 13, 11, 1, 1, 2, 5),
	('Cidade de Deus', 3350000.00, '130 min', '2002-08-30', 'https://play-lh.googleusercontent.com/hzB49wRFYtA-T5EvxgtrOLMp5SILwl49nyiOLEpNVtH6plGWK4TUGeDrkqs4wpPGPS3dhf0FKKHtAlKKPYwu', 15, 16, 2, 2, 2, 1),
	('Volver', 7500000.00, '121 min', '2006-03-22', 'https://m.media-amazon.com/images/M/MV5BMjA0NTUxMjY1OV5BMl5BanBnXkFtZTcwNjI2OTMzMQ@@._V1_QL75_UY281_CR0,0,190,281_.jpg', 17, 18, 3, 3, 3, 5),
	('In the Mood for Love', 5200000.00, '98 min', '2000-05-21', 'https://s3.amazonaws.com/nightjarprod/content/uploads/sites/344/2025/06/19144836/622343b4935942157a5b2782d60e96db-scaled-1.jpg', 19, 20, 5, 5, 2, 4),
	('Inception', 160000000.00, '148 min', '2010-07-16', 'https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_FMjpg_UX1000_.jpg', 2, 4, 1, 1, 6, 2),
	('The Wolf of Wall Street', 100000000.00, '180 min', '2013-12-25', 'https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_FMjpg_UX1000_.jpg', 4, 1, 1, 1, 3, 1),
	('Saving Private Ryan', 70000000.00, '169 min', '1998-07-24', 'https://m.media-amazon.com/images/M/MV5BZGZhZGQ1ZWUtZTZjYS00MDJhLWFkYjctN2ZlYjE5NWYwZDM2XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg', 6, 1, 1, 1, 1, 2),
	('Little Women', 40000000.00, '135 min', '2019-12-25', 'https://m.media-amazon.com/images/M/MV5BMWI4YWY0ZTktZTVkNC00ODRkLWJjOTYtY2I4NDY3YTRlNDNmXkEyXkFqcGc@._V1_.jpg', 8, 12, 1, 1, 5, 2),
	('Lady Bird', 10000000.00, '94 min', '2017-11-01', 'https://m.media-amazon.com/images/I/812jSz0gqHL._UF1000,1000_QL80_.jpg', 10, 13, 1, 1, 3, 5),
	('There Will Be Blood', 25000000.00, '158 min', '2007-12-26', 'https://m.media-amazon.com/images/I/91PTePb+VNL._UF894,1000_QL80_.jpg', 12, 14, 1, 1, 2, 3),
	('The Motorcycle Diaries', 5500000.00, '126 min', '2004-01-15', 'https://m.media-amazon.com/images/I/61tIEh4duGL._UF1000,1000_QL80_.jpg', 14, 19, 3, 3, 7, 4),
	('Twilight', 37000000.00, '122 min', '2008-11-21', 'https://upload.wikimedia.org/wikipedia/pt/c/c1/Twilight_Poster.jpg', 21, 21, 1, 1, 5, 6),
	('Talk to Her', 4000000.00, '132 min', '2002-03-15', 'https://m.media-amazon.com/images/M/MV5BM2NjMmQyYmQtMjRjMi00OGVjLWFlMDAtNDYzNDE0MmY4YjE1XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg', 18, 18, 3, 3, 5, 5),
	('Chungking Express', 1500000.00, '102 min', '1994-07-14', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsyfkO-pr9ZzGZTo-Hoy-sHBMeFkDJ2QM8pQ&s', 20, 20, 5, 5, 3, 4);
    
SELECT * FROM Filme;




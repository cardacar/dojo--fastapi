CREATE TABLE IF NOT EXISTS users(
	id SERIAL PRIMARY KEY,
	name character varying(255),
	email character varying(255),
	password character varying(255)
);

INSERT INTO users(id, name, email, password) VALUES (1, 'luisa', 'luisa@udea.edu.co', 'pass123');
INSERT INTO users(id, name, email, password) VALUES (2, 'miguel', 'miguel@udea.edu.co', 'pass456');
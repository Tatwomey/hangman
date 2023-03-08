DROP TABLE new_user;
CREATE TABLE IF NOT EXISTS new_user (UserId int PRIMARY KEY AUTOINCREMENT, username varchar(255), password varchar(255));

INSERT INTO new_user (username, password) VALUES ('dummyName', 'password');

INSERT INTO new_user (username, password) VALUES ('Trevor', '1234');

INSERT INTO new_user (username, password) VALUES ('Luana', '1234');

INSERT INTO new_user (username, password) VALUES ('Andrew', '1234');

INSERT INTO new_user (username, password) VALUES ('Ivan', '1234');
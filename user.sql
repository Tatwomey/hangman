DROP TABLE new_user;
CREATE TABLE IF NOT EXISTS new_user (UserId int PRIMARY KEY, username varchar(255), password varchar(255));

INSERT INTO new_user (UserId, username, password) VALUES (1, 'dummyName', 'password');

INSERT INTO new_user (UserId, username, password) VALUES (2, 'Trevor', '1234');

INSERT INTO new_user (UserId, username, password) VALUES (3, 'Luana', '1234');

INSERT INTO new_user (UserId, username, password) VALUES (4, 'Andrew', '1234');

INSERT INTO new_user (UserId, username, password) VALUES (5, 'Ivan', '1234');
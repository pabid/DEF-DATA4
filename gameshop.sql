#Database for  Games shop
CREATE DATABASE GameShop;
USE GameShop;


CREATE TABLE customer (
	ID INT AUTO_INCREMENT,
	FirstName VARCHAR(35) NOT NULL,
	LastName VARCHAR(35) NOT NULL,
	Age INT NOT NULL DEFAULT 3,
	Location VARCHAR(35), 
	ContactNumber VARCHAR(20), 
	PRIMARY KEY (ID)
) ;


CREATE TABLE games (
  ID INT AUTO_INCREMENT,
  Name VARCHAR(35) NOT NULL,
  Genre VARCHAR(35) NOT NULL,
  PEGIratings enum('3','7','12','16','18') NOT NULL DEFAULT '3',  
  Price FLOAT(10,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (ID) 
) ;

CREATE TABLE customer_order (
	ID INT AUTO_INCREMENT,
	CustomerID INT NOT NULL,
	GameID INT NOT NULL ,
	DateOrdered DATETIME NOT NULL,  
	PRIMARY KEY (ID),
	FOREIGN KEY (CustomerID) REFERENCES customer(ID),
	FOREIGN KEY (GameID) REFERENCES games(ID)
) ;




INSERT INTO customer
VALUES (1,'ADAM', 'BEN',15, 'UK', '01208219526'),
(2,'NICK', 'ADAM',25, 'UK', '01204219526'),
(3,'DAN', 'MOSTEL',15, 'UK', '01608219526'),
(4,'BOB', 'BEN',7, 'UK', '01308219522'),
(5,'HELEN', 'BEN',67, 'UK', '01208219523'),
(6,'CUBA', 'BEN',23, 'UK', '01208219524'),
(7,'ADAM', 'DAVIS',45, 'UK', '01208219525'),
(8,'RUDY', 'TRACY',15, 'UK', '01208219527'),
(9,'KARL', 'JACK',18, 'UK', '01208219528'),
(10,'JOE', 'LITTLE',12, 'UK', '01208219529');


INSERT INTO games 
VALUES (1,'BATMAN: ARKHAM ASYLUM', 'HORROR', '18', '39.99'),
(2,'SPIDERMAN', 'FUN', '7', '39.99'),
(3,'SPIDERMAN FOR KIDS', 'FUN', '3', '10.99'),
(4,'INJUSTICE', 'FUN', '12', '16.99'),
(5,'GOD OF WAR', 'HORROR', '18', '45.99')
;

INSERT INTO customer_order
VALUES
(1,1,1,'2021-02-11 12:34:33'),
(2,1,2,'2021-02-12 12:34:33'),
(3,1,2,'2021-02-12 12:34:33'),
(4,1,5,'2021-02-12 12:34:33'),
(5,5,4,'2021-02-12 12:34:33'),
(6,1,1,'2021-02-12 12:34:33'),
(7,1,2,'2021-02-12 12:34:33'),
(8,10,2,'2021-02-12 12:34:33'),
(9,1,2,'2021-02-12 12:34:33'),
(10,1,2,'2021-02-12 12:34:33'),
(11,2,1,'2021-02-11 16:34:33'),
(12,1,2,'2021-04-13 14:36:33'),
(13,3,2,'2021-02-13 12:34:33'),
(14,5,5,'2021-05-12 09:34:33'),
(15,1,4,'2021-06-12 11:34:33'),
(16,1,1,'2021-03-12 12:34:33'),
(17,7,2,'2021-06-12 15:34:33'),
(18,1,2,'2021-08-12 12:34:33'),
(19,9,2,'2021-01-12 10:34:33'),
(20,1,2,'2021-02-12 12:34:33')
;


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

use cips;


CREATE TABLE decoydata
 (
  CustomerName varchar(255),
  BankAccountNumber int,
  TransactionID int,
  TransactionAmount varchar(255),
  PAN varchar(255) 
);

CREATE TABLE realdata
 (
  CustomerName varchar(255),
  BankAccountNumber int,
  TransactionID int,
  TransactionAmount varchar(255),
  PAN varchar(255) 
);


drop table decoydata;
drop table realdata;
show tables;

ALTER TABLE decoydata
ADD PRIMARY KEY (BankAccountNumber);

ALTER TABLE realdata
ADD PRIMARY KEY (BankAccountNumber);


INSERT INTO decoydata (CustomerName,BankAccountNumber, TransactionID, TransactionAmount,  PAN)
   VALUES
   ( "DecoyName5", 9999999, 999 , "1500.0", "DecoyPan5" );

INSERT INTO decoydata (CustomerName,BankAccountNumber, TransactionID, TransactionAmount,  PAN)
   VALUES
   ( "DecoyName4", 9999998, 888 , "2000.0", "DecoyPan4" );

INSERT INTO decoydata (CustomerName,BankAccountNumber, TransactionID, TransactionAmount,  PAN)
   VALUES
   ( "DecoyName3", 9999997, 777 , "2100.0", "DecoyPan3" );

INSERT INTO decoydata (CustomerName,BankAccountNumber, TransactionID, TransactionAmount,  PAN)
   VALUES
   ( "DecoyName2", 9999996, 666 , "5502.0", "DecoyPan2" );

INSERT INTO decoydata (CustomerName,BankAccountNumber, TransactionID, TransactionAmount,  PAN)
   VALUES
   ( "DecoyName1", 9999995, 555 , "21322.0", "DecoyPan1" );




INSERT INTO realdata (CustomerName,BankAccountNumber, TransactionID, TransactionAmount,  PAN)
   VALUES
   ( "RealName5", 8437290, 666 , "5502.0", "RealPan5" );

INSERT INTO realdata (CustomerName,BankAccountNumber, TransactionID, TransactionAmount,  PAN)
   VALUES
   ( "RealName4", 1029324, 666 , "5502.0", "RealPan4" );

INSERT INTO realdata (CustomerName,BankAccountNumber, TransactionID, TransactionAmount,  PAN)
   VALUES
   ( "RealName3", 3598754, 666 , "5502.0", "RealPan3" );

INSERT INTO realdata (CustomerName,BankAccountNumber, TransactionID, TransactionAmount,  PAN)
   VALUES
   ( "RealName2", 1486721, 666 , "5502.0", "RealPan2" );

INSERT INTO realdata (CustomerName,BankAccountNumber, TransactionID, TransactionAmount,  PAN)
   VALUES
   ( "RealName1", 2932563, 666 , "5502.0", "RealPan1" );





Select * from decoydata;
Select * from realdata;

ALTER TABLE "decoydata"
RENAME COLUMN "Name" TO "CustomerName";

DROP TABLE decoytable;
CREATE DATABASE Product_Data;
Use Product_Data;

Create table Product (
  PID INT NOT NULL,
  PYOM DATE NOT NULL,
  PCategory VARCHAR(50) NOT NULL,
  PBrand VARCHAR(20) NOT NULL,
  PQuantity INT NOT NULL,
  PCost INT NOT NULL,
  PValue INT NOT NULL,
  PRIMARY KEY (PID)
);

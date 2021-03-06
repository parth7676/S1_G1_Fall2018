INSERT INTO Countries(countryName) VALUES ('Canada');

INSERT INTO Provinces (id, provinceName, country_id) VALUES (1, 'Ontario', 1);
INSERT INTO Provinces (id, provinceName, country_id) VALUES (2, 'British Colombia', 1);
INSERT INTO Provinces (id, provinceName, country_id) VALUES (3, 'Alberta', 1);
INSERT INTO Provinces (id, provinceName, country_id) VALUES (4, 'Quebec', 1);
INSERT INTO Provinces (id, provinceName, country_id) VALUES (5, 'Nova Scotia', 1);

INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (1, 'Toronto', 1, 2);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (2, 'Ottawa', 1, 2);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (3, 'Brampton', 1, 2);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (4, 'London', 1, 2);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (5, 'Niagara Falls', 1, 2);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (6, 'Windsor', 1, 2);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (7, 'Vancouver', 1, 3);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (8, 'Richmond', 1, 3);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (9, 'Victoria', 1, 3);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (10, 'Delta', 1, 3);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (11, 'Kimberly', 1, 3);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (12, 'Calgary', 1, 4);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (13, 'Edmonton', 1, 4);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (14, 'Brooks', 1, 4);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (15, 'Cold Lake', 1, 4);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (16, 'Red Deer', 1, 4);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (17, 'Quebec City', 1, 5);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (18, 'Montreal', 1, 5);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (19, 'Laval', 1, 5);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (20, 'Gatineau', 1, 5);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (21, 'Chandler', 1, 5);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (22, 'Halifax', 1, 6);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (23, 'Wolfville', 1, 6);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (24, 'Yarmouth', 1, 6);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (25, 'Digby', 1, 6);
INSERT INTO Cities (id, cityName, country_id, province_id) VALUES (26, 'Mahone Bay', 1, 6);

INSERT INTO Property_Categories(propertyCategory) VALUES ('singleHouse');
INSERT INTO Property_Categories(propertyCategory) VALUES ('attachedHouse');
INSERT INTO Property_Categories(propertyCategory) VALUES ('townHouse');
INSERT INTO Property_Categories(propertyCategory) VALUES ('apartment');
INSERT INTO Property_Categories(propertyCategory) VALUES ('store');
INSERT INTO Property_Categories(propertyCategory) VALUES ('farm');
INSERT INTO Property_Categories(propertyCategory) VALUES ('factory');
INSERT INTO Property_Categories(propertyCategory) VALUES ('mall');
INSERT INTO Property_Categories(propertyCategory) VALUES ('building');
INSERT INTO Property_Categories(propertyCategory) VALUES ('other');

INSERT INTO Property_Facings(propertyFacing) VALUES ('North');
INSERT INTO Property_Facings(propertyFacing) VALUES ('South');
INSERT INTO Property_Facings(propertyFacing) VALUES ('East');
INSERT INTO Property_Facings(propertyFacing) VALUES ('West');
INSERT INTO Property_Facings(propertyFacing) VALUES ('Other');

insert into Property_Sectors (id, propertySector) values (1, 'private');
insert into Property_Sectors (id, propertySector) values (2, 'residential');
insert into Property_Sectors (id, propertySector) values (3, 'commercial');
insert into Property_Sectors (id, propertySector) values (4, 'government');
insert into Property_Sectors (id, propertySector) values (5, 'rural');
insert into Property_Sectors (id, propertySector) values (6, 'other');

insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (1, '679 Partington Avenue', 'Partington Avenue', 679, 'N9B 2N6', '2016-11-23', '2016-10-24', 1, 6, 2, 2, 1300, 202000, 250000, 1, 22, 1, 1, 2, 2, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (2, '200 Lotherton Pathway', 'Lotherton Pathway', 200, 'M4N341', '2014-05-13', '2014-07-20', 2, 8, 4, 2, 3000, 300000, 280000, 1, 1, 1, 1, 2, 2, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (3, '750 Delhi Street', 'Delhi Street', 750, 'M56 TN2', '2013-11-13', '2013-10-15', 2, 7, 3, 2, 2000, 400000, 380000, 1, 4, 1, 2, 2, 2, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (4, '450 Richmod Avenue', 'Richmod Avenue', 450, 'TN6 T48', '2017-03-06', '2017-02-01', 3, 8, 3, 3, 4000, 350000, 380000, 1, 5, 1, 3, 2, 2, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (5, '1011 W Cordova Street', 'W Cordova Street', 1011, 'V6C0B2', '2015-02-25', '2015-06-18', 2, 6, 3, 2, 1500, 75000, 80000, 2, 6, 1, 1, 3, 1, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (6, '10171 Williams Road', 'Williams Road', 10171, 'V7A 1H5', '2010-04-15', '2010-07-18', 1, 7, 5, 2, 2350, 150000, 175000, 4, 7, 1, 1, 3, 3, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (7, '816 Government Streert', 'Government Street', 816, 'V8W1W9', '2011-09-01', '2011-11-04', 1, 3, 1, 1, 1200, 100000, 120000, 2, 8, 1, 2, 3, 4, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (8, '7655 Tamarack Road North West', 'Tamarack Road North West', 7655, 'T6T0N4', '2012-03-09', '2012-05-13', 1, 4, 2, 2, 1487, 300000, 350000, 3, 12, 1, 4, 4, 2, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (9, '454 Discovery Ridge Blvd SW', 'Discovery Ridge Blvd SW', 454, 'T3H5X6', '2009-09-30', '2009-11-28', 1, 4, 2, 2, 2714, 400000, 350000, 1, 11, 1, 4, 4, 2, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (10, '404 5 Ave Plaaza Place', '5 Ave', 404, 'T1R 0T5', '2008-04-11', '2008-06-06', 1, 2, 1, 5, 1500, 50000, 75000, 4, 13, 1, 1, 4, 3, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (11, '1360, Rue Courteline, La Haute-Saint-Charles', 'Rue Courteline, La Haute-Saint-Charles', 1360, 'G3k2k5', '2010-06-25', '2010-08-11', 2, 6, 4, 2, 13700, 500000, 550000, 1, 16, 1, 4, 5, 2, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (12, '1245 RUE REDPATH-CRESCENT, VILLE-MARIE', 'RUE REDPATH-CRESCENT', 1245, 'H3G1A1', '2015-06-21', '2015-11-10', 4, 12, 6, 3, 30000, 1000000, 1200000, 3, 17, 1, 1, 5, 1, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (13, '2309,150 Park Street West', '150 Park Street West', 2309, 'N9A4K8', '2006-11-05', '2006-12-13', 1, 4, 2, 23, 13000, 600000, 550000, 4, 22, 1, 4, 2, 2, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (14, '44 Sowthwell Dr', 'Sowthwell Dr', 44, 'M3B29N', '2008-05-13', '2008-11-28', 2, 5, 3, 2, 1500, 300000, 280000, 1, 1, 1, 1, 2, 2, 1);
insert into Properties (propertyID, propertyTitle, propertyStreet, propertyStreetNumber, propertyPostalCode, propertyConstructionDate, propertyRegistrationDate, propertyNoofHalls, propertyNoofRooms, propertyNoofBathrooms, propertyNoofFloors, propertyTotalArea, propertyAskingPrice, propertySellingPrice, propertyCategory_id, propertyCity_id, propertyCountry_id, propertyFacing_id, propertyProvince_id, propertySector_id, propertyUser_id) values (15, '154 Hamilton Street', 'Hamilton Street', 154, 'M4M2C8', '2013-11-11', '2013-10-10', 1, 3, 2, 11, 1550, 200000, 220000, 4, 1, 1, 2, 2, 2, 1);

INSERT INTO Role_Code (id, roleName, code) VALUES (1, 'uploader', 'PROPERTY_UPLOADER');
INSERT INTO Role_Code (id, roleName, code) VALUES (2, 'verifier', 'PROPERTY_VERIFIER');
INSERT INTO Role_Permission (rolePermissionID, sysFeature, code_id) VALUES (1, 'Uploads the properties to the system', 1);
INSERT INTO Role_Permission (rolePermissionID, sysFeature, code_id) VALUES (2, 'verifies the properties that are posted.', 2);

INSERT INTO User_Role (id, dateAssigned, role_id, user_id) VALUES (1, '2018-10-25', 1, 1);
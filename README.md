Readme file for the pld project as part of the negpod project.
Business Information Portal website

This is a web application built using Python and SQLite, which allows users to access business information through a web interface. This README file provides instructions on how to set up and use the application.

Installation
Clone the repository to your local machine:
bash
 
```
git clone https://github.com/fmhirwa/project-pld3.git
```
Install the required Python libraries listed in the requirements.txt file:
 
```
pip install -r requirements.txt
```
Create a new SQLite database by running the following command in your terminal:
 
```
sqlite3 business_info.db
```
Create the required tables by running the following command in the SQLite terminal:
vbnet
 
```
CREATE TABLE businesses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    address TEXT,
    phone_number TEXT,
    website TEXT
);
```
Insert some sample data into the businesses table by running the following commands in the SQLite terminal:
sql
 
```
INSERT INTO businesses (name, description, address, phone_number, website)
VALUES ('Business A', 'This is the first business', '123 Main St, Anytown USA', '555-1234', 'https://businessa.com');

INSERT INTO businesses (name, description, address, phone_number, website)
VALUES ('Business B', 'This is the second business', '456 Elm St, Anytown USA', '555-5678', 'https://businessb.com');

INSERT INTO businesses (name, description, address, phone_number, website)
VALUES ('Business C', 'This is the third business', '789 Oak St, Anytown USA', '555-9012', 'https://businessc.com');
```
Update the config.py file with your database information.
Usage
To start the web application, run the following command in your terminal:
 
```
python app.py
```
Open a web browser and navigate to http://localhost:5000/ to access the web interface.

You can view a list of all businesses by clicking on the "View All Businesses" link in the navigation menu.

To add a new business, click on the "Add a New Business" link in the navigation menu and fill in the form with the required information.

To edit or delete an existing business, click on the "View All Businesses" link in the navigation menu and then click on the "Edit" or "Delete" button next to the business you want to modify.

Contributing
If you would like to contribute to the development of this application, please fork the repository and submit a pull request.

License
This application is licensed under the MIT license. See the LICENSE file for more information.

Contact ALU for inquiry. Refer to Negpod 11, S22 BSE intake
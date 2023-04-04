# Business Manager

This program allows the user to manage a list of businesses stored in a JSON file. The user can add, delete and display businesses.

## Usage

1. Run the program by typing `python app.py` in the command line.
2. The program will display a menu with the following options:
    1. Add a business
    2. Delete a business
    3. Display all businesses
    4. Quit
3. Enter the number of the option you want to choose and press Enter.
4. Follow the prompts to add or delete a business or to display all businesses.
5. To quit the program, choose option 4 from the menu.

## Data Format

The businesses are stored in a JSON file named `businesses.json`. The file contains a dictionary where the keys are strings representing the business IDs and the values are dictionaries containing the business information.

Each business dictionary has the following keys:
- `name`: The name of the business.
- `description`: A description of the business.
- `location`: The address of the business.
- `phone`: The phone number of the business.
- `website`: The website of the business.

Here is an example of the contents of the `businesses.json` file:

{ “1”: { “name”: “ABC Pharmacy”, “location”: “123 Main Street”, “phone”: “555-1234”, “hours”: “9AM-5PM”, “description”: “A pharmacy that offers prescription and over-the-counter medication.” }, “2”: { “name”: “XYZ Restaurant”, “location”: “456 Broadway”, “phone”: “555-5678”, “hours”: “11AM-9PM”, “description”: “A restaurant that serves a variety of cuisines, including Italian and Mexican.” }, “3”: { “name”: “123 Hardware Store”, “location”: “789 Elm Street”, “phone”: “555-9012”, “hours”: “8AM-6PM”, “description”: “A hardware store that offers tools and supplies for DIY projects.” } }
## Travel Destinations Guide CLI Application
This is a CLI-based application for managing travel destinations, user reviews, and users. It allows users to create, read, update, and delete (CRUD) records for destinations, reviews, and user profiles in an SQLite database. The application uses SQLAlchemy for ORM and Alembic for database migrations.


#### Project Setup
1. Install Dependencies
Before using this project, make sure you have Python 3.x installed on your machine. To set up the project, follow these steps:
* Clone the repository to your local machine:
git clone https://github.com/abigail-salome/phase-3-project
cd travel-destinations-cli
* Install project dependencies using pipenv:pipenv install
* Activate the virtual environment:pipenv shell

2. Set Up the Database
* We are using an SQLite database to store data for destinations, reviews, and users.
* Open the lib/db/seed.py file and add seed data to pre-populate your database (optional).
* Initialize the database with Alembic by applying migrations (see step 3).

3. Run Migrations
* Use Alembic to create and update the database schema based on your models:
* Generate the migration scripts:alembic revision --autogenerate -m "Initial migration"
* Apply the migration:alembic upgrade head

4. Start the Application
* Once the setup is complete, run the CLI application:python lib/cli.py

#### Usage
The CLI menu will provide options for managing destinations, reviews, and users. The commands include:

1. Manage Destinations
#### List Destinations
To list all travel destinations:
* Choose 1 from the main menu.
* The list of destinations will be displayed with their ID, name, and location.

#### Add a Destination
To add a new destination:
* Choose 2 from the main menu.
* Enter the destination’s name, description, and location.
* The new destination will be saved to the database.

#### Update a Destination
To update an existing destination:
* Choose 3 from the main menu.
* Enter the destination ID you want to update.
* Update the fields (leave blank if no changes are needed).
* The destination will be updated.

#### Delete a Destination
To delete a destination:
* Choose 4 from the main menu.
* Enter the ID of the destination you want to delete.
* The destination will be removed from the database.

2. Manage Reviews
#### Add a Review
To add a review to a destination:
* Choose 5 from the main menu.
* Enter the destination ID.
* Provide the review content and rating (1-5).
* The review will be saved to the database.

#### Update a Review
To update an existing review:
* Choose 6 from the main menu.
* Enter the review ID you want to update.
* Update the fields (leave blank if no changes are needed).
* The review will be updated.

#### Delete a Review
To delete a review:
* Choose 7 from the main menu.
* Enter the ID of the review you want to delete.
* The review will be removed from the database.

3. Manage Users
#### List Users
To list all users:
* Choose 8 from the main menu.
* The list of users will be displayed with their ID, name, and email.

#### Add a User
To add a new user:
* Choose 9 from the main menu.
* Enter the user’s name, email, and any additional details.
* The new user will be saved to the database.

#### Update a User
To update an existing user:
* Choose 10 from the main menu.
* Enter the user ID you want to update.
* Update the fields (leave blank if no changes are needed).
* The user will be updated.

#### Delete a User
* To delete a user:
* Choose 11 from the main menu.
* Enter the ID of the user you want to delete.
* The user will be removed from the database.

#### Example Interaction
Here’s an example of how to use the application:

--- Destination & Review Management ---
1. List Destinations
2. Add Destination
3. Update Destination
4. Delete Destination
5. Add Review
6. Update Review
7. Delete Review
8. List Users
9. Add User
10. Update User
11. Delete User
12. Exit
Enter your choice: 2

Enter destination name: Machu Picchu
Enter destination description: Ancient Inca city in Peru
Enter destination location: Peru
Destination 'Machu Picchu' added successfully!

--- Destination & Review Management ---
1. List Destinations
2. Add Destination
3. Update Destination
4. Delete Destination
5. Add Review
6. Update Review
7. Delete Review
8. List Users
9. Add User
10. Update User
11. Delete User
12. Exit
Enter your choice: 9

Enter user name: John Doe
Enter user email: john.doe@example.com
User 'John Doe' added successfully!

#### Running Tests
Tests ensure that your code is functioning as expected. You can run tests using pytest. To run all tests use this command: pytest


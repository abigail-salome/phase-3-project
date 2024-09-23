import sys
from sqlalchemy.orm import sessionmaker
from db.models import Destination, Review, engine, User
from sqlalchemy.exc import NoResultFound

# Start a session
Session = sessionmaker(bind=engine)
session = Session()


# CRUD Functions for Users
def list_users():
    """List all users"""
    users = session.query(User).all()
    if users:
        for user in users:
            print(f"{user.id}: {user.name} - {user.email}")
    else:
        print("No users found.")


def add_user():
    """Add a new user"""
    name = input("Enter user name: ")
    email = input("Enter user email: ")

    new_user = User(name=name, email=email)
    session.add(new_user)
    session.commit()
    print(f"User '{name}' added successfully!")


def delete_user():
    """Delete a user"""
    user_id = input("Enter the user ID to delete: ")
    user = session.get(User, user_id)

    if user:
        session.delete(user)
        session.commit()
        print(f"User '{user.name}' deleted successfully!")
    else:
        print("User not found.")


def add_review():
    """Add a review to a destination"""
    destination_id = input("Enter Destination ID: ")
    user_id = input("Enter User ID: ")
    content = input("Enter Review Content: ")
    rating = int(input("Enter Rating (1-5): "))

    destination = session.get(Destination, destination_id)
    user = session.get(User, user_id)
    if destination and user:
        review = Review(
            content=content, rating=rating, destination=destination, user=user
        )
        session.add(review)
        session.commit()
        print("Review added successfully!")
    else:
        print("Destination or User not found!")


# CRUD Functions for Destinations


def list_destinations():
    """List all destinations"""
    destinations = session.query(Destination).all()
    if destinations:
        for destination in destinations:
            print(f"{destination.id}: {destination.name} - {destination.location}")
    else:
        print("No destinations found.")


def add_destination():
    """Add a new destination"""
    name = input("Enter destination name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    description = input("Enter destination description: ").strip()
    location = input("Enter destination location: ").strip()

    new_destination = Destination(name=name, description=description, location=location)
    session.add(new_destination)
    session.commit()
    print(f"Destination '{name}' added successfully!")


def update_destination():
    """Update an existing destination"""
    try:
        destination_id = int(input("Enter the destination ID to update: "))
        destination = session.get(
            Destination, destination_id
        )  # Updated with Session.get()
        if not destination:
            raise NoResultFound

        print(f"Current Name: {destination.name}")
        destination.name = (
            input("Enter new name (leave blank to keep current): ").strip()
            or destination.name
        )
        print(f"Current Description: {destination.description}")
        destination.description = (
            input("Enter new description (leave blank to keep current): ").strip()
            or destination.description
        )
        print(f"Current Location: {destination.location}")
        destination.location = (
            input("Enter new location (leave blank to keep current): ").strip()
            or destination.location
        )

        session.commit()
        print(f"Destination '{destination.name}' updated successfully!")
    except (ValueError, NoResultFound):
        print("Invalid destination ID. Please try again.")


def delete_destination():
    """Delete a destination"""
    try:
        destination_id = int(input("Enter the destination ID to delete: "))
        destination = session.get(
            Destination, destination_id
        )  # Updated with Session.get()
        if not destination:
            raise NoResultFound

        session.delete(destination)
        session.commit()
        print(f"Destination '{destination.name}' deleted successfully!")
    except (ValueError, NoResultFound):
        print("Invalid destination ID. Please try again.")


# CRUD Functions for Reviews


def add_review():
    """Add a review to a destination"""
    try:
        destination_id = int(input("Enter Destination ID: "))
        destination = session.get(
            Destination, destination_id
        )  # Updated with Session.get()
        if not destination:
            raise NoResultFound

        content = input("Enter Review Content: ").strip()
        rating = int(input("Enter Rating (1-5): "))
        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5.")
            return

        review = Review(content=content, rating=rating, destination=destination)
        session.add(review)
        session.commit()
        print("Review added successfully!")
    except (ValueError, NoResultFound):
        print("Invalid destination ID or input. Please try again.")


def update_review():
    """Update an existing review"""
    try:
        review_id = int(input("Enter the review ID to update: "))
        review = session.get(Review, review_id)  # Updated with Session.get()
        if not review:
            raise NoResultFound

        print(f"Current Content: {review.content}")
        review.content = (
            input("Enter new content (leave blank to keep current): ").strip()
            or review.content
        )
        print(f"Current Rating: {review.rating}")
        new_rating = input(
            "Enter new rating (1-5, leave blank to keep current): "
        ).strip()
        if new_rating and 1 <= int(new_rating) <= 5:
            review.rating = int(new_rating)
        elif new_rating:
            print("Rating must be between 1 and 5.")
            return

        session.commit()
        print(f"Review with ID {review.id} updated successfully!")
    except (ValueError, NoResultFound):
        print("Invalid review ID or input. Please try again.")


def delete_review():
    """Delete a review"""
    try:
        review_id = int(input("Enter the review ID to delete: "))
        review = session.get(Review, review_id)  # Updated with Session.get()
        if not review:
            raise NoResultFound

        session.delete(review)
        session.commit()
        print(f"Review with ID {review.id} deleted successfully!")
    except (ValueError, NoResultFound):
        print("Invalid review ID. Please try again.")


#  CLI menu


def main():
    """Main CLI logic"""
    while True:
        print("\n--- Destination & Review Management ---")
        print("1. List Destinations")
        print("2. Add Destination")
        print("3. Update Destination")
        print("4. Delete Destination")
        print("5. List Users")
        print("6. Add User")
        print("7. Delete User")
        print("8. Add Review")
        print("9. Update Review")
        print("10. Delete Review")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_destinations()
        elif choice == "2":
            add_destination()
        elif choice == "3":
            update_destination()
        elif choice == "4":
            delete_destination()
        elif choice == "5":
            list_users()
        elif choice == "6":
            add_user()
        elif choice == "7":
            delete_user()
        elif choice == "8":
            add_review()
        elif choice == "9":
            update_review()
        elif choice == "10":
            delete_review()
        elif choice == "11":
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

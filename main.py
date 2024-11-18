from sqlalchemy import select, create_engine
from crud import *
from connection import *
from models import User


def clear_users_table(session):
    """Функция для удаления всех записей из таблицы 'users'"""
    confirm = input("Вы уверены, что хотите удалить все записи из таблицы 'users'? (y/n): ").strip().lower()
    if confirm == 'y':
        session.query(User).delete()
        session.commit()
        print("Все записи из таблицы 'users' были удалены.")
    else:
        print("Удаление отменено.")


def is_login_unique(engine, login):
    with Session(engine) as session:
        query = select(User).filter_by(login=login)
        return session.scalars(query).first() is None


def get_all_users(engine):
    with Session(engine) as session:
        query = select(User)
        users = session.scalars(query).all()
        return users


def available_users(engine):
    with Session(engine) as session:
        query = select(User.login)
        for user in session.scalars(query):
            yield user


def main():
    engine = get_engine()
    create_table_ddl(engine)

    while True:
        print("\nMenu:")
        print("1. Add a new user")
        print("2. View all users")
        print("3. Clear all users from the table")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            login = input("Login:\t")

            if not is_login_unique(engine, login):
                print(f"Error: Login '{login}' is already taken. Please choose a different login.")
                continue

            user = User(
                login=login,
                user_fname=input("First Name:\t"),
                user_sname=input("Second Name:\t"),
                password=input("Password:\t")
            )
            create_entry([user], engine)
            print(f"User '{login}' added successfully!")

        elif choice == "2":
            users = get_all_users(engine)
            if users:
                print("\nRegistered Users:")
                for user in users:
                    print(f"Login: {user.login}, First Name: {user.user_fname}, Last Name: {user.user_sname}")
            else:
                print("\nNo users registered yet.")

        elif choice == "3":  # Option to clear all users
            with Session(engine) as session:
                clear_users_table(session)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

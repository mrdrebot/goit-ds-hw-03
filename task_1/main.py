from pymongo import MongoClient
from pymongo.server_api import ServerApi
import db_requests

def main():
    # Connect to MongoDB cloud service
    client = MongoClient(
        "mongodb+srv://cytric:Q1w2e3r$@cluster0.kx21d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        server_api=ServerApi('1')
    )

    # Connect to DB
    db = client.module3
    print("The DB is conected! Make your choiсe:")
    print('''
             1. Add data in DB (add-data)
             2. Find all cats (find-all)
             3. Find one cat by name (find-one <name>)
             4. Update cat age by name (update-one <name> <age>)
             5. Add new feature to features by cat name (add-feature <name> <feature>)
             6. Delete cat by name (delete-one <name>)
             7. Delete data from DB (delete-all)
             close or exit - end program
          ''')

    while True:
        try:
            user_input: str = input("Enter a command: ")
            command, *args = db_requests.parse_input(user_input)

            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "add-data":
                    print(db_requests.add_data(db))
                case "find-all":
                    print(db_requests.find_all(db))
                case "find-one":
                    print(db_requests.find_one(args, db))
                case "update-one":
                    print(db_requests.change_age_by_name(args, db))
                case "add-feature":
                    print(db_requests.add_feature_by_name(args, db))
                case "delete-one":
                    print(db_requests.delete_one_by_name(args, db))
                case "delete-all":
                    print(db_requests.delete_all(db))
                case _:
                    print("Invalid command!")
        except ValueError:
            print("Please, enter a command!")

if __name__ == "__main__":
    main()
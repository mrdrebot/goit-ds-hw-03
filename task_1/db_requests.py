from functools import wraps

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    @wraps(func)
    def inner(*args):
        try:
            return func(*args)
        except ValueError as e:
            return f"Error: { e }"
        except KeyError as e:
            return f"Error: { e }"
        except IndexError as e:
            return f"Error: { e }"

    return inner

# Add data in DB
def add_data(db):
    result_many = db.cats.insert_many(
        [
            {
                "name": 'barsik',
                "age": 3,
                "features": ['ходить в капці', 'дає себе гладити', 'рудий'],
            },
            {
                "name": "Lama",
                "age": 2,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Liza",
                "age": 4,
                "features": ["ходить в лоток", "дає себе гладити", "білий"],
            },
            {
                "name": 'Boris',
                "age": 12,
                "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
            },
            {
                "name": 'Murzik',
                "age": 1,
                "features": ['ходить в лоток', 'дає себе гладити', 'чорний'],
            },

        ]
    )
    print(result_many.inserted_ids)


# Find all cats
@input_error
def find_all(db):
    result = db.cats.find({})
    for el in result:
        print(el)

# Find one cat by name
@input_error
def find_one(args, db):
    result = db.cats.find_one({"name": args[0]})
    print(result)

# Update cat age by name
@input_error
def change_age_by_name(args, db):
    print(args)
    db.cats.update_one({"name": args[0]}, {"$set": {"age": int(args[1])}})
    result = db.cats.find_one({"name": args[0]})
    print(result)

# Add new feature to features by cat name
@input_error
def add_feature_by_name(args, db):
    db.cats.update_one({"name": args[0]}, {"$push": {"features": args[1]}})
    result = db.cats.find_one({"name": args[0]})
    print(result)

# Delete cat by name
@input_error
def delete_one_by_name(args, db):
    db.cats.delete_one({"name": args[0]})

# Delete cat from DB
@input_error
def delete_all(db):
    db.cats.delete_many({})

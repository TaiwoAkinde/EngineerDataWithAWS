# Download and install Mongodb community editio
import pymongo

def db_connection():
    
  client = pymongo.MongoClient("mongodb://localhost:27017/")
  # Note: The database is not created until it is populated by some data
  db = client["example_database"]
  
  return db

def customer_data_insert():
    
  customer_data = [{ "firstname": "Bob", "lastname": "Adams" },
                    { "firstname": "Amy", "lastname": "Smith" },
                    { "firstname": "Rob", "lastname": "Bennet" },]
  try:
    db_obj = db_connection()
    db_obj["customers"].insert_many(customer_data)              
  except Exception as e:
    return e
  
  return "Customers Data Uplaoded"


def items_data_insert():
    
  items_data    = [{ "title": "USB", "price": 10.2 },
                { "title": "Mouse", "price": 12.23 },
                { "title": "Monitor", "price": 199.99 },]
  try:
    db_obj = db_connection()
    db_obj["items"].insert_many(items_data)
  except Exception as e:
    return e

  return "Items Record Uploaded"

def update_rec(table_name, primary_key_field, primary_key_value, field_name, **kwargs):
  statement = table_name.update_many(
    {primary_key_field:primary_key_value},
    {
      "$set":{
        field_name:[
          {
            **kwargs
          }
        ]
      },
    }
  )

  return f"{table_name} table's {field_name} column successfully updated !"
  # amy = customers.update_many(
  #         {"firstname": "Amy"},
  #         {
  #             "$set": {
  #                 "boughtitems":[
  #                     {
  #                         "title": "Monitor",
  #                         "price": 199.99,
  #                         "original_item_id": 3,
  #                         "discounted": False
  #                     }
  #                 ]
  #             } ,
  #         }
  #     )

def create_index(table_name, column_name, index_order="DESCENDING"):
  table_name.create_index([(column_name, pymongo.index_order)])

  return f"Index created on {table_name}"

def get_all_table_recs(table_name, column_name, sort_order):
  items = table_name.find().sort(column_name, pymongo.sort_order)

  for item in items:
    print(item.get(table_name))


print(customer_data_insert())
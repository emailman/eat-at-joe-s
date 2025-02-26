import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def add_item(item_dict):
  app_tables.menu.add_row(**item_dict)

@anvil.server.callable
def get_items():
  # Get a list of items from the menu table
  return app_tables.menu.search(tables.order_by("item_id", ascending=True))

@anvil.server.callable
def delete_item(item):
  # check that the item being deleted exists in the menu
  if app_tables.menu.has_row(item):
    item.delete()
  else:
    raise Exception("Item does not exist")

@anvil.server.callable
def update_item(item, item_dict):
  # check that the article given is really a row in the ‘articles’ table
  if app_tables.menu.has_row(item):
    item.update(**item_dict)
  else:
    raise Exception("Item does not exist")
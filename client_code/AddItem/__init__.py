from ._anvil_designer import AddItemTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AddItem(AddItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Build a list of tuples for the category dropdown
    self.categories = [(cat['category'], cat) 
                       for cat in app_tables.categories.search()]
    
    # Populate the dropdown
    self.category_dropdown_menu.items = self.categories

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    # self.item['image'] = file
    pass

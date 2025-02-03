from ._anvil_designer import OrderForm3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class OrderForm3(OrderForm3Template):
  def __init__(self, **properties):
    # Set form properties and data bindings
    self.init_components(**properties)

    # Load the data from the menu table
    self.repeating_panel_1.items = app_tables.menu.search()


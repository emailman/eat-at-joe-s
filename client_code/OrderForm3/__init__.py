from ._anvil_designer import OrderForm3Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class OrderForm3(OrderForm3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Load the data from the menu table
    self.repeating_panel_1.items = app_tables.menu.search()

    print(self.repeating_panel_1.items[1]['unit_price'])

  def button_decr_click(self, **event_args):
    """Event handler for the decrease button"""
    # Decrease the quantity, but not less than 0
    qty = int(self.text_qty.text)
    if qty > 0:
      self.text_qty.text = qty - 1
      str_unit_price = self.text_unit_price.text

      # Strip the $ from the unit_price
      unit_price = str_unit_price[1:]

      # Calculate the extended price
      ext_price = float(unit_price) * int(self.text_qty.text)
      print(self.text_qty.text, unit_price, ext_price)

      # Show the extended price
      self.text_ext_price.text = f"${ext_price:.2f}"

  def button_incr_click(self, **event_args):
    """Event handler for the increase button"""
    # Increase the quantity, but not more than 10
    qty = int(self.text_qty.text)
    if qty < 10:
      self.text_qty.text = qty + 1
      str_unit_price = self.text_unit_price.text

      # Strip the $ from the unit_price
      unit_price = str_unit_price[1:]

      # Calculate the extended price
      ext_price = float(unit_price) * int(self.text_qty.text)
      print(self.text_qty.text, unit_price, ext_price)

      # Show the extended price
      self.text_ext_price.text = f"${ext_price:.2f}"

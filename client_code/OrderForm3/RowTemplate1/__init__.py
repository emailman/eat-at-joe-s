from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  
  def button_1_click(self, **event_args):
    """This method is called when the "-" button is clicked."""
    # Decrease the quantity, but not less than 0
    qty = int(self.text_qty.text)
    if qty > 0:
      self.text_qty.text = f'{qty - 1:2d}'
      self.calc_extended_price()
      

  def button_2_click(self, **event_args):
    """This method is called when the "+" button is clicked."""
    # Increase the quantity, but not more than 10
    qty = int(self.text_qty.text)
    if qty < 10:
      self.text_qty.text = f'{qty + 1:2d}'
      self.calc_extended_price()

  
  def calc_extended_price(self):
    str_unit_price = self.item['unit_price']

    # Strip the $ from the unit_price
    unit_price = str_unit_price[1:]

    # Calculate the extended price
    ext_price = float(unit_price) * int(self.text_qty.text)

    # Show the extended price
    self.text_ext_price.text = f"${ext_price:.2f}"

    # Raise an event to calculate the total price of the order
    self.parent.raise_event('x-add-prices', item=self.item)
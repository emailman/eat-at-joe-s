from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...AddItem import AddItem


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  
  def button_1_click(self, **event_args):
    """This method is called when the "-" button is clicked."""
    # Decrease the quantity, but not less than 0
    qty = int(self.text_qty.text)
    if qty > 0:
      self.text_qty.text = qty - 1
      self.calc_extended_price()
      

  def button_2_click(self, **event_args):
    """This method is called when the "+" button is clicked."""
    # Increase the quantity, but not more than 10
    qty = int(self.text_qty.text)
    if qty < 10:
      self.text_qty.text = qty + 1
      self.calc_extended_price()

  
  def calc_extended_price(self):
    str_unit_price = self.item['unit_price']

    # Strip the $ from the unit_price
    unit_price = str_unit_price[1:]

    # Calculate the extended price
    ext_price = float(unit_price) * int(self.text_qty.text)

    # Show the extended price
    self.text_ext_price.text = f'${ext_price:.2f}'

    # Raise an event to calculate the total price of the order
    self.parent.raise_event('x-add-prices', item=self.item)

  
  def delete_item_button_click(self, **event_args):
    # Get the user to confirm if they wish to delete the article
    # If yes, raise the 'x-delete-article' event on the parent, 
    # which is the repeating panel on Menu Order page.
    if confirm(f"Are you sure you want to delete:\n{self.item['description']}"):
      self.parent.raise_event('x-delete-item', item=self.item)

  
  def edit_item_button_click(self, **event_args):
    # Create a copy of the existing item from the Data Table 
    item_copy = dict(self.item)
    
    # Open an alert displaying the 'AddItem' Form
    save_clicked = alert(
      content=AddItem(item=item_copy),
      title="Update Item",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )

    # Update the article if the user clicks save
    if save_clicked:
      anvil.server.call('update_item', self.item, item_copy)

      # Now refresh the page
      self.refresh_data_bindings()

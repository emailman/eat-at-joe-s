from ._anvil_designer import OrderForm3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..AddItem import AddItem


class OrderForm3(OrderForm3Template):
  def __init__(self, **properties):
    # Set form properties and data bindings
    self.init_components(**properties)

    # Load the data from the menu table
    self.repeating_panel_1.items = app_tables.menu.search()

    # Handle the event to add the prices for all the items
    self.repeating_panel_1.set_event_handler('x-add-prices', self.add_item_prices)

    # Set an event handler on the Repeating Panel 
    self.repeating_panel_1.set_event_handler('x-delete-item', self.delete_item)
    
  def add_item_prices(self, item, **event_args):
    # Update the total price by adding the extended prices
    # for all items
    sum = 0
    for item in self.repeating_panel_1.get_components():
      sum += float(item.text_ext_price.text[1:])
      # sum += float(item.item['unit_price'][1:]) * int(item.text_qty.text)
    self.text_total.text = f'${sum:.2f}'

  def add_item_button_click(self, **event_args):
    # Initialise an empty dictionary to store the user inputs
    new_item = {}
    # Open an alert displaying the 'AddItem' Form
    save_clicked = alert(
      content=AddItem(item=new_item),
      title="Add Item",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
    # If the alert returned 'True', the save button was clicked.
    if save_clicked:
      anvil.server.call('add_item', new_item)
      self.refresh_items()

  def refresh_items(self):
    # Load existing items from the Data Table, 
    # and display them in the RepeatingPanel
    self.repeating_panel_1.items = anvil.server.call('get_items')

  def delete_item(self, item, **event_args):
    # Delete the article
    anvil.server.call('delete_item', item)

    # Refresh articles to remove the deleted article from the Homepage
    self.refresh_items()

  def button_order_click(self, **event_args):
    """This method is called when the order button is clicked."""
    # Get a new order number
    new_order_id = self.get_new_order_id()

    # Get the fields in all rows of the repeating panel
    for item in self.repeating_panel_1.get_components():
      # Only get info for the row if the item was ordered
      if int(item.text_qty.text) > 0:
        print(
          new_order_id, 
          item.item['item_id'], 
          item.item['description'], 
          int(item.text_qty.text),
          item.item['unit_price'],
          item.text_ext_price.text
        )

        order_dict = {
          'order_id': new_order_id,
          'item_id': item.item['item_id'],
          'description': item.item['description'],
          'qty_ordered': item.text_qty.text,
          'unit_price': float(item.item['unit_price'].lstrip('$')),
          'extended_price': float(item.text_ext_price.text.lstrip('$'))
        }
        anvil.server.call('add_order', order_dict)
        
    self.post_order_tracking(new_order_id, float(self.text_total.text.lstrip('$')))
    
    self.clear_order_qtys()

  def get_new_order_id(self):
    # Get all the current orders 
    orders = anvil.server.call('get_orders')
    
    # Create a list of existing orders ids
    order_list = []
    for order in orders:
      order_list.append(order['order_id'])
    
    # Create a new, unique order id
    return max(order_list) + 1 if order_list  else 1

  def clear_order_qtys(self):
    # Get all the rows of the repeating panel
    for item in self.repeating_panel_1.get_components():
      # Reset the quantity ordered, extended price and total to 0
      item.text_qty.text = 0
      item.text_ext_price.text = '$0.00'
      self.text_total.text = '$0.00'

  def post_order_tracking(self, new_order_id, order_total):
    tracking_order_dict = {
      'order_id': new_order_id,
      'order_total': order_total
    }
    anvil.server.call('add_order_tracking', tracking_order_dict)
          

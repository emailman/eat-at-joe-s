from ._anvil_designer import SpinnerWidgetTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class SpinnerWidget(SpinnerWidgetTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_incr_click(self, **event_args):
    # Increase the quantity, but not more than 10
    qty = int(self.text_qty.text)
    if qty < 10:
      self.text_qty.text = qty + 1

  def button_decr_click(self, **event_args):
    # Decrease the quantity, but not less than 0
    qty = int(self.text_qty.text)
    if qty > 0:
      self.text_qty.text = qty - 1

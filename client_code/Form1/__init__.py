from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
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

from ._anvil_designer import DataCatalogTemplate
from anvil import *
import anvil.server

class DataCatalog(DataCatalogTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def rich_text_1_show(self, **event_args):
    """This method is called when the RichText is shown on the screen"""
    self.n_merchants.text = anvil.server.call('get_merchants')

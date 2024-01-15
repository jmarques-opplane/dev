from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
from ..Homepage import Homepage

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_click(self, **event_args):
    form = get_open_form()
    form.clear()
    form.add_component(Homepage())

from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
from ..NewForm import NewForm

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_new_form(self):
    new_form_instance = NewForm()
    self.content_panel.clear()
    self.content_panel.add_component(new_form_instance)
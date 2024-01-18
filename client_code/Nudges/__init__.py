from ._anvil_designer import NudgesTemplate
from anvil import *
import anvil.server
from ..NudgesInput import NudgesInput
from ..PaymentsInput import PaymentsInput
from ..ExplainabilityConsole_1 import ExplainabilityConsole_1
from .SubscriptionPayments import SubscriptionPayments

class Nudges(NudgesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def see_how_it_works_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(SubscriptionPayments())

  def payments_button_click(self, **event_args):
    self.content_panel.clear()
    #form.content_panel.add_component(PaymentsInput())

  def xai_button_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    form.content_panel.add_component(ExplainabilityConsole_1())

  def salary_deposits_click(self, **event_args):
    self.content_panel.clear()

 


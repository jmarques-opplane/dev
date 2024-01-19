from ._anvil_designer import NudgesTemplate
from anvil import *
import anvil.server
from ..NudgesInput import NudgesInput
from ..PaymentsInput import PaymentsInput
from ..ExplainabilityConsole_1 import ExplainabilityConsole_1
from .SubscriptionPayments import SubscriptionPayments
from .SalaryDeposits import SalaryDeposits
from .ExplainabilityConsole import ExplainabilityConsole

class Nudges(NudgesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def reset_links(self, **event_args):
    self.salary_deposits.role = 'elevated-button'
    self.subscriptions_payments.role = 'elevated-button'
    
  def see_how_it_works_click(self, **event_args):
    self.reset_links()
    self.subscriptions_payments.role = 'selected'
    self.content_panel.clear()
    self.content_panel.add_component(SubscriptionPayments())

  def salary_deposits_click(self, **event_args):
    self.reset_links()
    self.salary_deposits.role = 'filled-button'
    self.salary_deposits.background = "#217bf4"
    self.content_panel.clear()
    self.content_panel.add_component(SalaryDeposits())

  def xai_button_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(ExplainabilityConsole())

  def subscriptions_payments_click(self, **event_args):
    self.reset_links()
    self.subscriptions_payments.role = 'selected'
    self.content_panel.clear()
    self.content_panel.add_component(SubscriptionPayments())


 


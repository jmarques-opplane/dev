from ._anvil_designer import InsightsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from ..FinancialInsights import FinancialInsights

class Insights(InsightsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def read_more_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(FinancialInsights())

  def read_more_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(FinancialInsights())

  def read_more_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(FinancialInsights())

  def read_more_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(FinancialInsights())

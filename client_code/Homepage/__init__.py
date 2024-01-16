from ._anvil_designer import HomepageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from ..Insights import Insights
from ..Lineage import Lineage
from ..TxnEnrichment import TxnEnrichment
from ..Overview import Overview
from ..Nudges import Nudges


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Overview())
    self.dom_nodes["overview_btn"].addEventListener('click', self.overview_click2)
    # Any code you write here will run before the form opens.

  def overview_click2(self, event):
    get_open_form().content_panel.clear()
    #get_open_form().content_panel.add_component(Overview())
    

  def insights_click(self, **event_args):
    """This method is called when the link is clicked"""
    # The top-level form has a component called
    # content_panel. Clear it and put a new Form2() panel there:
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(Insights())

  def nudges_click(self, **event_args):
    """This method is called when the link is clicked"""
    form = get_open_form()
    form.content_panel.clear()
    nudges = Nudges()
    form.content_panel.add_component(nudges)

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(TxnEnrichment())

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(Lineage())

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def overview_click(self, **event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(Overview())

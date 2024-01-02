from ._anvil_designer import HomepageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from ..Insights import Insights
from ..DataCatalog import DataCatalog
from ..Lineage import Lineage
from ..TxnEnrichment import TxnEnrichment
from ..Nudges import Nudges


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Insights())
    # Any code you write here will run before the form opens.

  def insights_click(self, **event_args):
    """This method is called when the link is clicked"""
    # The top-level form has a component called
    # column_panel. Clear it and put a new Form2() panel there:
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(Insights())

  def data_catalog_click(self, **event_args):
    """This method is called when the link is clicked"""
    # The top-level form has a component called
    # column_panel. Clear it and put a new Form2() panel there:
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(DataCatalog())

  def nudges_click(self, **event_args):
    """This method is called when the link is clicked"""
    form = get_open_form()
    form.content_panel.clear()
    nudges = Nudges()
    form.content_panel.add_component(nudges)

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    form = get_open_form()
    form.content_panel.clear()
    txn_enrichment_component = TxnEnrichment()
    form.content_panel.add_component(txn_enrichment_component)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(Lineage())

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def efhef_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

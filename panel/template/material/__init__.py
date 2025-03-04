"""
Material template based on the material web components library.
"""
import pathlib

import param

from ...theme import Design
from ...theme.material import Material
from ..base import BasicTemplate, TemplateActions

_ROOT = pathlib.Path(__file__).parent


class MaterialTemplateActions(TemplateActions):

    _scripts = {
        'open_modal': """
          modal.open();
          setTimeout(function() {{
            window.dispatchEvent(new Event('resize'));
          }}, 200);
        """,
        'close_modal': "modal.close()"
    }


class MaterialTemplate(BasicTemplate):
    """
    MaterialTemplate is built on top of Material web components.
    """

    sidebar_width = param.Integer(default=370, doc="""
        The width of the sidebar in pixels. Default is 370.""")

    design = param.ClassSelector(class_=Design, default=Material, constant=True,
                                 is_instance=False, instantiate=False, doc="""
        A Design applies a specific design system to a template.""")

    _actions = param.ClassSelector(
        default=MaterialTemplateActions(), class_=TemplateActions)

    _css = [_ROOT / "material.css"]

    _template = _ROOT / 'material.html'

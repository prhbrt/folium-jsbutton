
__version__ = '0.1.0'

from branca.element import CssLink, Figure, JavascriptLink, MacroElement

from jinja2 import Template

class JsButton(MacroElement):
    """
    Button that executes a javascript function.
    Parameters
    ----------
    title : str
         title of the button, may contain html like 
    function : str
         function to execute, should have format `function(btn, map) { ... }`
          
    See https://github.com/prinsherbert/folium-jsbutton.
    """
    _template = Template("""
        {% macro script(this, kwargs) %}
        L.easyButton(
            '<span>{{ this.title }}</span>',
            {{ this.function }}
        ).addTo({{ this.map_name }});
        {% endmacro %}
        """)

    def __init__(self, title='', function="""
        function(btn, map){
            alert('no function defined yet.');
        }
    """):
        super(JsButton, self).__init__()
        self.title = title
        self.function = function

    def add_to(self, m):
        self.map_name = m.get_name()
        super(JsButton, self).add_to(m)

    def render(self, **kwargs):
        super(JsButton, self).render()

        figure = self.get_root()
        assert isinstance(figure, Figure), (
            'You cannot render this Element if it is not in a Figure.')

        figure.header.add_child(
            JavascriptLink('https://cdn.jsdelivr.net/npm/leaflet-easybutton@2/src/easy-button.js'),  # noqa
            name='Control.EasyButton.js'
        )

        figure.header.add_child(
            CssLink('https://cdn.jsdelivr.net/npm/leaflet-easybutton@2/src/easy-button.css'),  # noqa
            name='Control.EasyButton.css'
        )

        figure.header.add_child(
            CssLink('https://use.fontawesome.com/releases/v5.3.1/css/all.css'),  # noqa
            name='Control.FontAwesome.css'
        )


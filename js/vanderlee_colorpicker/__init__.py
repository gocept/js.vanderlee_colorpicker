from js.jquery import jquery
from js.jqueryui import jqueryui
import fanstatic


library = fanstatic.Library('colorpicker', 'resources')


colorpicker_css = fanstatic.Resource(
    library, 'jquery.colorpicker.css', minified='jquery.colorpicker.min.css')
colorpicker = fanstatic.Resource(
    library, 'jquery.colorpicker.js', minified='jquery.colorpicker.min.js',
    depends=[jquery, jqueryui, colorpicker_css])

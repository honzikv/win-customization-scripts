from lib.logger_factory import create_logger
from lib.selection_box import set_selection_box_color
import webcolors

_logger = create_logger(__name__)

color = webcolors.name_to_rgb('crimson')
_logger.info(f'Color = {color}')

set_selection_box_color(color)

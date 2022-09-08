import logging
import winreg
import webcolors
from typing import Tuple

from lib.logger_factory import create_logger

# This module contains scripts relevant to the selection box

_logger = create_logger(__name__)

# Must be added to HKEY_CURRENT_USER
_COLORS_KEY = r'Control Panel\Colors'

_COLORABLE_PARAMS = {'Hilight', 'HotTrackingColor'}
_TEXT_PARAMS = {'HilightText'}


def set_selection_box_color(color: Tuple[int, int, int]):
    """
    Sets drag selection box and hot tracking color in the registry
    :param color: Tuple of RGB values
    """
    color_name = webcolors.hex_to_name(webcolors.rgb_to_hex(color))
    _logger.info(f'Setting selection box color to {color_name}')

    try:
        # Try getting the key
        parent = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, _COLORS_KEY, 0, winreg.KEY_ALL_ACCESS)
    except FileNotFoundError as err:
        logging.error(
            f'Could not find parent key for: {_COLORS_KEY}, the selection box color will not be changed. Caused by {err}')
        return

    for key in _COLORABLE_PARAMS:
        winreg.SetValueEx(parent, key, 0, winreg.REG_SZ, f'{color[0]} {color[1]} {color[2]}')
        
    _logger.info('Selection box color set successfully')

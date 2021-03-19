# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Editor Swap",
    "author" : "carlosmu <carlos.damian.munoz@gmail.com>",    
    "blender" : (2, 83, 0),
    "version" : (0, 6, 0),
    "category" : "User",
    "location" : "Editors headers",
    "description" : "Swapping between paired editors.",
    "warning" : "",
    "doc_url" : "https://github.com/carlosmu/editor_swap",
    "tracker_url" : "https://github.com/carlosmu/editor_swap/issues",
}

import bpy

from . import draw_button
from . import ot_editor_swap
from . import user_prefs



####################################
# REGISTER/UNREGISTER
####################################
def register():
    draw_button.register()
    ot_editor_swap.register() 
    user_prefs.register() 
        
def unregister():
    draw_button.unregister()
    ot_editor_swap.unregister() 
    user_prefs.unregister() 


"""
TO-DO
- Editors based on preferences properties
- Keymap cunfigurable by preferences
- Custom buttons based on properties
- Restore Defaults button (or deactivate, activate)
- Add "None" option to editors selector


"""


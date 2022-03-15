# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

"""
Contains objects which auto-attach on parent
Theses objects should be in the parent, they are not displayed by default
they have got :

    * init(parent), which auto attach on parent
    * show(...), which show the object
    * close(..), to hide the object

except "Clipboard", which have init(parent) & copy(str)

"""

from .mbox import MBox
from .toaster import Toaster
from .popmenu import PopMenu
from .clipboard import Clipboard

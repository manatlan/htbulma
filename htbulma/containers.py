# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

"""
Only containers can contain multiple objects ...
(like Box(*obj))

"""

from htag import Tag
from . import TagBulma

class VBox(TagBulma):
    statics = [Tag.H.style("""
.vbox {display: flex;flex-flow: column nowrap;}
.vbox > * {flex: 1 1 auto;margin:1px !important;}
""")]

    def __init__(self,*objs,**a):
        super().__init__(**a)
        self.classEnsure("vbox")
        for o in objs:
            self <= o


class HBox(TagBulma):
    statics = [Tag.H.style("""
.hbox {display: flex;flex-flow: row nowrap;align-items:center}
.hbox > * {flex: 1 1 auto;margin:1px !important;}
""")]

    def __init__(self,*objs,**a):
        super().__init__(**a)
        self.classEnsure("hbox")
        for o in objs:
            self <= o

class Box(TagBulma):
    def __init__(self,*objs,**a):
        super().__init__(**a)
        self.classEnsure("box")
        for o in objs:
            self <= o


class Section(TagBulma,Tag.section):
    def __init__(self,*objs,**a):
        super().__init__(**a)
        self.classEnsure("section")
        for o in objs:
            self <= o

if __name__=="__main__":
    obj=Section( )
    obj<= Box("Hello")
    obj<= HBox( Box(1),Box(2),Box(3) )
    obj<= VBox( Box(1),Box(2),Box(3) )

    from . import _test
    _test( obj )

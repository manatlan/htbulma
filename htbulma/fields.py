# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from . import TagBulma, A
from htag import Tag


class Fields(Tag.fieldset,TagBulma):
    """ Just a helper to produce beautiful bulma forms """
    def __init__(self, **a): # accept bool "_disabled" !!!
        super().__init__(**a)

    def addField(self, label, obj,info=None):
        left = Tag.div( Tag.div(label,_class="label"), _class="field-label is-normal")
        contents=[Tag.div(obj,_class="control")]
        if info: contents.append( Tag.p(info,_class="help") )
        right = Tag.div( Tag.div( contents,_class="field"), _class="field-body")
        self <= Tag.div( [left,right], _class="field is-horizontal")

if __name__=="__main__":


    nav= Fields()
    nav.addField( "zone1 ", "object1" )
    nav.addField( "zone2 ", "object2", "help2" )

    from . import _test
    _test( nav )

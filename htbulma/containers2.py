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
from . import TagBulma,Button


class Flex(Tag.div):
    """ kind of hbox/vbox, but maximized (w/h @ 100%, without overflow).
        so, contents are overflow'able
    """
    def __init__(self,orientation:str,*objs,**k):
        assert orientation in ["row","column"]
        Tag.div.__init__(self,**k)
        self["style"]=f"display: flex;flex-flow: {orientation} nowrap;align-items:center;align-items: stretch;width:100%;height:100%;overflow:hidden"

        if objs:
            objs=list(objs)
            first=objs.pop(0)
            self.addNormal(first)
            for obj in objs:
                self.addFluid(obj)

    def append(self,obj,flex="1 0 auto"):   # shrinked by default !
        self <= Tag.div( obj, _style=f"flex:{flex};overflow:auto;")

    def addNormal(self,obj):
        """ shortcut """
        self.append(obj,"1 0 auto")
    def addFluid(self,obj):
        """ shortcut """
        self.append(obj,"1 1 auto")


class VFlex(Flex):
    """ vertical flex, first object keep its sizes, others expand (ideal to build a layout)"""
    def __init__(self,*objs,**attrs):
        Flex.__init__(self,"column",*objs,**attrs)


class HFlex(Flex):
    """ horizontal flex, first object keep its sizes, others expand (ideal to build a layout)"""
    def __init__(self,*objs,**attrs):
        Flex.__init__(self,"row",*objs,**attrs)



if __name__=="__main__":


    o=VFlex("TOP TITLE", VFlex( Button("BIG"),  HFlex( [Tag.div("MENU OP") for i in range(100)],"hello "*10000)) )

    from . import _test
    _test( o )

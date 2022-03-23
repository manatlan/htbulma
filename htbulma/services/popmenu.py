# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

from htag import Tag
from .. import TagBulma,Button


class PopMenu(TagBulma):
    tag="span"

    def __init__(self, parent):
        """ auto attach on 'parent' """
        TagBulma.__init__(self)
        parent <= self
        self._parent = parent
        self._menu={}

    def show(self,x:int,y:int,entries:dict):
        self._menu=dict(
            pos=dict(x=x,y=y),
            entries=entries,
        )

    def __str__(self):
        self.clear()
        if self._menu and self._menu.get("entries"):
            entries=Tag.H.ul(_class="menu-list")
            for name,callback in self._menu["entries"].items():
                entries<= Tag.H.li( Tag.H.a(name,_onclick=self.bind.close(name)) )

            if "pos" in self._menu:
                fix="left:%spx;top:%spx" % (self._menu["pos"]["x"],self._menu["pos"]["y"])
            else:
                fix=""

            self <= Tag.H.div(
                _class="modal-background",
                _onclick=self.bind.close(),
                _style="background-color:inherit"
            )
            self <= Tag.H.div(
                Tag.H.aside( entries,_class="menu"),
                _class="card",
                _style="position:fixed;z-index:10000;padding:2px;"+fix,
            )

        return TagBulma.__str__(self)

    def close(self,name=None):
        if name:
            self._menu["entries"][name]()

        self._menu=None

    def binder(self, callbackName: str) -> str:
        """ bind to a parent method called 'callbackName', which should be callbackName(self,x,y) """
        return getattr(self._parent.bind, callbackName)(b"event.clientX",b"event.clientY")


if __name__=="__main__":
    class Obj(Tag):
        def __init__(self,**a):
            Tag.__init__(self,**a)

            self.pop = PopMenu(self)

            self <= Button("yo", _onclick=self.pop.binder("aff") )  #TODO: CAN DO BETTER HERE

        def aff(self,x,y):
            entries=dict(
                menu1= lambda: self.nothing(1),
                menu2= lambda: self.nothing(2),
            )
            self.pop.show(x,y, entries)

        def nothing(self,v):
            print("do nothing",v)


    from .. import _test
    _test( Obj() )

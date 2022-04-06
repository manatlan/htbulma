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

class Nav(TagBulma):
    tag="nav"

    def __init__(self, title):
        super().__init__()
        self["role"]="navigation"
        self["aria-label"]="main navigation"
        self.classEnsure("navbar is-fixed-top is-black")
        self.title = title
        self._entries_first = {}
        self._entries_end = {}

        self.update()

    def addEntry(self,name,callback,atEnd=False):
        if atEnd:
            self._entries_end[name]=callback
        else:
            self._entries_first[name]=callback
        self.update()

    def update(self):  # DYNAMIC RENDERING HERE !
        self.clear()
        divBrand = Tag.H.div(_class="navbar-brand")
        divBrand <= Tag.H.b(self.title,  _class="navbar-item")
        if self._entries_first or self._entries_end:
            divBrand <= A(
                [Tag.H.span(_aria_hidden=True),
                Tag.H.span(_aria_hidden=True),
                Tag.H.span(_aria_hidden=True),
                ],
                _role="button",
                _class="navbar-burger burger",
                _aria_label="menu",
                _aria_expanded="false",
                _data_target="navbarBasicExample",
                _onclick="this.classList.toggle('is-active');document.querySelector('.navbar-menu').classList.toggle('is-active')",
            )

        menu = Tag.H.div(_class="navbar-start")
        for k, v in self._entries_first.items():
            menu <= A(k, _class="navbar-item", _onclick=self.bind.evtSelectEntry(k))

        if self._entries_end:
            menuEnd = Tag.H.div(_class="navbar-end")
            for k, v in self._entries_end.items():
                menuEnd <= A(k, _class="navbar-item", _onclick=self.bind.evtSelectEntry(k))
        else:
            menuEnd = None

        divMenu = Tag.H.div( [menu, menuEnd], _class="navbar-menu")

        self <= divBrand
        self <= divMenu

    def evtSelectEntry(self, name):
        self("document.querySelector('.navbar-menu').classList.remove('is-active')")
        self("document.querySelector('.navbar-burger').classList.remove('is-active')")
        entries = {**self._entries_first,**self._entries_end}
        callback = entries[name]
        callback()

if __name__=="__main__":

    def nothing():
        print("do nothing")

    def add():
        nav.addEntry( "added page%s" %len(nav._entries_first), nothing )

    nav= Nav("Nav Demo")
    # nav.addEntry( "Add a Page ", add )
    # nav.addEntry( "exit", nothing, True )


    from . import _test
    _test( nav )

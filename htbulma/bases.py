# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from htag import Tag
from . import TagBulma

class Progress(TagBulma):

    def __init__(self,**a):
        self.tag="progress" # enforce the html tag (bicoz TagBulma is nativly a div)
        super().__init__(**a)
        self["class"].add("progress","is-dark")

class Loader(TagBulma):
    """ it's clearly not the best bulma way to got that ;-)"""
    def __init__(self,**a):
        self.tag="span" # enforce the html tag (bicoz TagBulma is nativly a div)
        super().__init__(None,**a)
        self["class"].add("button","is-loading")
        self["style"].set("border","0px !important")


class Content(TagBulma):

    def __init__(self,txt=None,**a):
        super().__init__(**a)
        self["class"].add("content")
        self <= txt


class Button(TagBulma):

    def __init__(self,txt=None,**a):
        self.tag="button" # enforce the html tag (bicoz TagBulma is nativly a div)
        super().__init__(**a)
        self["class"].add("button","is-link")
        self <= txt


class A(TagBulma):

    def __init__(self,txt,**a):
        self.tag="a" # enforce the html tag (bicoz TagBulma is nativly a div)
        super().__init__(**a)
        self["class"].add("a","is-link")
        self <= txt



if __name__=="__main__":
    obj=Tag.div( )
    obj<= Button("Hello")
    obj<= Button("Hello", _class="is-small")
    obj<= Button("Hello",_class="is-success")
    obj<= A("Hello",_href="#")
    obj <= Progress()
    obj <= Loader()

    from . import _test
    _test( obj )

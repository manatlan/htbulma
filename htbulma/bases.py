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

class Progress(TagBulma,Tag.progress):

    def __init__(self,**a):
        super().__init__(**a)
        self.classEnsure("progress is-dark")

class Content(TagBulma,Tag.div):

    def __init__(self,txt=None,**a):
        super().__init__(**a)
        self.classEnsure("content")
        self <= txt


class Button(TagBulma,Tag.button):

    def __init__(self,txt=None,**a):
        super().__init__(**a)
        self.classEnsure("button is-link")
        self <= txt


class A(TagBulma,Tag.a):

    def __init__(self,txt,**a):
        super().__init__(**a)
        self.classEnsure("a is-link")
        self <= txt



if __name__=="__main__":
    obj=Tag.div( )
    obj<= Button("Hello")
    obj<= Button("Hello", _class="is-small")
    obj<= Button("Hello",_class="is-success")
    obj<= A("Hello",_href="#")

    from . import _test
    _test( obj )

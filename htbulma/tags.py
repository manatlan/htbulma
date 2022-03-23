# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from . import TagBulma
from htag import Tag

class Tags(TagBulma):
    tag="div"
    """
        tags:       mutable list of tags (should be in choices)
        choices:    complete list of available tags
        editable :  can edit the tags or not
    """

    def __init__(self, tags: list, choices: list, editable=True,**a):
        super().__init__(**a)
        self.tags = tags
        self.editable = editable
        self.choices = choices
        self.update()

    def update(self):
        self.clear()
        for i in self.choices:
            if self.editable:
                klass = "tag is-success" if i in self.tags else "tag"
                self.add(
                    Tag.H.span(
                        i,
                        _class=klass,
                        _onclick=self.bind.switch(i),
                        _style="cursor:pointer",
                    )
                )
            else:
                if i in self.tags:
                    self.add(Tag.H.span(i, _class="tag is-success"))
            self.add(" ")

    def switch(self, t):
        if t in self.tags:
            self.tags.remove(t)
        else:
            self.tags.append(t)
        self.update()

if __name__=="__main__":

    ll = ["banana", "apple", "pear", "peach", "melon", "cherry", "plum"]
    obj=Tags( [ll[3],ll[5]], ll)

    from . import _test
    _test( obj )

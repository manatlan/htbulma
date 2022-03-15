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

class _Selector(TagBulma): # not HTAG OPTIMIZED, and others too!
    def __init__(self, value, choices: list, disabled=False, onchange=None,**a):
        super().__init__(**a)
        assert value in choices
        self.value = value
        self.choices = choices
        self.disabled = disabled
        self.onchange = onchange
        self.update()

    def _selectVal(self, idx):
        self.value = self.choices[int(idx)]
        if self.onchange:
            self.onchange(self.value)
        self.update()


class TabsHeader(_Selector):  # TODO: implement disabled
    tag="div"

    def update(self):
        self.clear()
        self.classEnsure("tabs is-centered")

        u = Tag.ul()
        for idx, i in enumerate(self.choices):
            isActive = "is-active" if self.value == i else None
            u <= Tag.li(A(i, _onclick=self.bind._selectVal(idx)), _class=isActive)
        self <= u



class RadioButtons(_Selector):
    tag="div"

    def update(self):
        self.clear()
        self.classEnsure("control")

        for idx, i in enumerate(self.choices):
            self <= Tag.label(
                        [
                            Tag.input(
                                _type="radio",
                                _class="radio",  # override
                                _name="r%s" % id(self),
                                _onclick=self.bind._selectVal(idx),
                                _checked=(self.value == i),
                                _disabled=bool(self.disabled),
                            ),
                            i
                        ],
                        _class="radio",
                    )

class SelectButtons(_Selector):  # TODO: add disabled ?
    tag="div"

    def update(self):
        self.clear()
        self.classEnsure("tabs is-toggle")
        u = Tag.ul()
        for idx, i in enumerate(self.choices):
            isActive = "is-active" if self.value == i else None
            u<=Tag.li(A(i, _onclick=self.bind._selectVal(idx)), _class=isActive)
        self <= u


class Select(_Selector):
    tag="div"

    def update(self):
        self.clear()
        self.classEnsure("select")
        s = Tag.select(
            _onchange=self.bind._selectVal(b"this.value"),
            _style="width:100%",
            _disabled=bool(self.disabled),
        )
        for idx, i in enumerate(self.choices):
            s <= Tag.option(i, _value=idx, _selected=(self.value == i))

        self <= s


if __name__=="__main__":

    s = 2
    obj=Tag.div( )
    obj<=TabsHeader(s, [1, 2, 3] )
    obj<=RadioButtons(s, [1, 2, 3]),
    obj<=SelectButtons(s, [1, 2, 3]),
    obj<=Select(s, [1, 2, 3] ),

    from . import _test
    _test( obj )

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


class InputText(TagBulma): # not HTAG OPTIMIZED
    tag="input"

    def __init__(self, value, type="text", disabled=False, onchange=None,**a):
        super().__init__(**a)
        self.classEnsure("input")
        self["type"]=type
        self["onchange"]=self.bind.changeValue(b"this.value")

        self.value = value
        self.disabled = disabled
        self.onchange = onchange
        self.update()

    def update(self):
        self["disabled"]=self.disabled
        self["value"]= self.value

    def changeValue(self, value):
        self.value = value
        if self.onchange:
            self.onchange(self.value)
        self.update()


class TextArea(TagBulma):    # not HTAG OPTIMIZED
    tag="textarea"

    def __init__(self, value, disabled=False, onchange=None,**a):
        super().__init__(**a)
        self.classEnsure("input")
        self["onchange"]=self.bind.changeValue(b"this.value")

        self.value = value
        self.disabled = disabled
        self.onchange = onchange
        self.update()

    def update(self):
        self.clear()
        self["disabled"]=self.disabled
        self<=self.value

    def changeValue(self, value):
        self.value = value
        if self.onchange:
            self.onchange(self.value)
        self.update()

class Checkbox(TagBulma):
    tag="div"

    def __init__(self, value: bool, title: str, disabled=False, onchange=None,**a):
        super().__init__(**a)
        self.value = value
        self.title = title
        self.disabled = disabled
        self.onchange = onchange
        self.update()

    def update(self):
        self.clear()
        self.add(
            Tag.label(
                [
                    Tag.input(
                        _checked=self.value,
                        _type="checkbox",
                        _class="checkbox",
                        _onclick=self.bind.switch(),
                        _disabled=self.disabled,
                    ),
                    self.title,
                ],
                _class="checkbox",
            )
        )

    def switch(self):
        self.value = not self.value
        if self.onchange:
            self.onchange(self.value)
        self.update()



class Slider(TagBulma):
    tag="input"

    def __init__(self, value, min=None, max=None, step=None, onchange=None,**a):
        TagBulma.__init__(self,**a)
        self["type"]="range"
        self.classEnsure("slider is-fullwidth")
        self["value"]=value
        self["min"]=min
        self["max"]=max
        self["step"]=step
        self["oninput"] = self.bind.changeValue(b"this.value")
        self.onchange = onchange

    def changeValue(self,v):
        self["value"] = v
        if self.onchange:
            self.onchange(v)

if __name__=="__main__":
    obj=Tag.div( )
    obj <= Input()
    obj <= InputText("hello")
    obj <= TextArea("hello")
    obj <= Checkbox(True,"Yolo")
    obj <= Slider(42,0,100)

    from . import _test
    _test( obj )

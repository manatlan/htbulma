# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

from . import TagBulma,Slider,InputText
from htag import Tag
import json

class Form(Tag.form):
    def __init__(self,onsubmit=None,**a):
        Tag.__init__(self,**a)
        self["onsubmit"]="%s;event.preventDefault();" % self.bind._onsubmit(b"JSON.stringify(Object.fromEntries(new FormData(this)))")
        self.onsubmit = onsubmit

    @Tag.NoRender # avoid redrawing itself
    def _onsubmit(self,f):
        if self.onsubmit:
            self.onsubmit(json.loads(f))


if __name__=="__main__":
    def onsubmit(form: dict):
        print(form)

    obj=Form(onsubmit=onsubmit)
    obj<=InputText("",_name="txt")
    obj<=Tag.H.input(_name="txt2",_value="", _class="input")
    obj<=Slider(1,1,100,_name="sel")
    obj<=Tag.H.input(_type="submit",_value="ok", _class="button")

    from . import _test
    _test( obj )

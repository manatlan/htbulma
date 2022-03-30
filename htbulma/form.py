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
import json

class Form(Tag.form):
    def __init__(self,onsubmit=None,**a):
        Tag.__init__(self,**a)
        # rewrite the form.submit() (bicoz this method doesn't call the onsubmit ;-( )
        self.js = """tag.submit=function() {%s}""" % self.bind._onsubmit(b"JSON.stringify(Object.fromEntries(new FormData(this)))")

        self["onsubmit"]="event.preventDefault();this.submit()"
        self._callback = onsubmit

    @Tag.NoRender # avoid redrawing itself
    def _onsubmit(self,f:dict):
        if self._callback:
            self._callback(json.loads(f))


if __name__=="__main__":
    def onsubmit(form: dict):
        print(form)

    obj=Form(onsubmit=onsubmit)
    obj<=Tag.H.input(_name="txt1",_value="1", _class="input")
    obj<=Tag.H.input(_name="txt2",_value="2", _class="input")
    obj<=Tag.H.input(_name="txt3",_value="3", _class="input")
    obj<=Tag.H.input(_type="submit",_value="ok", _class="button")

    from . import _test
    _test( obj )

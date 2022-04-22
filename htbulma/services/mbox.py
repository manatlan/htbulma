# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from .. import TagBulma,Button,Box,HBox,Content
from htag import Tag

class MBox(TagBulma):
    tag="div"

    imports = Button,Box,HBox,Content

    def __init__(self, parent):
        """ auto attach on 'parent' """
        super().__init__()
        self["info"]="mbox"
        parent.add( self )

    def show(self, content, canClose=True, full=False):
        self.clear()
        o = Tag.H.div(_class = "modal is-active")

        jsclose= self.bind.close()

        o <= Tag.H.div(_class="modal-background", _onclick=jsclose)
        if canClose:
            o <= Tag.H.div(
                    _class="modal-close is-large",
                    _aria_label="close",
                    _onclick=jsclose,
                )

        o <= Tag.H.div( Box( content , _style="height:100%;overflow-y:auto" if full else None) , _class="modal-content", _style = "width:90%;height:98%;" if full else None )


        self.add( o )

    def confirm(self, content, ok, ko=None,txtok="OK",txtko="Cancel"):
        self._cbok = ok
        self._cbko = ko
        js = """if (event.keyCode === 27) {event.preventDefault();%s;}""" % self.bind._confirm(0)

        main = Content( content )
        main <= HBox(
            Tag.H.div(_style="flex: 1 0 25%;"),
            Tag.H.div(_style="flex: 1 0 25%;"),
            Button(txtko, _onclick=self.bind._confirm(0), _class="is-light",_style="flex: 1 0 25%;"),
            Button(txtok, _onclick=self.bind._confirm(1), js="tag.focus()",_onkeyup = js , _style="flex: 1 0 25%;"),
        )
        self.show(main, canClose=True)

    def _confirm(self, ok):
        self.close()
        if ok and self._cbok:
            self._cbok()
        elif self._cbko:
            self._cbko()


    def prompt(self, title, defaultValue, ok, ko=None,txtok="OK",txtko="Cancel"):
        self._cbok = ok
        self._cbko = ko

        js =  """if (event.keyCode === 13) {event.preventDefault();%s;}""" % self.bind._prompt(b"this.value")
        js += """if (event.keyCode === 27) {event.preventDefault();%s;}""" % self.bind._prompt()
        input = Tag.input(_value=defaultValue, js="tag.focus();tag.setSelectionRange(0, tag.value.length)", _class="input", _onkeyup = js)

        main = Content( Tag.h3(title) )
        main <= input
        main <= HBox(
            Tag.H.div(_style="flex: 1 0 25%;"),
            Tag.H.div(_style="flex: 1 0 25%;"),
            Button(txtko, _onclick=self.bind._prompt(), _class="is-light",_style="flex: 1 0 25%;"),
            Button(txtok, _onclick=self.bind._prompt( b"document.getElementById('%d').value" % id(input)) ,_style="flex: 1 0 25%;"),
            _style="margin-top:10px"
        )
        self.show(main, canClose=True)

    def _prompt(self, value=None):
        self.close()
        if (value is not None) and self._cbok:
            self._cbok(value)
        elif self._cbko:
            self._cbko()


    def close(self):
        self.clear()



if __name__=="__main__":
    def majok(v=None):
        print("ok",v)
    def majko():
        print("ko")

    obj=Tag( )
    # MBox(obj).show( Content("YO"),  )
    # MBox(obj).show( Content("YO"), full=True )
    # MBox(obj).confirm("hello ? sure ?????", ok=majok, ko=majko)
    MBox(obj).prompt("What's your name ?","john doe", ok=majok, ko=majko)

    from .. import _test
    _test( obj )

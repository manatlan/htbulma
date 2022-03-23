# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from .. import TagBulma,Button,Box,Content,HBox
from htag import Tag

class MBox(TagBulma):
    tag="div"

    def __init__(self, parent):
        """ auto attach on 'parent' """
        super().__init__()
        self["info"]="mbox"
        parent.add( self )

    def show(self, content, canClose=True):
        self.clear()
        o = Tag.H.div(_class = "modal is-active")

        jsclose= self.bind.close()

        if canClose:
            o <= Tag.H.div(_class="modal-background", _onclick=jsclose)
            o <= Tag.H.div(
                    _class="modal-close is-large",
                    _aria_label="close",
                    _onclick=jsclose,
                )
        else:
            o <= Tag.H.div(_class="modal-background")

        o <= Tag.H.div( Box(content), _class="modal-content")
        self.add( o )

    def confirm(self, content, ok, ko=None,txtok="OK",txtko="Cancel"):
        self.ok = ok
        self.ko = ko
        main = Tag.H.div( content )
        main <= HBox(
            Tag.H.button(txtko, _class="button is-light", _onclick=self.bind._confirm(0)),
            Button(txtok, _onclick=self.bind._confirm(1)),
            _style="text-align:right"
        )
        self.show(main, canClose=True)

    def _confirm(self, ok):
        self.close()
        if ok and self.ok:
            self.ok()
        elif self.ko:
            self.ko()


    def close(self):
        self.clear()



if __name__=="__main__":
    def majok():
        print("ok")
    def majko():
        print("ko")

    obj=Tag( )
    # MBox(obj).show( Content("YO") )
    MBox(obj).confirm("hello ? sure ?????", ok=majok, ko=majko)

    from .. import _test
    _test( obj )

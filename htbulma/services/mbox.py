# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from .. import TagBulma,Button,Box
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
        o = Tag.div(_class = "modal is-active")

        jsclose= self.bind.close()

        if canClose:
            o <= Tag.div(_class="modal-background", _onclick=jsclose)
            o <= Tag.div(
                    _class="modal-close is-large",
                    _aria_label="close",
                    _onclick=jsclose,
                )
        else:
            o <= Tag.div(_class="modal-background")

        o <= Tag.div( Box(content), _class="modal-content")
        self.add( o )

    def close(self):
        self.clear()



if __name__=="__main__":


    obj=Tag( )
    MBox(obj).show("YO")

    from .. import _test
    _test( obj )

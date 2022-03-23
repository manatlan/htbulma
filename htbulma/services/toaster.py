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


class Toaster(TagBulma):
    tag="div"
    statics=[]

    def __init__(self, parent):
        """ auto attach on 'parent' """
        super().__init__()
        self["info"]="toaster"
        parent.add( self )

    def show(self,content,delay=2000): #TODO: can't be called immediatly ;-( (coz __caller__ for js interact)
        self.clear()

        jsclose= self.bind.close()

        o = Tag.H.div( _class="notification has-text-light has-background-grey",_style = "position:fixed;left:0px;right:0px;bottom:0px;z-index:1000")
        o.add( Tag.H.button(_class="delete", _onclick=jsclose) )
        o.add( content )

        self("""setTimeout(function() {%s;},%s);""" % (jsclose,delay))

        self <= o

    def close(self):
        self.clear()


if __name__=="__main__":

    # not really interactive in this test, so I need to put this
    # and not produce JS (close timeout)
    Toaster.__call__ = lambda x,y:x

    obj=Tag( )
    Toaster(obj).show( Box("Hello") )

    from .. import _test
    _test( obj )

# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

from htag import Tag

class Clipboard(Tag):
    tag="div"
    def __init__(self,parent):
        """ auto attach parent """
        super().__init__()
        parent <= self

    def copy(self,txt):
        assert "`" not in txt # ;-)
        self("""
let ta = document.createElement('textarea');
ta.value = `%s`;
tag.appendChild(ta);
ta.select();
document.execCommand('copy');
tag.removeChild(ta);
""" % txt)

if __name__=="__main__":
    from htag.runners import PyWebWiew,BrowserHTTP

    class Obj(Tag):
        def __init__(self):
            super().__init__()
            self.cc = Clipboard(self)
            self<= Tag.H.button( "Copy", _onclick=self.bind.copy())

        def copy(self):
            self.cc.copy("backend text to copy in clipboard")

    BrowserHTTP( Obj() ).run()

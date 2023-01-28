# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

from htag import Tag

class Clipboard(Tag.div):
    tag="div"
    def __init__(self,parent):
        """ auto attach parent """
        print("**DEPRECATED** don't use Clipboard, use the new Service !")
        super().__init__()
        parent <= self

    def copy(self,txt):
        assert "`" not in txt # ;-)
        self.call("""
let ta = document.createElement('textarea');
ta.value = `%s`;
self.appendChild(ta);
ta.select();
document.execCommand('copy');
self.removeChild(ta);
""" % txt)

if __name__=="__main__":
    from htag.runners import PyWebWiew,BrowserHTTP

    class Obj(Tag.div):
        def __init__(self):
            super().__init__()
            self.cc = Clipboard(self)
            self<= Tag.button( "Copy", _onclick=self.bind.copy())

        def copy(self):
            self.cc.copy("backend text to copy in clipboard")

    BrowserHTTP( Obj() ).run()

# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

from htag import Tag
import os

#TODO: perhaps a security limiter ;-) ?

class FileSelect(Tag.div):
    statics=[Tag.H.style("""
.FileSelect div:hover {background: #eee;cursor:pointer;}
""")]
    def __init__(self,path,onselect,**a):
        Tag.__init__(self,**a)
        self["class"]="FileSelect"
        self.onselect=onselect

        self._render(path)

    def _render(self,path):
        self.clear()
        self.path = os.path.realpath(path)
        folders=[]
        files=[]
        for i in os.listdir(self.path):
            if os.path.isdir( os.path.join(self.path,i) ):
                folders.append(i)
            else:
                files.append(i)

        if os.path.dirname(self.path)!=self.path:
            self<= Tag.H.div( "📁 ..", _onclick=self.bind._selectFolder(".."))
        for i in sorted(folders):
            self<= Tag.H.div( "📁 "+i, _onclick=self.bind._selectFolder(i))
        for i in sorted(files):
            self<= Tag.H.div(i, _onclick=self.bind._selectFile(i))

    def _selectFolder(self,i):
        self._render( os.path.join(self.path,i) )
    def _selectFile(self,i):
        path = os.path.join(self.path,i)
        self.onselect(path)

if __name__=="__main__":
    def showFile(name):
        print(name)

    obj=FileSelect( r".", showFile )

    from . import _test
    _test( obj )

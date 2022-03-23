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

#TODO: permit binary files too !

class FileUpload(Tag.input):
    """ only text file """
    statics=[Tag.H.script("""
function fileupload( self, cbInteract ) {
    let file = self.files[0];
    var reader = new FileReader();
    reader.onload =  e => { cbInteract(file.name, e.target.result) };
    reader.readAsText(file);     //reader.readAsBinaryString(file);
}""")]

    def __init__(self,onchange,**a):
        Tag.__init__(self,**a)
        self["type"]="file"
        self["onchange"]="fileupload(this, function(name,content) {%s})" % self.bind._onchange( b"name",b"content")
        self.onchange=onchange

    def _onchange(self,name,content):
        self.onchange(name,content)

if __name__=="__main__":
    def showFile(name,content):
        print(name,content)

    obj=FileUpload( showFile )

    from . import _test
    _test( "only txt file",obj )

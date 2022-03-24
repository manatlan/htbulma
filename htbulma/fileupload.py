# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

from htag import Tag
import os,base64


class FileUpload(Tag.input):
    statics=[Tag.H.script(r"""
function fileupload( self, cbInteract ) {
    let file = self.files[0];
    var reader = new FileReader();
    reader.onload =  e => { cbInteract(file.name, btoa(e.target.result)) };
    reader.readAsBinaryString(file); //reader.readAsText(file);
}""")]

    def __init__(self,onchange,**a):
        Tag.__init__(self,**a)
        self["type"]="file"
        self["onchange"]="fileupload(this, function(name,content) {%s})" % self.bind._onchange( b"name", b"content")
        self.onchange=onchange

    def _onchange(self,name:str,content:str):
        self.onchange(name,base64.b64decode(content))

if __name__=="__main__":
    def showFile(name: str,content: bytes):
        print(name,content)

    obj=FileUpload( showFile )

    from . import _test
    _test( "TRANSFERT AS BINARY STRING",obj )

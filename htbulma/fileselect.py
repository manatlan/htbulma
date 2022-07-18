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
import fnmatch


class FileSelect(Tag.div):
    statics="""
.FileSelect {
    white-space: nowrap;
}
.FileSelect div:hover {
    background: #eee;cursor:pointer;
}
.FileSelect div.selected {
    background:#DDD;
}
""",b"""

function FileSelect_select(id) {
    document.querySelectorAll('div.FileSelect div').forEach(div => {
      div.classList.remove('selected');
    });
    document.getElementById(id).classList.add('selected');
}

"""
    def init(self,path,onselect,pattern="*"):
        self["class"].add("FileSelect")
        self.onselect=onselect

        self._patterns = [pattern] if isinstance(pattern,str) else pattern
        self._root = os.path.realpath(path)
        self._selected = None
        self._render(path)

    def refresh(self):
        self._render(self.path)

    def _render(self,path):
        self.clear()
        self.path = os.path.realpath(path)
        assert self.path.startswith(self._root) # security
        folders=[]
        files=[]
        for i in os.listdir(self.path):
            if os.path.isdir( os.path.join(self.path,i) ):
                folders.append(i)
            else:
                files.append(i)

        if os.path.dirname(self.path).startswith(self._root):
            self<= Tag.div( Tag.b( "&#11013; "+ path[len(self._root)+1:]),path=".." , _onclick=self._selectFolder)
        for i in sorted(folders):
            self<= Tag.div( "📁 "+i, path=i, _onclick=self._selectFolder)
        for i in sorted(files):
            if any( [fnmatch.fnmatch(i, p) for p in self._patterns] ):
                self<= Tag.div(i, path=i, _onclick=self._selectFile, _class="selected" if i==self._selected else "")

    def _selectFolder(self,o):
        self._render( os.path.realpath(os.path.join(self.path,o.path)) )
    def _selectFile(self,o):
        path = os.path.realpath(os.path.join(self.path,o.path))
        assert path.startswith(self._root)
        self._selected = o.path
        self(f"""FileSelect_select('{id(o)}')""")
        self.onselect(path)

if __name__=="__main__":
    def showFile(name):
        print(name)

    obj=FileSelect( r".", showFile )

    from . import _test
    _test( obj )

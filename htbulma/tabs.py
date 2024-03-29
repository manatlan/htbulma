# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from . import TagBulma,TabsHeader

class Tabs(TagBulma): # New version (NOT htag optimized ;-()

    imports = TabsHeader

    def __init__(self,**a):
        super().__init__(**a)
        self.__tabs={}
        self.__selected = None

    def addTab(self,name,content):
        self.__tabs[name] = content
        if self.__selected is None:
            self.__selected=name
        self._render()

    def _render(self):
        self.clear()

        ll=[]
        for k,v in self.__tabs.items():
            ll.append(k)

        if self.__selected:
            if len(ll)>0:
                self <= TabsHeader(self.__selected, ll, _onchange= self._setselected )
                try: # to be compatible with htag>0.8.9
                    #TODO: remove when new htag is widely deployed
                    self.add( self.__tabs[ self.__selected ], True) # reparenting
                except:
                    self.add( self.__tabs[ self.__selected ] )

    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, v):
        self.__selected =v
        self._render()

    def _setselected(self,obj):
        self.__selected = obj.value
        self._render()

if __name__=="__main__":

    obj=Tabs()
    obj.addTab("P1", "I'm the page1")
    obj.addTab("P2", "Currently, I am the page2 !")

    from . import _test
    _test( obj )


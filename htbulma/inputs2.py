# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from htag import Tag
import ast,json
# from htag.tag import Caller
# import json,html
from htbulma import TagBulma, Form

from typing import Union

ListOrDict = Union[ list, dict]



#########################################################################################################################
## Common helpers
#########################################################################################################################

class Options:

    def __init__(self,options:ListOrDict):
        if isinstance(options,list):
            self._options = {i:i for i in options}
        elif isinstance(options,dict):
            self._options = dict(options)
        else:
            self._options={}

    def fix_value_if_options(self,value): #TODO: dont work for float,bool,.. (only int/str) ;-(
        if self._options:
            if isinstance(value, str) and value.isnumeric() and int(value) in self._options.keys():
                return int(value)
        return value


class NewInput:

    _value=None
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        # and draw
        self._redraw()

    def _redraw(self):
        pass

    
#########################################################################################################################
## Generics (not bulma related)
#########################################################################################################################

class Input(Tag.input,Options,NewInput):
    statics= """.disabled {pointer-events:none;cursor: not-allowed;opacity:0.5}"""

    """
    a.keys() can be :
        _type : date,email,color,file etc ...
        _required
        _readonly
        _disabled
        _style
        _class
        _placeholder
        ...
    """

    def __init__(self, value, options:ListOrDict=[], name=None, **a):
        Options.__init__(self,options)
        super().__init__(**a)
        self.value=value  # store the real value in a property value

        self["class"].add("input")
        self["onchange"] = self.bind( self._set, b"this.value" ).bind( a.get("_onchange",None) )    # assign an event to reflect change

        if name: self["name"]=name

        if self._options:
            self["type"]="search"
            datalist = Tag.datalist( [Tag.H.option(v,_value=k) for k,v in self._options.items()] )
            self <= datalist
            self["list"] = id(datalist)

    def _redraw(self):
        self["value"]=self._value

    def _set(self,value:str): # when changed, keep the property value up-to-date
        self._value = self.fix_value_if_options(value)


class Select(Tag.select,Options,NewInput):

    def __init__(self, value, options:ListOrDict,name=None,**a):
        Options.__init__(self,options)
        super().__init__(**a)

        self["class"].add("select")
        self["onchange"] = self.bind( self._set, b"this.value").bind( a.get("_onchange",None) )

        if name: self["name"]=name

        if self["readonly"] or self["disabled"]:
            self["class"].add("disabled")

        self.value = value  # redraw

    def _redraw(self):
        self["value"]=self._value
        self.clear()
        if self._options:
            for k,v in self._options.items():
                self <= Tag.H.option( v, _value=k, _selected = (self._value == k) )

    def _set(self,value:str):
        self._value  = self.fix_value_if_options(value)


class Checkbox(Tag.input,NewInput):

    #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ overrides !
    #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = bool(value)
        # and draw
        """
        **WARNING TRICK ***********************************************************************************
        returning "<input><label>xxx</label></input>" will produce "<input/> <label>xxx</label>" in dom
        so labels will stack, at each change ;-(
        ===> the self.clear() avoid that !!!!!!!!!!!!!!!
        **WARNING TRICK ***********************************************************************************
        """
        self.clear()
        self["checked"]=self._value
    #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    #/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

    def __init__(self, value:bool, label=None, name=None,**a):
        super().__init__(**a)
        self.value = value  # !important here

        self["class"].add("checkbox")
        self["type"]="checkbox"
        self["onchange"] = self.bind( self._set, b"this.checked").bind( a.get("_onchange",None) )

        if self["readonly"] or self["disabled"]:
            self["class"].add("disabled")

        if name: self["name"]=name

        if label:
            self <= Tag.label(label,_for=str(id(self)),_class="disabled" if self["readonly"] or self["disabled"] else "")

    def _set(self,value:str):
        self._value = value in ["true","on","yes",True,1]


class Range(Tag.input,NewInput):

    def __init__(self, value, name=None,**a):
        super().__init__(**a)

        self["type"]="range"
        self["class"].add("control")
        if name: self["name"]=name

        if self["readonly"]:
            self["class"].add("disabled")

        self["onchange"] = self.bind( self._set, b"this.value" ).bind( a.get("_onchange",None) )

        self.value = value

    def _redraw(self):
        self["value"]=self._value

    def _set(self,value):
        self._value = ast.literal_eval(value)


class Textarea(Tag.textarea,NewInput):

    def __init__(self, value:str, name=None,**a):
        super().__init__(**a)

        self["class"].add("textarea")
        self["onchange"] = self.bind( self._set, b"this.value" ).bind( a.get("_onchange",None) )    # assign an event to reflect change

        if self["readonly"]:
            self["class"].add("disabled")

        if name: self["name"]=name
        self.value = value

    def _redraw(self):
        self.set( self._value )

    def _set(self,value:str):
        self._value = value


class Radio(Tag.span,Options,NewInput):

    def __init__(self, value, options:ListOrDict, name=None,**a):
        Options.__init__(self,options)
        super().__init__(**a)

        self["class"].add("control")
        self["onchange"] = self.bind( a.get("_onchange",lambda o:None) )   # TODO: evol htag ?! bcoz 2 interactions

        if self["readonly"] or self["disabled"]:
            self._disabled=True
            self["class"].add("disabled")
        else:
            self._disabled=False

        self._default_name = name or ("r%s" % id(self))

        self.value=value    # redraw

    def _redraw(self):
        self.clear()
        if self._options:
            for k,v in self._options.items():
                i=Tag.input(_type="radio", _value=k, _checked = (self._value==k), _name = self._default_name,_disabled=self._disabled )
                i["onchange"] = self.bind( self._set, b"this.value" )
                self <= Tag.H.label( [i," ",v], _class="radio" )


    def _set(self,value):
        self._value = self.fix_value_if_options(value)

#########################################################################################################################
## Bulma specifics
#########################################################################################################################

class SelectButtons(Tag.div,Options,NewInput):
    _bstyle_ = "is-toggle is-small"

    def __init__(self, value, options:ListOrDict, name=None,**a):
        Options.__init__(self,options)
        super().__init__(**a)

        self["class"].add("tabs",self._bstyle_)
        self["onchange"] = self.bind( a.get("_onchange",lambda o:None) )   # TODO: evol htag ?! bcoz 2 interactions

        self.input = Tag.input(_name=name,_type="hidden",_value=self._value, **a)
        self.u = Tag.H.ul()

        self<= self.input + self.u

        self.value=value

    def _redraw(self):
        self.input["value"]=self._value
        self.u.clear()
        if self["disabled"] or self["readonly"]:
            self.u["class"].add("disabled")

        for k,v in self._options.items():
            isActive = "is-active" if self._value == k else ""
            if self["disabled"]:
                self.u<=Tag.H.li(Tag.H.a(v,_disabled=True), _class=isActive, _disabled=True)
            else:
                self.u<=Tag.H.li(Tag.a(v, _onclick=self.bind(  self._set, k )), _class=isActive)

    def _set(self,value):
        self._value = self.fix_value_if_options(value)
        self( self["onchange"] )
        self._redraw()

class TabsHeader(SelectButtons):
    _bstyle_="is-centered" # "is-boxed is-centered"


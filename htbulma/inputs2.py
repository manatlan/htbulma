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


"""
new inputs (**WORK IN PROGRESS**)

 - every widget make an interaction to set its ".value" after each change !
 - REAL "_onchange" : every widget can re-bind/chain the default onchange (with attrs or in init)
 - every widget doesn't redraw itself on change (except radio, selectbuttons & tabheaders; by nature)
 - clever (more self tag based !!!)
 - each widget got self.value dynamic ! (setting it, force redraw)

AND HTAG.BIND.PRIOR will disappear !!!! (non sense, now)
"""

#########################################################################################################################
## Common helpers
#########################################################################################################################

class Options:

    def make_options(self,options):
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

#########################################################################################################################
## Generics (not bulma related)
#########################################################################################################################

class Input(Tag.input,Options):
    """
    **a can be :
        _type : date,email,color,file etc ...
        _required
        _readonly
        _disabled
        _style
        _class
        _placeholder
    """
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        # and draw
        self["value"]=self._value

    def __init__(self, value, options:list=[], name=None, **a):
        super().__init__(**a)
        self.value=value  # store the real value in a property value

        self["class"].add("input")
        self["onchange"] = self.bind( self._set, b"this.value" ).bind( a.get("_onchange",None) )    # assign an event to reflect change

        if name: self["name"]=name

        self.make_options(options)
        if self._options:
            self["type"]="search"
            datalist = Tag.datalist( [Tag.H.option(v,_value=k) for k,v in self._options.items()] )
            self <= datalist
            self["list"] = id(datalist)

    def _set(self,value:str): # when changed, keep the property value up-to-date
        self._value = self.fix_value_if_options(value)


class Select(Tag.select,Options):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        # and draw
        self["value"]=self._value
        self._redraw()

    def __init__(self, value, options:list,name=None,**a):
        super().__init__(**a)

        self["class"].add("select")
        self["onchange"] = self.bind( self._set, b"this.value").bind( a.get("_onchange",None) )

        if name: self["name"]=name

        self.make_options(options)
        self.value = value  # redraw

    def _redraw(self):
        self.clear()
        if self._options:
            for k,v in self._options.items():
                self <= Tag.H.option( v, _value=k, _selected = (self._value == k) )

    def _set(self,value:str):
        self._value  = self.fix_value_if_options(value)

class Checkbox(Tag.input):

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

    def __init__(self, value:bool, label=None, name=None,**a):
        super().__init__(**a)
        self.value = value

        self["class"].add("checkbox")
        self["type"]="checkbox"
        self["onchange"] = self.bind( self._set, b"this.checked").bind( a.get("_onchange",None) )

        if name: self["name"]=name

        if label:
            self <= Tag.label(label,_for=str(id(self)))

    def _set(self,value:str):
        self._value = value in ["true","on","yes",True,1]

class Range(Tag.input):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        # and draw
        self["value"]=self._value

    def __init__(self, value, name=None,**a):
        super().__init__(**a)
        self.value = value

        self["type"]="range"
        self["class"].add("control")
        if name: self["name"]=name

        self["onchange"] = self.bind( self._set, b"this.value" ).bind( a.get("_onchange",None) )

    def _set(self,value):
        self._value = ast.literal_eval(value)


class Textarea(Tag.Textarea):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        # and draw
        self.set( self._value )

    def __init__(self, value:str, name=None,**a):
        super().__init__(**a)
        self.value = value

        self["class"].add("textarea")
        self["onchange"] = self.bind( self._set, b"this.value" ).bind( a.get("_onchange",None) )    # assign an event to reflect change

        if name: self["name"]=name

    def _set(self,value:str):
        self._value = value


class Radio(Tag.span,Options):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        # and draw
        self._redraw()

    def __init__(self, value, options:list, name=None,**a):
        super().__init__(**a)

        self["class"].add("control")
        self["onchange"] = self.bind( a.get("_onchange",lambda o:None) )   # TODO: evol htag ?! bcoz 2 interactions

        self._default_name = name or ("r%s" % id(self))

        self.make_options(options)
        self.value=value    # redraw

    def _redraw(self):
        self.clear()
        if self._options:
            for k,v in self._options.items():
                i=Tag.input(_type="radio", _value=k, _checked = (self._value==k), _name = self._default_name )
                i["onchange"] = self.bind( self._set, b"this.value" )
                self <= Tag.H.label( [i," ",v], _class="radio" )


    def _set(self,value):
        self._value = self.fix_value_if_options(value)

#########################################################################################################################
## Bulma specifics
#########################################################################################################################

class SelectButtons(Tag.div,Options):
    _bstyle_ = "is-toggle is-small"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        # and draw
        self.input["value"]=self._value
        self._render()

    def __init__(self, value, options:list, name=None,**a):
        super().__init__(**a)

        self._value=value
        self._options=options
        self._children=[]

        self["class"].add("tabs",self._bstyle_)
        self["onchange"] = self.bind( a.get("_onchange",lambda o:None) )   # TODO: evol htag ?! bcoz 2 interactions

        self.make_options(options)

        self.input = Tag.input(_name=name,_type="hidden",_value=self._value, **a)
        self.u = Tag.H.ul()

        self<= self.input + self.u

        self._render()


    def _render(self):
        self.u.clear()
        if self["disabled"] or self["readonly"]:
            self.u["style"]="pointer-events: none;"

        for k,v in self._options.items():
            isActive = "is-active" if self._value == k else ""
            if self["disabled"]:
                self.u<=Tag.H.li(Tag.H.a(v,_disabled=True), _class=isActive, _disabled=True)
            else:
                self.u<=Tag.H.li(Tag.a(v, _onclick=self.bind(  self._set, k )), _class=isActive)

    def _set(self,value):
        self._value = self.fix_value_if_options(value)
        self( self["onchange"] )
        self._render()

class TabsHeader(SelectButtons):
    _bstyle_="is-centered" # "is-boxed is-centered"

##############################################################################
##############################################################################
##############################################################################

from htag.runners import DevApp

class Test(Tag.body):
    def init(self):
        self.cb_disabled= Checkbox(False,"disabled",_onchange = self._render)
        self.cb_readonly= Checkbox(False,"readonly", _onchange = self._render)
        self.cb_required= Checkbox(False,"required", _onchange = self._render)

        self.main = Form(onsubmit=self.formSubmit)

        # build layout
        self <= self.cb_disabled + self.cb_readonly + self.cb_required
        self <= Tag.button("Show current contents",_onclick=self.show)
        self <= Tag.button("Set all to 1",_onclick=self.bind(self.setall,1))
        self <= Tag.button("Set all to 0",_onclick=self.bind(self.setall,0))
        self <= Tag.hr()
        self <= self.main

        self._render()

    def _render(self,o=None):
        commons={}
        commons["_disabled"]=self.cb_disabled._value
        commons["_readonly"]=self.cb_readonly._value
        commons["_required"]=self.cb_required._value

        self.main.clear()
        LIST = [0,1,12,13,14]
        DICT={0:"zero",1:"one","a":"aa","b":"bb"}
        self.main <= Input(12,name="input_simple",**commons)
        self.main <= Input(12,LIST,name="input_list",**commons)
        self.main <= Input("a",DICT,name="input_dict",**commons)
        self.main <= Checkbox(True,name="cb_simple",**commons)
        self.main <= Checkbox(True,"Checked",name="cb_true",**commons)
        self.main <= Checkbox(False,"Not-Checked",name="cb_false",**commons)
        self.main <= Select(12,LIST,name="select_list",**commons)
        self.main <= Select("a",DICT,name="select_dict",**commons)
        self.main <= SelectButtons(12,LIST,name="selectb_list",**commons)
        self.main <= SelectButtons("a",DICT,name="selectb_dict",**commons)
        self.main <= TabsHeader(12,LIST,name="tabsheader_list",**commons)
        self.main <= TabsHeader("a",DICT,name="tabsheader_dict",**commons)
        self.main <= Textarea("hello",name="textarea")
        self.main <= Radio(12,LIST,name="rb_list",**commons)
        self.main <= Radio("a",DICT,name="rb_dict",**commons)
        self.main <= Range(10,_min=0, _max=100, name="range",**commons)

        self.main <= Tag.button("Test the form post way",_class="button")

        for i in self.main.childs:
            if i.tag!="button":
                i["onchange"].bind( self.react ) # chain on the default event !

    def setall(self, v):
        print("Set all values to",v)
        for obj in self.main.childs:
            if obj.tag!="button":
                obj.value=v

    def show(self, o):
        for obj in self.main.childs:
            if obj.tag!="button":
                self.react(obj)

    def react(self, o ):
        txt="- %s id=%s, value = %s (type:%s)" %( o.__class__.__name__, id(o), o.value, str(type(o.value)) )
        print(txt)

    def formSubmit(self, f:dict):
        print( json.dumps(f,indent=4) )

app=DevApp(Test)
if __name__=="__main__":
    app.run()
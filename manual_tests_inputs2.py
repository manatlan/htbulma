# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

from htag import Tag
from htbulma import Form
from htbulma.inputs2 import Checkbox,Input,Select,SelectButtons,TabsHeader,Textarea,Range,Radio,NewInput
from htag.runners import DevApp
import json

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
        commons["_disabled"]=self.cb_disabled.value
        commons["_readonly"]=self.cb_readonly.value
        commons["_required"]=self.cb_required.value

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
        self.main <= Textarea("hello",name="textarea",**commons)
        self.main <= Radio(12,LIST,name="rb_list",**commons)
        self.main <= Radio("a",DICT,name="rb_dict",**commons)
        self.main <= Range(10,_min=0, _max=100, name="range",**commons)

        self.main <= Tag.button("Test the form post way",_class="button")

        for i in self.main.childs:
            if issubclass(i.__class__,NewInput):
                i["onchange"].bind( self.react ) # chain on the default event !

    def setall(self, v):
        print("Set all values to",v)
        for obj in self.main.childs:
            if issubclass(obj.__class__,NewInput):
                obj.value=v

    def show(self, o):
        for obj in self.main.childs:
            if issubclass(obj.__class__,NewInput):
                self.react(obj)

    def react(self, o ):
        txt="- %s id=%s, value = %s (type:%s)" %( o.__class__.__name__, id(o), o.value, str(type(o.value)) )
        print(txt)

    def formSubmit(self, f:dict):
        print( json.dumps(f,indent=4) )
App = Test

app=DevApp(Test)
if __name__=="__main__":
    app.run()
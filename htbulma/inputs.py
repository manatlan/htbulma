# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from . import TagBulma, Box, Fields, HBox, Form, Content
from htag import Tag
from htag.tag import Caller
import json,html


class SelfProperties:
    # _callback=None

    def onchange(self,callback):
        if not isinstance( callback, Caller):
            callback = self.bind( callback )
        callback = callback.prior( self.setValue, b"this.value" )

        self["onchange"] = callback
        # self._callback = callback
        return self

    def setValue(self,value):
        self["value"] = value
        self.value = value
        # if self._callback: self._callback( self )



    def _fixValue(self,value): #TODO: dont work for float,bool,.. (only int/str) ;-(
        if isinstance(self._options,list):
            if isinstance(value, str) and value.isnumeric() and int(value) in self._options:
                return int(value)
        elif isinstance(self._options,dict):
            if isinstance(value, str) and value.isnumeric() and int(value) in self._options.keys():
                return int(value)
        return value

class Input(Tag.input, SelfProperties, TagBulma):
    def __init__(self, value, options:list=[], name=None, onchange=None,**a):
        super().__init__(**a)
        self.classEnsure("input")

        if name: self["name"]=name

        self["value"] = value
        self.value = value
        self._options = options
        if isinstance(options,list) and options:
            datalist = Tag.datalist( [Tag.H.option(_value=j) for j in options] )
            self <= datalist
            self["list"] = id(datalist)
        elif isinstance(options,dict) and options:
            datalist = Tag.datalist( [Tag.H.option(v,_value=k) for k,v in options.items()] )
            self <= datalist
            self["list"] = id(datalist)

        if onchange:
            self.onchange( onchange )


    def setValue(self,value): # override
        # fix value type, using options
        value = self._fixValue(value)

        self["value"] = value
        self.value = value


class Range(Tag.div):
    def __init__(self, value, name=None,onchange=None,**a):
        super().__init__(**a)
        self["class"]="control"
        self["value"] = value
        self.value = value

        if "_class" in a: del a["_class"]
        if "_style" in a: del a["_style"]

        if self["readonly"]:
            a["_style"]="flex: 1 0 auto;pointer-events: none;"
        else:
            a["_style"]="flex: 1 0 auto;"

        self.input= Tag.input(_name=name,_type="range",_oninput="this.previousElementSibling.value = this.value", _value=value,**a)
        if not self["style"]: self["style"]=""
        self["style"]+=";display: flex; flex-flow: row nowrap;"
        self <= Tag.H.output(str(value),_style="flex: 0 0 auto;padding:4px;")
        self <= self.input

        if onchange:
            self.onchange( onchange )


    #|||||||||||||||||||||||||||||||||
    def onchange(self,callback):
        if not isinstance( callback, Caller):
            callback = self.bind( callback )
        callback = callback.prior( self.setValue, b"this.value" )


        self.input["onchange"] = callback
        return self

    def setValue(self,value):
        self.value = int(value)
    #|||||||||||||||||||||||||||||||||

class Checkbox(Tag.label, TagBulma):
    def __init__(self, value:bool, label:str, name=None,onchange=None,**a):
        super().__init__(**a)
        self.classEnsure("checkbox")

        if self["readonly"]:
            if not self["style"]: self["style"]=""
            self["style"]+=";pointer-events: none;"


        self.value = bool(value)
        self._callback=None

        if "_class" in a: del a["_class"]
        if "_style" in a: del a["_style"]

        self.input=Tag.input(_name=name,_type="checkbox", _checked = value, **a)

        self <= self.input + " " + label

        if onchange:
            self.onchange( onchange )

    #|||||||||||||||||||||||||||||||||
    def onchange(self,callback):
        if not isinstance( callback, Caller):
            callback = self.bind( callback )
        callback = callback.prior( self.setValue, b"this.checked" )

        self.input["onchange"] = callback
        return self

    def setValue(self,value):
        self.value = value in ["true","on","yes",True,1]
    #|||||||||||||||||||||||||||||||||



class Radio(Tag.div, SelfProperties, TagBulma):
    def __init__(self, value, options:list, name=None,onchange=None,**a):
        super().__init__(**a)
        self.value=value
        self.classEnsure("control")
        default_name = name or ("r%s" % id(self))
        self._options=options
        self._children=[]

        if "_class" in a: del a["_class"]
        if "_style" in a: del a["_style"]

        if self["readonly"]:
            if not self["style"]: self["style"]=""
            self["style"]+=";pointer-events: none;"

        if isinstance(options,list):
            for j in options:
                i=Tag.input(_type="radio", _value=j, _checked = (value==j), _name = default_name, **a)
                self._children.append(i)
                self <= Tag.H.label( [i," ",j], _class="radio" )
        elif isinstance(options,dict):
            for k,v in options.items():
                i=Tag.input(_type="radio", _value=k, _checked = (value==k), _name = default_name, **a)
                self._children.append(i)
                self <= Tag.H.label( [i," ",v], _class="radio" )

        if onchange:
            self.onchange( onchange )


    #|||||||||||||||||||||||||||||||||
    def onchange(self,callback): # override

        if not isinstance( callback, Caller):
            callback = self.bind( callback )
        callback = callback.prior( self.setValue, b"this.value" )

        for i in self._children:
            i["onchange"] = callback
        return self

    def setValue(self,value):   # override
        # fix value type, using options
        value = self._fixValue(value) #(only reason to use SelfProperties)

        self.value = value
    #|||||||||||||||||||||||||||||||||



class SelectButtons(Tag.div, TagBulma):
    _bstyle_ = "is-toggle is-small"
    def __init__(self, value, options:list, name=None,onchange=None,**a):
        super().__init__(**a)
        self.value=value
        self._options=options
        self._children=[]

        self.classEnsure("tabs "+self._bstyle_)

        self.input = Tag.input(_name=name,_type="hidden",_value=self.value, **a)
        self.u = Tag.H.ul()

        self<= self.input + self.u

        self._callback = onchange
        self._render()


    def _render(self):
        self.u.clear()
        if self["disabled"] or self["readonly"]:
            self.u["style"]="pointer-events: none;"

        if isinstance(self._options,list):
            options=[ (j,j) for j in self._options]
        elif isinstance(self._options,dict):
            options=self._options.items()
        else:
            options=[]

        for k,v in options:
            isActive = "is-active" if self.value == k else ""
            if self["disabled"]:
                self.u<=Tag.H.li(Tag.H.a(v,_disabled=True), _class=isActive, _disabled=True)
            else:
                if self._callback:
                    if not isinstance( self._callback, Caller):
                        callback = self.bind( self._callback )
                    else:
                        callback = self._callback # !!!!?
                    callback = callback.prior( self.setValue, k )
                else:
                    callback = self.bind(  self.setValue, k )

                self.u<=Tag.H.li(Tag.a(v, _onclick=callback), _class=isActive)



    #|||||||||||||||||||||||||||||||||
    def onchange(self,callback):
        raise Exception("Don't use it, use the onchange attr at constructor !")

    def setValue(self,value):   # force re-render
        self.value = value
        self.input["value"] = value
        self._render()
    #|||||||||||||||||||||||||||||||||

class TabsHeader(SelectButtons):
    _bstyle_="is-centered" # "is-boxed is-centered"


class Select(Tag.div, SelfProperties, TagBulma):
    def __init__(self, value, options:list,name=None,onchange=None,**a):
        super().__init__(**a)
        self.classEnsure("select")

        self.value = value
        self._options = options
        if name: self["name"]=name

        if "_class" in a: del a["_class"]
        if "_style" in a: del a["_style"]

        if self["readonly"]:
            a["_style"]="width:100%;pointer-events: none;"
        else:
            a["_style"]="width:100%;"

        self.input = Tag.select(_name=name,**a)

        if isinstance(options,list):
            for j in options:
                self.input <= Tag.H.option( j, _selected = (value == j) )
        elif isinstance(options,dict):
            for k,v in options.items():
                self.input <= Tag.H.option( v, _value=k, _selected = (value == k) )

        self <= self.input

        if onchange:
            self.onchange( onchange )


    #|||||||||||||||||||||||||||||||||
    def onchange(self,callback):
        if not isinstance( callback, Caller):
            callback = self.bind( callback )
        callback = callback.prior( self.setValue, b"this.value" )

        self.input["onchange"] = callback
        return self

    def setValue(self,value):
        value = self._fixValue(value)
        self.value = value
    #|||||||||||||||||||||||||||||||||


class Textarea(Tag.Textarea, SelfProperties, TagBulma):
    def __init__(self, value:str, name=None,onchange=None,**a):
        super().__init__(value,**a)
        if name: self["name"]=name
        self.classEnsure("textarea")
        self.value = value

        if onchange:
            self.onchange( onchange )


    def setValue(self,value):   #OVERRIDE
        self.value = value
        self.set(value)



##############################################################################
##############################################################################
##############################################################################

if __name__=="__main__":

    LIST=[1,2,3]
    DICT = dict(A="Albert",B="Bonnie",C="Clyde")

    class Page(Tag.div):
        statics = [Tag.H.style(""".myclass {border: 1px solid blue !important;background:#AFA !important}""")]
        def __init__(self):
            super().__init__()

            self.modders = SelectButtons(0,{0:"normal",4:"all required",5:"all readonly", 1:"all disabled",2:"style",3:"class"}, onchange= self.redraw )

            self.tab = TabsHeader(0,{0:"Via Form",1:"Reactive",2:"Inside Fields"}, onchange= self.redraw )
            self.visu = Tag.div()
            self.pre = Tag.pre()

            self <= self.modders
            self <= self.tab
            self <= self.visu
            self <= self.pre

            self.redraw( None )

        def redraw(self, notUsed ):
            if self.modders.value ==1:
                commons={"_disabled": True}
            elif self.modders.value ==4:
                commons={"_required": True}
            elif self.modders.value ==5:
                commons={"_readonly": True}
            elif self.modders.value ==2:
                commons={"_style": "border: 1px solid red !important;background:yellow !important"}
            elif self.modders.value ==3:
                commons={"_class": "myclass"}
            else:
                commons={}

            print("COMMONS:",commons)

            if self.tab.value==0:
                #====================================================
                # FORM
                #====================================================
                f=Form(onsubmit=self.formSubmit)
                f<= Content("All inputs are sent thru a 'form' via the submit button below")
                f<=Textarea("hello", name="mytext", **commons)
                f<= HBox(
                    Input(2,name="myinput1",**commons),
                    Input(None,LIST,name="myinput2",**commons),
                    Input(None,DICT,name="myinput3",**commons),
                )
                f<= HBox(
                    Input("",name="date",_type="date",**commons),
                    Input("",name="month",_type="month",**commons),
                    Input("",name="time",_type="time",**commons),
                    Input("",name="pass",_type="password",**commons),
                    Input("",name="color",_type="color",**commons),
                    Input("",name="file",_type="file",**commons), # non sense, in a form
                )

                f<= HBox(
                    Radio(2,LIST,name="myradio1",**commons),
                    Radio("B",DICT,name="myradio2",**commons),
                )

                f<= HBox(
                    SelectButtons(2,LIST,name="mysb1",**commons),
                    SelectButtons("B",DICT,name="mysb2",**commons),
                )

                f<= HBox(
                    Select(2,LIST,name="myselect1",**commons),
                    Select("B",DICT,name="myselect2",**commons),
                )

                f<= HBox(
                    Checkbox(True,"homme",name="mycb1",**commons),
                    Checkbox(False,"femme",name="mycb1",**commons),
                )

                f<= Range(12, name="myrange", _min=10, _max=78, _step=2, **commons)

                f<= Tag.button("ok",_class="button")

                self.pre.set( "^^ Use the SUBMIT BUTTON ^^" )
            elif self.tab.value==1:
                #====================================================
                # Reactive
                #====================================================
                f=Tag.div()
                f<= Content("All inputs are reactive and sent itself to the react() method")
                f<= Textarea("hello",onchange= self.react,**commons)
                f<= HBox(
                    Input(2,onchange= self.react,**commons),
                    Input(None,LIST,onchange= self.react,**commons),
                    Input(None,DICT,onchange= self.react,**commons),
                )

                f<= HBox(
                    Input("",_type="date",onchange= self.react, **commons),
                    Input("",_type="month",onchange= self.react,**commons),
                    Input("",_type="time",onchange= self.react,**commons),
                    Input("",_type="password",onchange= self.react,**commons),
                    Input("",_type="color",onchange= self.react,**commons),
                    Input("",_type="file",onchange= self.react,**commons),    # not a great sense, either !
                )


                f<= HBox(
                    Radio(2,LIST,onchange= self.react,**commons),
                    Radio("B",DICT,onchange= self.react,**commons),
                )

                f<= HBox(
                    SelectButtons(2,LIST, onchange = self.react,**commons),
                    SelectButtons("B",DICT, onchange = self.react,**commons),
                )

                f<= HBox(
                    Select(2,LIST,onchange= self.react,**commons),
                    Select("B",DICT,onchange= self.react,**commons),
                )

                f<= HBox(
                    Checkbox(True,"homme",onchange= self.react,**commons),
                    Checkbox(False,"femme",onchange= self.react,**commons),
                )

                f<= Range(12, _min=10, _max=78, _step=2,onchange= self.react,**commons)

                self.pre.set( "Interact with an input ;-)" )
            else:
                #====================================================
                # just a fieldset/form (without interaction/submit)
                #====================================================
                f=Fields()
                f.addField("Name", Input("mamamam",**commons))
                f.addField("Surname", Input("kookokko",**commons), "not me ;-)")
                f.addField("Sex", Radio(1,LIST,**commons))
                f.addField("Other", [Select(1,DICT,**commons), Select(None,[None,1,2,3],**commons) ])
                f.addField("Address", Textarea("",_rows="2",**commons))
                f.addField("Size", Range(10,_min=0, _max=100, **commons))
                f.addField("Ok with that", Checkbox(False,"Sure?", **commons))

                self.pre.set( "Just a presentation thing ! (no interactions)" )

            #######################################################
            self.visu.set( Box(f) )

        def formSubmit(self, f:dict):
            self.pre.set( json.dumps(f,indent=4) )

        def react(self, obj ):
            self.pre.set( "class:%s id=%s, value = %s (type:%s)" %( obj.__class__.__name__, id(obj), obj.value, html.escape(str(type(obj.value))) ) )



    app=Page()



    from . import _test
    _test( app )

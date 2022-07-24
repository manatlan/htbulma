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


def warn(o,where):
    print(f"**WARNING** DEPRECATED remove '{where}()' for ",o.__class__.__name__)

from . import inputs2

class OldInputCompat:
    def __init__(self):
        pass
    def onchange(self,cb):
        warn(self,"onchange")
        self["onchange"].bind( cb )
    def setValue(self,value):
        warn(self,"setValue")
        self.value = value

class Input(inputs2.Input,OldInputCompat):
    def __init__(self, value, options:inputs2.ListOrDict=[], name=None, onchange=None,**a):
        super().__init__(value,options,name=name,_onchange=onchange, **a)
        OldInputCompat.__init__(self)


class Range(inputs2.Range,OldInputCompat):
    def __init__(self, value, name=None,onchange=None,**a):
        super().__init__(value,name=name,_onchange=onchange, **a)
        OldInputCompat.__init__(self)


class Checkbox(inputs2.Checkbox,OldInputCompat):
    def __init__(self, value:bool, label:str, name=None,onchange=None,**a):
        super().__init__(value,label=label,name=name,_onchange=onchange, **a)
        OldInputCompat.__init__(self)


class Radio(inputs2.Radio,OldInputCompat):
    def __init__(self, value, options:inputs2.ListOrDict, name=None,onchange=None,**a):
        super().__init__(value,options,name=name, **a)
        OldInputCompat.__init__(self)
        if onchange:
            self.onchange(onchange)


class Select(inputs2.Select,OldInputCompat):
    def __init__(self, value, options:inputs2.ListOrDict, name=None,onchange=None,**a):
        super().__init__(value,options,name=name,_onchange=onchange, **a)
        OldInputCompat.__init__(self)


class Textarea(inputs2.Textarea,OldInputCompat):
    def __init__(self, value:str, name=None,onchange=None,**a):
        super().__init__(value,name=name,_onchange=onchange, **a)
        OldInputCompat.__init__(self)


class SelectButtons(inputs2.SelectButtons,OldInputCompat):
    def __init__(self, value, options:inputs2.ListOrDict, name=None,onchange=None,**a):
        super().__init__(value,options,name=name, **a)
        OldInputCompat.__init__(self)
        if onchange:
            self.onchange(onchange)


class TabsHeader(SelectButtons):
    _bstyle_="is-centered" # "is-boxed is-centered"




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

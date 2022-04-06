from htag import Tag
import htbulma as b
from htbulma import TagBulma

class SelfProperties:
    _callback=None

    def onchange(self,callback):

        self["onchange"] = self.bind( self.setValue, b"this.value" ).bind( callback )
        # self._callback = callback
        return self

    @Tag.NoRender
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


    @Tag.NoRender
    def setValue(self,value): # override
        # fix value type, using options
        value = self._fixValue(value)

        self["value"] = value
        self.value = value
        if self._callback: self._callback( self )


if __name__=="__main__":

    class Page(Tag):
        def __init__(self):
            super().__init__()

            self <=Input(None, [1, 2, 3], onchange=self.doit )

        async def doit(self,obj):
            # yield "a"
            # yield "b"
            print("==>",obj.value)




    import logging
    logging.basicConfig(format='[%(levelname)-5s] %(name)s: %(message)s',level=logging.DEBUG)
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
    logging.getLogger("htag.tag").setLevel( logging.INFO )

    app=Page()

    from htag.runners import *
    # r=GuyApp( app )
    # r=PyWebWiew( app )
    # r=BrowserStarletteHTTP( app )
    # r=BrowserStarletteWS( app )
    r=BrowserHTTP( app )
    # r=WebHTTP( lambda: Page() )
    r.run()

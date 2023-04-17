
# -*- coding: utf-8 -*-
# the simplest htag'app, in the best env to start development (hot reload/refresh)

from htag import Tag
from htbulma import ServerStorage,LocalStorage


class StorageTest(Tag.div):
    imports=[]
    def init(self):
        self.conf=LocalStorage(self.redraw)
        # self.conf=ServerStorage("AEFF")
        # self.redraw()

    def redraw(self):
        self.clear()
        self<=f"hello {self.conf['v'] or '?'}"
        self<=Tag.button("set 1",_onclick=self.set1)
        self<=Tag.button("set 2",_onclick=self.set2)
        self<=Tag.button("clear",_onclick=self.clr)
        self+= Tag.hr()
        self+= self.conf

    def set1(self,o):
        self.conf["v"]=1
        self.redraw()
    def set2(self,o):
        self.conf["v"]=2
        self.redraw()
    def clr(self,o):
        self.conf.clear()
        self.redraw()

App=StorageTest
# #=================================================================================
from htag.runners import DevApp as Runner
# from htag.runners import BrowserHTTP as Runner
# from htag.runners import ChromeApp as Runner

app=Runner(App)
if __name__=="__main__":
    app.run()

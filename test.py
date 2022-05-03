from htag import Tag
import htbulma as b



if __name__=="__main__":

    ALLTAGS = ["banana", "apple", "pear", "peach", "melon", "cherry", "plum"]


    class MyTabs(b.Tabs):  # inherit
        def init(self):
            self.addTab("P1", "I'm the page1")
            self.addTab("P2", "Currently, I am the page2 !")

    class Page(Tag):
        def init(self):
            self.select=2
            self.disabled=False
            self.ll = [(i + 1, i + 1, i + 1, i + 1, i + 1) for i in range(33)]
            self.mbox = b.MBox( self )
            self.toast = b.Toaster( self )


            group1=Tag.div()
            group1<=b.VBox()
            group1<=b.HBox( b.Button("hello"), b.Button("hello", _class="is-success") )
            group1<=b.HBox( b.Button("hello"), b.Button("hello", _class="is-small") )
            group1<=b.Tags( ["pear","plum"], ALLTAGS)
            group1<=b.Checkbox( False, "Just do it").onchange(self.onchange)
            group1<=b.Button("aff modal",_onclick=self.bind.affmodal())
            group1<=b.Button("aff toast",_onclick=self.bind.afftoast())
            group1<=b.Input("input text").onchange(self.onchange)
            group1<=b.Input("input passwd", type="password").onchange(self.onchange)
            group1<=b.Textarea("text area").onchange(self.onchange)
            group1<=b.Range(42,_min=0,_max=100).onchange(self.onchange)
            group1<=b.Content( "<h1>Hello</h1>" )
            group1<=b.Progress()


            group2=Tag.div()
            # #=============== selectors
            group2<=b.TabsHeader(self.select, [1, 2, 3])
            group2<=b.Radio(self.select, [1, 2, 3])
            group2<=b.SelectButtons(self.select, [1, 2, 3], onchange=self.doit )
            group2<=b.Select(self.select, [1, 2, 3])
            # # # #===============


            table = b.Table(self.ll, cols=list("abcde"), pageSize=10, pageIndex=0)
            split=b.HSplit( group2, table , sizes=[30,70])

            def showFile(n):
                self.toast.show( n, 1000 )

            commons={}
            f=b.Fields()
            f.addField("Name", b.Input("mamamam",**commons))
            f.addField("Surname", b.Input("kookokko",**commons), "not mine!")
            f.addField("Sex", b.Radio(1,[1,2,3],**commons))
            f.addField("Other", [b.Select(1,[1,2,3],**commons), b.Select(None,[None,1,2,3],**commons) ])
            f.addField("Address", b.Textarea("",_rows="2",**commons))
            f.addField("Size", b.Range(10,_min=0, _max=100, **commons))
            f.addField("Ok with that", b.Checkbox(False,"Sure?", **commons))

            tab = b.Tabs()
            tab.addTab("Tab1", group1)
            tab.addTab("Tab2", split)
            tab.addTab("Tab3", table)
            tab.addTab("Tab4", b.FileSelect(".", showFile,"*.py"))
            tab.addTab("A form", f)
            tab.selected = "Tab2"

            nav= b.Nav("HTag Demo")
            nav.addEntry( "Page1", self.affmodal )
            nav.addEntry( "exit", lambda: self.exit(), True )

            self <= nav
            self <= b.Section() <= tab

        def affmodal(self):
            self.mbox.show( MyTabs(_style="border:1px solid red") )

        def afftoast(self):
            self.toast.show( "Hello World", 1000 )

        def onchange(self,obj):
            print("++++++++++++++++++++++",obj)
            self.toast.show( obj.value, 1000 )

        def doit(self,obj):
            # yield "a"
            # yield "b"
            print("=====+=========ù*******",obj)




    import logging
    logging.basicConfig(format='[%(levelname)-5s] %(name)s: %(message)s',level=logging.DEBUG)
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
    logging.getLogger("htag.tag").setLevel( logging.INFO )


    from htag.runners import *
    # r=GuyApp( Page )
    # r=PyWebWiew( Page )
    # r=BrowserStarletteHTTP( Page )
    # r=BrowserStarletteWS( Page )
    r=BrowserHTTP( Page )
    # r=WebHTTP( Page )
    r.run()

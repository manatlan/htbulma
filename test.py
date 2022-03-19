from htag import Tag
import htbulma as b


if __name__=="__main__":

    ALLTAGS = ["banana", "apple", "pear", "peach", "melon", "cherry", "plum"]


    class MyTabs(b.Tabs):  # inherit
        def __init__(self,**a):
            super().__init__(**a)
            self.addTab("P1", "I'm the page1")
            self.addTab("P2", "Currently, I am the page2 !")

    class Page(Tag):
        def __init__(self):
            super().__init__()
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
            group1<=b.Checkbox( False, "Just do it")
            group1<=b.Button("aff modal",_onclick=self.bind.affmodal())
            group1<=b.Button("aff toast",_onclick=self.bind.afftoast())
            group1<=b.InputText("input text", onchange = self.onchange)
            group1<=b.InputText("input passwd", type="password", onchange = self.onchange)
            group1<=b.TextArea("text area", onchange = self.onchange)
            group1<=b.Slider(42,0,100, onchange = self.onchange)
            group1<=b.Content( "<h1>Hello</h1>" )
            group1<=b.Progress()


            group2=Tag.div()
            # #=============== selectors
            group2<=b.TabsHeader(self.select, [1, 2, 3], self.disabled )
            group2<=b.RadioButtons(self.select, [1, 2, 3], self.disabled)
            group2<=b.SelectButtons(self.select, [1, 2, 3], self.disabled)
            group2<=b.Select(self.select, [1, 2, 3], self.disabled)
            # # # #===============


            table = b.Table(self.ll, cols=list("abcde"), pageSize=10, pageIndex=0)
            split=b.HSplit( group2, table , sizes=[30,70])

            tab = b.Tabs()
            tab.addTab("Tab1", group1)
            tab.addTab("Tab2", split)
            tab.addTab("Tab3", table)
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

        def onchange(self,v):
            print("++++++++++++++++++++++",v)
            self.toast.show( v, 1000 )






    app=Page()

    from htag.runners import *
    # r=GuyApp( app )
    # r=PyWebWiew( app )
    # r=BrowserStarletteHTTP( app )
    # r=BrowserStarletteWS( app )
    r=BrowserHTTP( app )
    # r=WebHTTP( lambda: Page() )
    r.run()

from htag import Tag
import htbulma as b



ALLTAGS = ["banana", "apple", "pear", "peach", "melon", "cherry", "plum"]


class MyTabs(b.Tabs):  # inherit
    def __init__(self,**a):
        super().__init__(**a)
        self.addTab("P1", "I'm the page1")
        self.addTab("P2", "Currently, I am the page2 !")

class Page(Tag):
    def init(self):
        self.select=2
        self.disabled=False
        self.ll = [(i + 1, i + 1, i + 1, i + 1, i + 1) for i in range(33)]
        self.s = b.Service( self )


        group1=Tag.div()
        group1<=b.VBox()
        group1<=b.HBox( b.Button("hello"), b.Button("hello", _class="is-success") )
        group1<=b.HBox( b.Button("hello"), b.Button("hello", _class="is-small") )
        group1<=b.Tags( ["pear","plum"], ALLTAGS)
        group1<=b.Checkbox( False, "Just do it",_onchange=self.onchange)
        group1<=b.Button("aff modal",_onclick=self.bind.affmodal())
        group1<=b.Button("aff toast",_onclick=self.bind.afftoast())
        group1<=b.Input("input text",_onchange=self.onchange)
        group1<=b.Input("input passwd", type="password",_onchange=self.onchange)
        group1<=b.Textarea("text area",_onchange=self.onchange)
        group1<=b.Range(42,_min=0,_max=100,_onchange=self.onchange)
        group1<=b.Content( "<h1>Hello</h1>" )
        group1<=b.Progress()


        group2=Tag.div()
        # #=============== selectors
        group2<=b.TabsHeader(self.select, [1, 2, 3])
        group2<=b.Radio(self.select, [1, 2, 3])
        group2<=b.SelectButtons(self.select, [1, 2, 3], _onchange=self.doit )
        group2<=b.Select(self.select, [1, 2, 3])
        # # # #===============


        table = b.Table(self.ll, cols=list("abcde"), pageSize=10, pageIndex=0)
        split=b.HSplit( group2, table , sizes=[30,70])

        def showFile(n):
            self.s.toast( n, 1000 )

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
        tab.addTab("A form", f + b.Loader())
        tab.selected = "Tab2"

        def action(v):
            self.s.toast( f"Action v={v}" )

        nav= b.Nav("HTag Demo")
        nav.addEntry("alert", self.affmodal )
        nav.addEntry("confirm", lambda: self.s.confirm("Sure ?",ok=lambda o: action("ok"))   )  # declare an entry in the nav bar
        nav.addEntry("prompt",  lambda: self.s.prompt("What is your name ?","",ok=lambda o: action(o.value)) )  # declare an entry in the nav bar

        nav.addEntry( "exit", lambda: self.exit(), True )

        self <= nav
        self <= b.Section() <= tab

    def affmodal(self):
        self.s.alert( MyTabs(_style="border:1px solid red") )

    def afftoast(self):
        self.s.toast( "Hello World", 1000 )

    def onchange(self,obj):
        print("++++++++++++++++++++++",obj)
        self.s.toast( obj.value, 1000 )

    def doit(self,obj):
        # yield "a"
        # yield "b"
        print("=====+=========ù*******",obj)




# import logging
# logging.basicConfig(format='[%(levelname)-5s] %(name)s: %(message)s',level=logging.DEBUG)
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
# logging.getLogger("htag.tag").setLevel( logging.INFO )


from htag.runners import DevApp as Runner
r=Runner( Page )
if __name__=="__main__":
    r.run()

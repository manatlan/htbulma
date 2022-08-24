from htag import Tag
import htbulma as b

class App(Tag.body):
    statics=r"""
    html,body {width:100%;height:100%;margin:0px}

    .clair {background:#EEE}
    .clair * {color:red !important}

    .fonce {background:#444}
    .fonce * {color:yellow !important}
    """

    def init(self):
        self.main = b.Content("here is the content")

        menu = b.VBox(
            b.Button( "Hello1", _onclick = self.test),
            b.A( "Hello2", _onclick = self.test),
            b.Button( "Hello3", _onclick = self.test),
        )

        self.sidebar = b.NavSide( "MyAppFonce",menu, class_color="fonce" )
        #~ self.sidebar = NavSide( "MyAppClaire",menu, class_color="clair" )
        #~ self.sidebar = NavSide( "MyApp",menu )

        self.main <= Tag.i("You are in BIG Screen",_class="onlyBig")
        self.main <= Tag.i("You are in SMALL Screen",_class="onlySmall")


        self <= self.sidebar + self.main

    def test(self,o):
        self.sidebar.hide()
        self.main <= o.innerHTML+" "

############################################################
from htag.runners import DevApp
app=DevApp( App )

if __name__=="__main__":
    app.run()
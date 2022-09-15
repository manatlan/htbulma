from htag import Tag
import htbulma as b


class App(Tag.body):

    def init(self):
        self._s = b.Service(self)

        self += Tag.button( "Popmenu", _onclick=self.pmenu)
        self += Tag.button( "Toast", _onclick=self.toast)

    def pmenu(self,o):
        entries=[
            Tag.a("menu1", v="1",_onclick=self.entry),
            Tag.A("menu2", v="2",_onclick=self.entry),
            Tag.A("alert", _onclick=self.alert),
            Tag.A("confirm()", _onclick=self.confirm),
            Tag.A("prompt()", _onclick=self.prompt),
            Tag.A("toast()", _onclick=self.toast),
            Tag.A("clipboard()", _onclick=self.cc),
            Tag.hr(_style="padding:0px;margin:0px"),
            "nimp:",
            Tag.button("menu3", v="3",_onclick=self.pmenu),
        ]
        self._s.popmenu(entries,o)

    def cc(self,o):
        import time
        self._s.clipboard( str(time.time()) )

    def toast(self,o):
        self._s.toast("hello")

    def entry(self,o):
        self._s.alert( "hello"+o.v )

    def alert(self,o):
        self._s.alert( b.Input("yo") )

    def confirm(self,o):

        def ok(o):
            print("ok",o)
        def ko(o):
            print("ko",o)

        self._s.confirm( "koi?",ok,ko )


    def prompt(self,o):

        def ok(o):
            print("ok",o.value)
        def ko(o):
            print("ko",o)

        self._s.prompt( "koi?","val",ok,ko )

############################################################
from htag.runners import DevApp
app=DevApp( App )

if __name__=="__main__":
    app.run()
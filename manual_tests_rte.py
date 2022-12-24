
# -*- coding: utf-8 -*-
# the simplest htag'app, in the best env to start development (hot reload/refresh)

from htag import Tag
from htbulma import RichText

import html,json

class App(Tag.body):

    imports=[RichText]

    def init(self):
        contentH = "<b>Hello</b> <i>World</i>"
        contentJ={"ops": [{"attributes": {"bold": True}, "insert": "Hello"}, {"insert": " "}, {"attributes": {"italic": True}, "insert": "DELTA"}, {"insert": "\n"}]}

        def show(o):
            if isinstance(o.value,str):
                h = html.escape(o.value)
            else:
                h = html.escape( json.dumps(o.value))
            result.set(h)

        def setterH(o):
            rte.value = contentH
        def setterJ(o):
            rte.value = contentJ

        # build ui
        rte=RichText(contentH,onsave=show)
        result = Tag.div()

        # draw ui
        self += rte
        self += Tag.button("save html",_onclick=rte.save )
        self += Tag.button("save json",_onclick=rte.saveJSON )
        self += Tag.button("set html",_onclick=setterH )
        self += Tag.button("set json",_onclick=setterJ )
        self += result

# #=================================================================================
from htag.runners import DevApp as Runner
# from htag.runners import BrowserHTTP as Runner
# from htag.runners import ChromeApp as Runner

app=Runner(App)
if __name__=="__main__":
    app.run()

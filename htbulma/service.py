# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

from htag import Tag
from . import TagBulma,Button,HBox,Content


"""
will replace old services MBox,Toaster,PopMenu,Clipboard
with just One (unclear'able) service named 'Service' (poor name)
it does all the same thing, but :
 - in one object Service
 - this instance can reattach automatically (after a clear childs)
 - modal features with keyboard event (esc/return) (except: alert, just escape)
 - all objets are unlimited (ex: you can pop multiple popmenu at a time)
 - all objets use the last highend features of htag (0.8.4 at this time)
 - popmenu can contains a list of object (not only Tag.A), and can open on new event htag feature
 - all are betters

"""

class PopMenu(Tag.div):
    def init(self,entries,x,y):
        omenu=Tag.ul(_class="menu-list")
        for obj in entries:
            if isinstance(obj,Tag) and obj.tag in ["a","A"] and obj["onclick"]:
                # Only a[@onclick] auto-close the popmenu...
                obj["onclick"].bind(self.close)
            omenu += Tag.li( obj )

        self += Tag.div(
            _class="modal-background",
            _onclick=self.close,
            _style="background-color:inherit;z-index:9"
        )

        js="""(function(tag,x,y) {
            tag.style="position:fixed;z-index:10;padding:2px;left:"+x+"px;top:"+y+"px";
            let bw=document.body.clientWidth;
            let bh=document.body.clientHeight;
            let w=tag.clientWidth;
            let h=tag.clientHeight;
            
            if(x+w > bw) x=bw-w;
            if(y+h > bh) y=bh-h;
            
            tag.style="position:fixed;z-index:10;padding:2px;left:"+x+"px;top:"+y+"px";
        })(tag,%s,%s)"""
        
        self += Tag.div(
            Tag.aside( omenu,_class="menu"),
            _class="card",
            js=js % (x,y),
        )

    def close(self,o=None):
        self.remove()
  
class Modal(Tag.div):
    def init(self, content, canClose=True, full=False):
        self["class"] = "modal is-active"

        bg=Tag.div(_class="modal-background")
        self += bg
        if canClose:
            bg["onclick"]=self.close
            self += Tag.div(
                _class="modal-close is-large",
                _aria_label="close",
                _onclick=self.close,
            )
            self["onkeydown"]="""if(event.which == 13) %s; if(event.which == 27) %s;""" % (self.bind.onkey(True),self.bind.onkey(False))

        self += Tag.div(
            Tag.div(
                content,
                _tabindex=0,
                js="tag.focus()",
                _style="outline: none" + ("height:100%;overflow-y:auto" if full else ""),
                _class="box",
            ),
            _class="modal-content",
            _style = "width:90%;height:98%;" if full else None,
        )

    def onkey(self,valid):
        #default behaviour in modal.mbox
        if valid is False:
            self.close(self)

    def close(self,o):
        self.remove()


class Toast(Tag.div):

    def init(self,content):
        self["class"]="notification has-text-light has-background-grey"
        self["style"] = "position:fixed;left:0px;right:0px;bottom:0px;z-index:1000"
        self+= Tag.button(_class="delete", _onclick=self.close)
        self+= content

    def close(self,o):
        self.remove()

class Service(TagBulma):

    def init(self,parent):
        self["info"]="htbulma services"
        self._root = parent
        self._reroot()

    def _reroot(self):
        """ ensure that this object is attached to a parent/main (_root)
            if not (after a clear()), it re-adds itself to _root (parented object) ;-)
        """
        if self not in self._root.childs:
            self._root.add(self,True) # force reparent (when Tag.STRICT_MODE)


    def clipboard(self,txt):
        self._reroot()

        assert "`" not in txt # ;-)
        self("""
let ta = document.createElement('textarea');
ta.value = `%s`;
tag.appendChild(ta);
ta.select();
document.execCommand('copy');
tag.removeChild(ta);
""" % txt)


    def popmenu(self,entries:list,pos):
        self._reroot()

        if isinstance(pos,Tag):
            x,y=pos.event["clientX"],pos.event["clientY"]
        elif isinstance(pos,tuple):
            x,y=pos
        else:
            raise Exception("popemenu bad call")

        x=PopMenu(entries,x,y)
        self += x
        return x

    def toast(self,content,delay=2000):
        self._reroot()

        x=Toast(content)
        self += x
        # prefer the self() way, to send the js for this case
        # because with x.js, js is re-executed at each redraw
        # and can cause dead objects (when event reach server)
        self("""setTimeout(function(){%s},%s);""" % (x.bind.close(None),delay))
        return x

    def alert(self, content, canClose=True, full=False):
        """ "same" signature as js window.alert() """
        self._reroot()

        x=Modal(content, canClose=canClose, full=full)
        self += x
        return x

    def confirm(self, content, ok, ko=None,txtok="OK",txtko="Cancel"): # -> o.value
        """ "same" signature as js window.confirm() """
        self._reroot()

        bko=Button(txtko, _class="is-light", _style="flex: 1 0 25%;")
        bok=Button(txtok, _style="flex: 1 0 25%;")

        main = Content( content )
        main += HBox(
            Tag.H.div(_style="flex: 1 0 25%;"),
            Tag.H.div(_style="flex: 1 0 25%;"),
            bko,
            bok,
        )

        if ko is None:
            ko=lambda o: None

        x=Modal(main, canClose=True)
        x.onkey = lambda valid: x( f"document.getElementById('{id(valid and bok or bko)}').click()" )
        bok["onclick"].bind(ok).bind(x.close)
        bko["onclick"].bind(ko).bind(x.close)

        self += x
        return x


    def prompt(self, title, defaultValue, ok, ko=None,txtok="OK",txtko="Cancel"): # -> o.value
        """ "same" signature as js window.prompt() """
        self._reroot()

        input = Tag.input(_value=defaultValue, js="tag.focus();tag.setSelectionRange(0, tag.value.length)", _class="input")

        bko=Button(txtko, _class="is-light", _style="flex: 1 0 25%;")
        bok=Button(txtok, _style="flex: 1 0 25%;")

        main = Content( Tag.h3(title) )
        main += input
        main += HBox(
            Tag.H.div(_style="flex: 1 0 25%;"),
            Tag.H.div(_style="flex: 1 0 25%;"),
            bko,
            bok,
            _style="margin-top:10px"
        )

        def getv(o,x):
            # save the value in the button object
            o.value = x

        x=Modal(main, canClose=True, full=False)
        x.onkey = lambda valid: x( f"document.getElementById('{id(valid and bok or bko)}').click()" )

        js_get_value = b"document.getElementById('%d').value" % id(input)
        bok["onclick"].bind( getv, js_get_value ).bind(ok).bind(x.close)
        bko["onclick"].bind( getv, js_get_value ).bind(ko).bind(x.close)

        self += x
        return x


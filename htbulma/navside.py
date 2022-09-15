# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from . import TagBulma
from htag import Tag

class NavSide(TagBulma.div):
    statics = (
        Tag.style(r"""
.aburger {
  transform:scale(1.8,1.3);
  vertical-align: text-bottom;
  padding:3px;
  margin-right:8px;
  cursor:pointer;
}

div.backmenu {
    display:none;
    z-index:9;
    position:fixed;
    top:0px;
    bottom:0px;
    left:0px;
    right:0px;
    background:#888;
    opacity:0.5;
}

div.menupop {
    position:fixed;
    z-index:20;
    top: var(--ns-top);
    bottom:0px;
    left:0px;
    width: var(--ns-width);
    height:100%;
    overflow:auto;
    background:white;

    -webkit-transition: left 0.2s ease-in-out;
    -moz-transition: left 0.2s ease-in-out;
    -ms-transition: left 0.2s ease-in-out;
    -o-transition: left 0.2s ease-in-out;

}

body {
    padding-left: var(--ns-width) !important;
    padding-top: var(--ns-top) !important;
}

.onlyBig   { display:inherit }
.onlySmall { display:none }

@media (max-width: 800px) {

    div.menupop { left: var(--ns-width-mobile-sub) }

    body { padding-left:0px !important }

    .menuShow div.menupop {
        left: 0px;
        width: var( --ns-width-mobile );
    }
    .menuShow div.backmenu { display:block }

    .onlyBig   { display:none }
    .onlySmall { display:inherit }

}"""),
        Tag.script("""
function switchMenu() { document.body.classList.toggle("menuShow") }
function hideMenu()   { document.body.classList.remove("menuShow") }
""")
    )
    def init(self,title,sidecontent,width:str="200px",width_small:str="80%",class_color:str="is-black", **a):

        bb=Tag.div("&#9776;",_class="aburger onlySmall",_onclick="switchMenu()")

        nav= Tag.nav(_role="navigation",_aria_label="main navigation", _class="navbar is-fixed-top "+class_color)
        nav <= Tag.div(_class="navbar-brand") <= Tag.span(bb + title,  _class="navbar-item")

        width_m="80%"

        self <= Tag.style(f"""
:root {{
  --ns-top: 52px;
  --ns-width: {width};
  --ns-width-mobile: {width_small};
  --ns-width-mobile-sub: -{width_small};
}}
        """)
        self <= nav
        self <= Tag.div(_class="backmenu click",_onclick="switchMenu()")    # greyed background
        self <= Tag.div(sidecontent,_class="menupop")

    def hide(self):
        """ hide menu if on mobile """
        self("""hideMenu()""")


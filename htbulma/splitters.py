# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################

from htag import Tag
import json

class TagWcSplyt(Tag.wc_splyt):

    # statics = Tag.H.script(_src="https://my.netlib.re/wyc/gen/splyt.py")  # WYC "web component" in python ;-)
    statics = [Tag.H.script(r"""var $jscomp=$jscomp||{};$jscomp.scope={};$jscomp.createTemplateTagFirstArg=function(c){return c.raw=c};$jscomp.createTemplateTagFirstArgWithRaw=function(c,p){c.raw=p;return c};
!function(c,p){"object"==typeof exports&&"undefined"!=typeof module?module.exports=p():"function"==typeof define&&define.amd?define(p):(c=c||self).Split=p()}(this,function(){var c="undefined"!=typeof window?window:null,p=null===c,x=p?void 0:c.document,r=function(){return!1},Y=p?"calc":["","-webkit-","-moz-","-o-"].filter(function(g){var e=x.createElement("div");return e.style.cssText="width:"+g+"calc(9px)",!!e.style.length}).shift()+"calc",O=function(g){if("string"==typeof g||g instanceof String){var e=
x.querySelector(g);if(!e)throw Error("Selector "+g+" did not match a DOM element");return e}return g},q=function(g,e,m){g=g[e];return void 0!==g?g:m},E=function(g,e,m,t){if(e){if("end"===t)return 0;if("center"===t)return g/2}else if(m){if("start"===t)return 0;if("center"===t)return g/2}return g},Z=function(g,e){var m=x.createElement("div");return m.className="gutter gutter-"+e,m},aa=function(g,e,m){var t={};return"string"==typeof e||e instanceof String?t[g]=e:t[g]=Y+"("+e+"% - "+m+"px)",t},ba=function(g,
e){var m;return(m={})[g]=e+"px",m};return function(g,e){function m(d,a,b,f){var l=P(y,a,b,f);Object.keys(l).forEach(function(h){d.style[h]=l[h]})}function t(){return n.map(function(d){return d.size})}function Q(d){var a=n[this.a],b=n[this.b],f=a.size+b.size;a.size=d/this.size*f;b.size=f-d/this.size*f;m(a.element,a.size,this._b,a.i);m(b.element,b.size,this._c,b.i)}function ca(d){var a,b=n[this.a],f=n[this.b];this.dragging&&(a=("touches"in d?d.touches[0][A]:d[A])-this.start+(this._b-this.dragOffset),
1<G&&(a=Math.round(a/G)*G),a<=b.minSize+R+this._b?a=b.minSize+this._b:a>=this.size-(f.minSize+R+this._c)&&(a=this.size-(f.minSize+this._c)),Q.call(this,a),q(e,"onDrag",r)(t()))}function S(){var d=n[this.b].element,a=n[this.a].element.getBoundingClientRect();d=d.getBoundingClientRect();this.size=a[y]+d[y]+this._b+this._c;this.start=a[H];this.end=a[I]}function T(d){var a=function(h){if(!getComputedStyle)return null;var k=getComputedStyle(h);if(!k)return null;h=h[J];return 0===h?null:h-("horizontal"===
B?parseFloat(k.paddingLeft)+parseFloat(k.paddingRight):parseFloat(k.paddingTop)+parseFloat(k.paddingBottom))}(C);if(null===a||K.reduce(function(h,k){return h+k},0)>a)return d;var b=0,f=[],l=d.map(function(h,k){var u=a*h/100,v=E(D,0===k,k===d.length-1,F);v=K[k]+v;return u<v?(b+=v-u,f.push(0),v):(f.push(u-v),u)});return 0===b?d:l.map(function(h,k){var u=h;0<b&&0<f[k]-b&&(u=Math.min(b,f[k]-b),b-=u,u=h-u);return u/a*100})}function da(){var d=n[this.a].element,a=n[this.b].element;this.dragging&&q(e,"onDragEnd",
r)(t());this.dragging=!1;c.removeEventListener("mouseup",this.stop);c.removeEventListener("touchend",this.stop);c.removeEventListener("touchcancel",this.stop);c.removeEventListener("mousemove",this.move);c.removeEventListener("touchmove",this.move);this.move=this.stop=null;d.removeEventListener("selectstart",r);d.removeEventListener("dragstart",r);a.removeEventListener("selectstart",r);a.removeEventListener("dragstart",r);d.style.userSelect="";d.style.webkitUserSelect="";d.style.MozUserSelect="";
d.style.pointerEvents="";a.style.userSelect="";a.style.webkitUserSelect="";a.style.MozUserSelect="";a.style.pointerEvents="";this.gutter.style.cursor="";this.parent.style.cursor="";x.body.style.cursor=""}function ea(d){if(!("button"in d)||0===d.button){var a=n[this.a].element,b=n[this.b].element;this.dragging||q(e,"onDragStart",r)(t());d.preventDefault();this.dragging=!0;this.move=ca.bind(this);this.stop=da.bind(this);c.addEventListener("mouseup",this.stop);c.addEventListener("touchend",this.stop);
c.addEventListener("touchcancel",this.stop);c.addEventListener("mousemove",this.move);c.addEventListener("touchmove",this.move);a.addEventListener("selectstart",r);a.addEventListener("dragstart",r);b.addEventListener("selectstart",r);b.addEventListener("dragstart",r);a.style.userSelect="none";a.style.webkitUserSelect="none";a.style.MozUserSelect="none";a.style.pointerEvents="none";b.style.userSelect="none";b.style.webkitUserSelect="none";b.style.MozUserSelect="none";b.style.pointerEvents="none";this.gutter.style.cursor=
L;this.parent.style.cursor=L;x.body.style.cursor=L;S.call(this);this.dragOffset=("touches"in d?d.touches[0][A]:d[A])-this.end}}function U(d){var a=d.i===z.length,b=a?z[d.i-1]:z[d.i];S.call(b);Q.call(b,a?b.size-d.minSize-b._c:d.minSize+b._b)}if(void 0===e&&(e={}),p)return{};var y,A,H,I,J,n,w=g;Array.from&&(w=Array.from(w));var C=O(w[0]).parentNode,V=getComputedStyle?getComputedStyle(C):null,W=V?V.flexDirection:null,M=q(e,"sizes")||w.map(function(){return 100/w.length}),N=q(e,"minSize",100),K=Array.isArray(N)?
N:w.map(function(){return N}),fa=q(e,"expandToMin",!1),D=q(e,"gutterSize",10),F=q(e,"gutterAlign","center"),R=q(e,"snapOffset",30),G=q(e,"dragInterval",1),B=q(e,"direction","horizontal"),L=q(e,"cursor","horizontal"===B?"col-resize":"row-resize"),ha=q(e,"gutter",Z),P=q(e,"elementStyle",aa),ia=q(e,"gutterStyle",ba);"horizontal"===B?(y="width",A="clientX",H="left",I="right",J="clientWidth"):"vertical"===B&&(y="height",A="clientY",H="top",I="bottom",J="clientHeight");M=T(M);var z=[];return(n=w.map(function(d,
a){var b,f={element:O(d),size:M[a],minSize:K[a],i:a};if(0<a&&((b={a:a-1,b:a,dragging:!1,direction:B,parent:C})._b=E(D,0==a-1,!1,F),b._c=E(D,!1,a===w.length-1,F),"row-reverse"===W||"column-reverse"===W)){var l=b.a;b.a=b.b;b.b=l}0<a&&(l=ha(a,B,f.element),!function(h,k,u){var v=ia(y,k,u);Object.keys(v).forEach(function(X){h.style[X]=v[X]})}(l,D,a),b._a=ea.bind(b),l.addEventListener("mousedown",b._a),l.addEventListener("touchstart",b._a),C.insertBefore(l,f.element),b.gutter=l);return m(f.element,f.size,
E(D,0===a,a===w.length-1,F),a),0<a&&z.push(b),f})).forEach(function(d){var a=d.element.getBoundingClientRect()[y];a<d.minSize&&(fa?U(d):d.minSize=a)}),{setSizes:function(d){var a=T(d);a.forEach(function(b,f){if(0<f){var l=z[f-1],h=n[l.a],k=n[l.b];h.size=a[f-1];k.size=b;m(h.element,h.size,l._b,h.i);m(k.element,k.size,l._c,k.i)}})},getSizes:t,collapse:function(d){U(n[d])},destroy:function(d,a){z.forEach(function(b){if(!0!==a?b.parent.removeChild(b.gutter):(b.gutter.removeEventListener("mousedown",b._a),
b.gutter.removeEventListener("touchstart",b._a)),!0!==d){var f=P(y,b.a.size,b._b);Object.keys(f).forEach(function(l){n[b.a].element.style[l]="";n[b.b].element.style[l]=""})}})},parent:C,pairs:z}}});var _pyfunc_truthy=function(c){return null===c||"object"!==typeof c?c:void 0!==c.length?c.length?c:!1:void 0!==c.byteLength?c.byteLength?c:!1:c.constructor!==Object?!0:Object.getOwnPropertyNames(c).length?c:!1},WcSplyt;
WcSplyt=function(){var c=Reflect.construct(HTMLElement,[],WcSplyt);if(c._template){var p=document.createElement("template");p.innerHTML=c._template;c.attachShadow({mode:"open"}).appendChild(p.content.cloneNode(!0))}c.init&&c.init();return c};WcSplyt.prototype=Object.create(HTMLElement.prototype);WcSplyt.prototype._base_class=HTMLElement.prototype;WcSplyt.prototype.__name__="WcSplyt";WcSplyt.prototype.init=function(){this.root=this.shadowRoot.querySelector("#split");return this._s=null};
WcSplyt.prototype.modeChanged=function(){this.connectedCallback();this.dispatchEvent(new window.Event("change"));return null};WcSplyt.prototype.sizesChanged=function(){var c=this.getAttribute("sizes");_pyfunc_truthy(this._s)&&_pyfunc_truthy(c)&&(this._s.setSizes(JSON.parse(c)),this.dispatchEvent(new window.Event("change")));return null};
WcSplyt.prototype.connectedCallback=function(){var c=_pyfunc_truthy(this.getAttribute("mode"))||"horizontal";var p=JSON.parse(_pyfunc_truthy(this.getAttribute("sizes"))||"[50, 50]");this.root.className=c;_pyfunc_truthy(this._s)&&this._s.destroy();this._s=new Split(this.shadowRoot.querySelectorAll("slot"),{direction:c,sizes:p,minSize:[0,0],onDragEnd:function(x){return this.changeSize(x)}.bind(this)});return null};
WcSplyt.prototype.changeSize=function(c){this.setAttribute("sizes",JSON.stringify(c));this.dispatchEvent(new window.Event("change"));return null};Object.defineProperty(WcSplyt,"observedAttributes",{get:function(){return["mode","sizes"]}});WcSplyt.prototype._template='\n<style>\nslot {display:block}\n\n#split {\n    width:100%;\n    height:100%;\n}\n#split.horizontal {\n    display: flex;\n}\n#split.vertical {\n}\n\n.gutter {\n    background-color: #eee;\n    background-repeat: no-repeat;\n    background-position: 50%;\n}\n\n.gutter.gutter-horizontal {\n    background-image: url(\'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAeCAYAAADkftS9AAAAIklEQVQoU2M4c+bMfxAGAgYYmwGrIIiDjrELjpo5aiZeMwF+yNnOs5KSvgAAAABJRU5ErkJggg==\');\n    cursor: col-resize;\n}\n\n.gutter.gutter-vertical {\n    background-image: url(\'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAFAQMAAABo7865AAAABlBMVEVHcEzMzMzyAv2sAAAAAXRSTlMAQObYZgAAABBJREFUeF5jOAMEEAIEEFwAn3kMwcB6I2AAAAAASUVORK5CYII=\');\n    cursor: row-resize;\n}\n\n</style>\n<div id="split">\n    <slot name="a"></slot>\n    <slot name="b"></slot>\n</div>\n\n    ';
WcSplyt.prototype._reacts={mode:["modeChanged"],sizes:["sizesChanged"]};WcSplyt.prototype.attributeChangedCallback=function(c,p,x){if(this._reacts[c])for(var r in this._reacts[c])this[this._reacts[c][r]]()};customElements.define("wc-splyt",WcSplyt);""")]  # WYC "web component" in python ;-)


    def changeSize(self,v):
        # save the rendering size (to redo the same sizes !)
        self["sizes"] = [int(i) for i in json.loads(v)]

class HSplit(TagWcSplyt):
    def __init__(self,left,right, sizes=[50,50],**a):
        super().__init__(**a)
        self["sizes"] = sizes
        self["mode"] = "horizontal"
        # when sizes change, ensure to inform the py component
        self["onchange"] = self.bind.changeSize( b"this.getAttribute('sizes')")
        self <= Tag.H.div(left,_slot="a",_style="height:100%")
        self <= Tag.H.div(right,_slot="b",_style="height:100%")

class VSplit(TagWcSplyt):
    def __init__(self,up,down, sizes=[50,50],**a):
        super().__init__(**a)
        self["sizes"] = sizes
        self["mode"] = "vertical"
        self["onchange"] = self.bind.changeSize( b"this.getAttribute('sizes')")
        self <= Tag.H.div(up,_slot="a",_style="height:100%")
        self <= Tag.H.div(down,_slot="b",_style="height:100%")


if __name__=="__main__":
    v1=VSplit("top1","bottom1")
    v2=VSplit("top2","bottom2",sizes=[30,70])
    obj= HSplit(v1,v2)

    from . import _test
    _test( obj )

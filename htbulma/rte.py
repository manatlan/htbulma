# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from htag import Tag

import json,html

"""
The latest (most recent) object (happy christmas 2022 !)
(it's coded using the latest tricks of htag (can be a reference, for future!))

MORE:
    - js method to force save, in js/clientside
LESS:
    - it's not like others "inputs" standards here ;-(. So this object doesn't work as a b.Textarea, for example ;-(
    - 2 interactions ... but will be better in next htag version !
"""

class RichText(Tag.div):
    """ Rich Text Editor, based on Quill : https://quilljs.com/
        can deal with "real html" or "quill's delta"

        @value           : can be html or delta
        @onsave          : if defined, call a python callback (cb(self)) on '.save*()'
        @edit            : can make editable or not (default : true), but not dynamic !!!
        @opts            : (list) toolbar opts (see quilljs)
        .value           : is dynamic
        .eventSave()     : create an event to update server side (with html content)
        .eventSave(True) : create an event to update server side (with DELTA content)
    """

    statics=Tag.link(_href="//cdn.quilljs.com/1.3.6/quill.snow.css",_rel="stylesheet")
    statics+=Tag.script(_src="//cdn.quilljs.com/1.3.6/quill.js",_type="text/javascript")

    def init(self,value:"str or delta", onsave:"cb(self)"=None, opts:list=None, edit:bool=True, **a):
        self.onsave = onsave
        if opts is None:
            opts = [
              [{ 'header': [1, 2, 3, False] }],
              [{ 'size': ['small', False, 'large', 'huge'] }],
              [{ 'color': [] }, { 'background': [] }],
              ['bold', 'italic', 'underline', 'strike'],
              ['link', 'code-block'],
              [{ 'list': 'ordered'}, { 'list': 'bullet' }],
              #~ [{ 'indent': '-1'}, { 'indent': '+1' }],
              [{ 'align': [] }],
              ['clean'],
            ]

        self.js="""
            tag.ed = new Quill(tag, {
              modules: {
                toolbar: %s,
              },
              readOnly: %s,
              theme: %s,
            });

            tag.save = function(asDelta) {
                if(asDelta)
                    var value=tag.ed.getContents();
                else
                    var value=tag.ed.root.innerHTML;
                %s;
            }
            """ % (
            edit and json.dumps(opts) or "false",
            edit and "false" or "true",
            edit and "'snow'" or "false",
            self.bind._set(b"value"),
            )
        self.setValue(value,init=True)


    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,value):
        self.setValue(value)

    def setValue(self,value:"str or delta",init:bool=False):
        self._value=value
        if isinstance(value,str):
            if init:
                self.set( value )
            else:
                self( f"tag.ed.setContents(tag.ed.clipboard.convert(`{value}`) ,'silent');" )
        else:
            cmd=f"tag.ed.setContents( {json.dumps(value)}, 'silent')"
            if init:
                self.js += cmd
            else:
                self( cmd )


    def save(self,obj=None):
        self( "tag.save(false)")
    def saveJSON(self,obj=None):
        self( "tag.save(true)")

    def _set(self, data:"str or delta"):
        self.value = data
        if self.onsave: self.onsave( self )


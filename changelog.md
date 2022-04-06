### 0.2.4 2022/04/06

 * all inputs can now call a real htag callback (with async/generator etc ..)
 * (use htag 0.1.6 with multi bindings)
 * SelectButtons & TabsHeader doesn't provide .onchange anymore ! use onchange attribut only !
 * in general : the .onchange() was a bad idea and will be removed for others inputs too, soon

### 0.2.3 2022/04/06

 * inputs : onchange is now in the signature of constructor of all inputs (prefer this) (like in the past)
 * nav : don't show the burger if no entries

### 0.2.2 2022/04/01

 * FIX : Fields produced a full static form fields ;-(

### 0.2.1 2022/03/31

 * select(@name) was bugued ;-(

### 0.2.0 "Inputs breaking changes" 2022/03/30

 * Form implements its own submit() method
 * Fields, simple object to build a "form" template (can't be simpler)
 * bye bye : InputText,TextArea,Checkbox,Slider,RadioButtons,SelectButtons,Select
 * welcome : Input,Range,Checkbox,Radio,SelectButtons,TabsHeader,Select,Textarea
 * theses new ones are better, in all way (they.work in same way, with .onchange(), name=xxx, and attrs _readonly, _required, _disabled, ...)
 * Input can handle a datalist (dict or list) (like a combobox)
 * others can handle a dict or list too (radio, select, ...)

### 0.1.2  2022/03/24

 * FileUpload transfer as base64 and decode to bytes now

### 0.1.1  2022/03/24

 * FileUpload transfer binary string now (if text, you will need to decode))
 * FileSelect is now limited to the path (no way to browse/select elsewhere), security !!!
 * signature change: FileSelect( path, cb(fullpath), pattern="*" )

### 0.1.0 "use the new" 2022/03/23

 * for htag >= 0.1.0
 * add FileSelect( path, cb(fullpath) ) (need to add security blocker!)
 * add FileUpload( cb(name,content) )

### 0.0.8 "add form" 2022/03/22

 * use "Tag.NoRender" from htag>=0.0.16 (in place of return 0)

### 0.0.7 "add form" 2022/03/20

 * add Form() object (which onsubmit json formdata without redrawing itself)
 * inputs don't redraw itself after onchange

### 0.0.6 "my name is" 2022/03/19

 * add a meta tag with htbulma version used in rendering
 * add some spaces in Tags()

### 0.0.5 "revert, bad idea" 2022/03/18

 * tabs from tab, are no more in a Box() ;-)
 * revert : Toaster.show(content) take only one object
 * revert : MBox.show(content) take only one object

### 0.0.4 "multi contents" 2022/03/17

 * Toaster.show(*content) can take multiple objects
 * MBox.show(*content) can take multiple objects
 * MBox.confirm(content, ok, ko=None,txtok="OK",txtko="Cancel") (ok/ko are callbacks)

### 0.0.3 "classEnsure ensure" 2022/03/16

 * __version__ is uptodate to toml version
 * classEnsure() is a little bit better (not appending continously)

### 0.0.2 "right imports" 2022/03/16

 * just the package imports

### 0.0.1 "initial public release" 2022/03/15

 * initial public release


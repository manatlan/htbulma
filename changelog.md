### 0.7.2 2022/07/15

 * Splitters redraw correctly now !

### 0.7.1 2022/07/14

 * htbulma.ALL is now a list (not a tuple anymore) ;-)
 * FIX: Splitters resizing doesn't create a hole on right ;-)

### 0.7.0 2022/07/10

 * use htag 0.7 (no more classEnsure() ;-))

### 0.6.2 2022/07/08

 * add Flex,HFlex, VFlex, to build flexbox better ;-)

### 0.6.1 2022/07/05

 * mbox.show(), canClose works as expected now !

### 0.6.0 2022/06/07

 * use htag >= 0.6.0

### 0.5.0 2022/05/28

 * use htag >= 0.5.0

### 0.4.0 2022/05/03

 * use htag >= 0.4.0

### 0.3.0 2022/04/24

 * use htag 0.3.0 (norender is gone, but init+render are backs)

### 0.2.12 2022/04/23

 * Containers can handle list ;-)

### 0.2.11 2022/04/23

 * Some inputs objects was incompatible with htag 0.2.0 (the braces killer): now fixed !

### 0.2.10 2022/04/23

 * just toml conf for dependencies

### 0.2.9 2022/04/22

 * new mbox.prompt(title, defaultValue, ok, ko=None,txtok="OK",txtko="Cancel") ... ok = lambda value: pass
 * mbox.confirm can be answered with keyboard (return/escape)
 * better mbox.show(full)

### 0.2.8 2022/04/21

 * new mbox.show(self, content, canClose=True, full=False) : can make a box in nearly fullscreen

### 0.2.7 2022/04/21

 * Use new mechanism "imports" from htag, to define dependancies
 * add "ALL" to get a list(tuple) of all widgets declared in the lib

### 0.2.6 2022/04/13

 * FIX Checkbox issue, using reactive mode (was always true/on)

### 0.2.5 2022/04/08

 * all inputs keep the instance of the callback/caller given on 'onchange=...'
   (use the Caller.prior from htag>=0.1.8 to do the trick)

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


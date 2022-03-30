### 0.2.0 "Inputs breainkg changes" 2022/03/30

* Form implement its own submit method
* Fields, simple object to build a "form" template (can't be simpler)
* new widgets !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


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


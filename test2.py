from htag import Tag
import htbulma as b


if __name__=="__main__":

    class Page(Tag.div):
        def init(self):

            i = b.HBox( Tag.button(1)+Tag.button(2),Tag.button(3))

            self <= i





    import logging
    logging.basicConfig(format='[%(levelname)-5s] %(name)s: %(message)s',level=logging.DEBUG)
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
    logging.getLogger("htag.tag").setLevel( logging.INFO )

    from htag.runners import *
    # r=GuyApp( Page )
    # r=PyWebWiew( Page )
    # r=BrowserStarletteHTTP( Page )
    # r=BrowserStarletteWS( Page )
    r=BrowserHTTP( Page )
    # r=WebHTTP( Page )
    r.run()

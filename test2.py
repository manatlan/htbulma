from htag import Tag
import htbulma as b


if __name__=="__main__":

    class Page(Tag):
        def __init__(self):
            super().__init__()

            i = b.HBox( Tag.button(1)+Tag.button(2),Tag.button(3))

            self <= i





    import logging
    logging.basicConfig(format='[%(levelname)-5s] %(name)s: %(message)s',level=logging.DEBUG)
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
    logging.getLogger("htag.tag").setLevel( logging.INFO )

    app=Page()

    from htag.runners import *
    # r=GuyApp( app )
    # r=PyWebWiew( app )
    # r=BrowserStarletteHTTP( app )
    # r=BrowserStarletteWS( app )
    r=BrowserHTTP( app )
    # r=WebHTTP( lambda: Page() )
    r.run()

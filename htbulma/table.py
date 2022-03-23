# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htbulma
# #############################################################################
from . import TagBulma, Button
from htag import Tag
import math


class Table(TagBulma):
    """ adapted as is, from gtag.gtags.Table
        NOT OPTIMIZED for htag ... but works as is ;-)
    """
    tag="div"

    def __init__(
        self, rows: list, cols: list = None, pageSize: int = None, pageIndex: int = 0, **a
    ):
        super().__init__(**a)
        self.rows = rows
        self.cols = cols
        self.pageSize = pageSize
        self.pageIndex = pageIndex
        self.update()

    def update(self):
        self.clear()
        if self.cols:
            h = Tag.thead( [Tag.H.th(col) for col in self.cols] )
        else:
            h = None

        if self.pageSize:
            rows = self.rows[
                self.pageIndex * self.pageSize : self.pageIndex * self.pageSize
                + self.pageSize
            ]
            nbPage = math.ceil(len(self.rows) / self.pageSize)
        else:
            rows = self.rows

        ll = []
        for row in rows:
            row = row if hasattr(row, "__iter__") else [row]
            ll.append(Tag.H.tr( [Tag.H.td(col) for col in row]) )

        t=Tag.H.table( _class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth")
        t <= h
        t <= Tag.H.tbody(ll)

        self <= t

        if self.pageSize:
            nav = Tag.H.nav(
                _class="pagination is-small", _role="navigation", _aria_label="pagination"
            )
            if self.pageIndex > 0:
                nav.add(
                    Tag.H.a(
                        "<<",
                        _class="pagination-previous",
                        _onclick=self.bind.setPage(self.pageIndex - 1),
                    )
                )
            else:
                nav.add(Tag.H.a("<<", _class="pagination-previous", _disabled=True))
            if self.pageIndex < nbPage - 1:
                nav.add(
                    Tag.H.a(
                        ">>",
                        _class="pagination-next",
                        _onclick=self.bind.setPage(self.pageIndex + 1),
                    )
                )
            else:
                nav.add(Tag.H.a(">>", _class="pagination-next", _disabled=True))

            ul = Tag.H.ul(_class="pagination-list")
            for i in range(0, nbPage):
                if (i == 0 or i == nbPage - 1 or self.pageIndex - 3 <= i <= self.pageIndex + 3):
                    klass = (
                        "pagination-link is-current"
                        if self.pageIndex == i
                        else "pagination-link"
                    )
                    ul.add(
                        Tag.H.li(
                            Tag.H.a(
                                (i + 1),
                                _class=klass,
                                _aria_label="Goto page %s" % (i + 1),
                                _onclick=self.bind.setPage(i),
                            )
                        )
                    )
                    hole = False
                else:
                    if not hole:
                        ul.add(Tag.H.li(Tag.H.a("&hellip;", _class="pagination-ellipsis")))
                        hole = True

            nav.add(ul)

            self <= nav

    def setPage(self, p):
        self.pageIndex = p
        self.update()

if __name__=="__main__":

    ll = [( Button(i + 1,_class="is-small"), i + 1, i + 1, i + 1, i + 1) for i in range(33)]
    obj=Table(ll, cols=list("abcde"), pageSize=10, pageIndex=0)

    from . import _test
    _test( obj )

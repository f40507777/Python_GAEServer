#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from TableTitle import TableBCLowy, TableChuChuShoe, TableCantine, TablePttjoke,StoreData


sys.path.insert(0, 'libs')
import webapp2


class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('index')


app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/Table_bclowy*', TableBCLowy.TableBCLowyHandler),
                               ('/Table_chuchushoe*', TableChuChuShoe.TableChuChuShoeHandler),
                               ('/Table_Pttjoke*', TablePttjoke.TablePttjokeHandler),
                               ('/Table_Cantine*', TableCantine.TableCantineHandler),
                               ('/get*', StoreData.StoreDataHandler),

                              ], debug=True)

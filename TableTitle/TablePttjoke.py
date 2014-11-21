#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'libs')
import webapp2,json
from StoreData import TablePttJoke

class TablePttjokeHandler(webapp2.RequestHandler):

	def get(self):
		self.parser()

	def parser(self):
		datastores=TablePttJoke.all()
		JsonDict=dict()
		for datalist in datastores:
			for i,data in enumerate(datalist.titles):
				JsonDict[i] = [datalist.titles[i], datalist.urls[i]]
		jsondata = json.dumps(JsonDict)
		self.response.write(jsondata)


app = webapp2.WSGIApplication([('/', TablePttjokeHandler)], debug=True)
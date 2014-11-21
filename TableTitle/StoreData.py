#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'libs')
import webapp2,urllib2
from google.appengine.ext import db
from bs4 import BeautifulSoup




class TableBCLowy(db.Model):
	titles = db.ListProperty(str)
	urls = db.ListProperty(str)

class TableCantine(db.Model):
	titles = db.ListProperty(str)
	urls = db.ListProperty(str)

class TableChuChuShoe(db.Model):
	titles = db.ListProperty(str)
	urls = db.ListProperty(str)

class TablePttJoke(db.Model):
	titles = db.ListProperty(str)
	urls = db.ListProperty(str)



class StoreDataHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write("storedata" + "<br>")
		self.bclowy()
		self.cantine()
		self.chuchushoe()
		self.pttjoke()
		self.response.write("Blog data loading...<br/><br/>")



	def bclowy(self):
		db.delete(TableBCLowy.all())

		url = urllib2.urlopen("http://forgetfulbc.blogspot.com/search")
		html = url.read()
		url.close()
		soup = BeautifulSoup(html)

		titleslist = []
		urlist = []

		for x in soup.findAll(attrs={"class":"post-title entry-title"}):
			handlestr=(x.a.get_text()).strip("\n")
			titleslist.append(handlestr)
			urlist.append(x.a['href'])

		TableBCLowy(titles= titleslist, urls= urlist).put()



	def cantine(self):

		db.delete(TableCantine.all())

		url = urllib2.urlopen("http://traducantine.blogspot.tw/search")
		html = url.read()
		url.close()
		soup = BeautifulSoup(html)

		titleslist = []
		urlist = []

		for x in soup.findAll(attrs={"class":"post-title entry-title"}):
			titleslist.append(x.a.get_text())
			urlist.append(x.a['href'])
		TableCantine(titles= titleslist, urls= urlist).put()

	def chuchushoe(self):

		db.delete(TableChuChuShoe.all())

		url = urllib2.urlopen("http://chuchushoe.blogspot.tw/search?")
		html = url.read()
		url.close()
		soup = BeautifulSoup(html)

		titleslist = []
		urlist = []

		for x in soup.findAll(attrs={"class":"post-title"}):
			titleslist.append(x.a.get_text())
			urlist.append(x.a['href'])
		TableChuChuShoe(titles= titleslist, urls= urlist).put()


	def pttjoke(self):
		db.delete(TablePttJoke.all())

		url = urllib2.urlopen("http://www.pttjoke.com/search")
		html = url.read()
		url.close()
		soup = BeautifulSoup(html)

		titleslist = []
		urlist = []

		for x in soup.findAll(attrs={"class":"post-title"}):
			titleslist.append(x.a.get_text())
			urlist.append(x.a['href'])
		TablePttJoke(titles= titleslist, urls= urlist).put()

app = webapp2.WSGIApplication([('/', StoreDataHandler)], debug=True)
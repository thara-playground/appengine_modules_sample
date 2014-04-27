""" Hello world application. """

import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, webapp2 world!!!!!!!!!!')


APP = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)

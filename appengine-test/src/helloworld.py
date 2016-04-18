import webapp2
from quick_sort import Quick_sort

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Nico\'s personal python test environment here.\
Next: Graphical interface.')
        list_to_sort = [1,2,4,5]
        quick_sort = Quick_sort()
        self.response.write(quick_sort.sortList(list_to_sort))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

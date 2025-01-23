import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return

'''
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = self.parse_query_params()
        
        # Get the marks for the requested names
        marks = [student_marks.get(name, 0) for name in query.get('name', [])]
        
        # Return the response as JSON
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({"marks": marks})
        self.wfile.write(response.encode('utf-8'))

    def parse_query_params(self):
        # Parse query parameters into a dictionary
        query_string = self.path.split('?')[1] if '?' in self.path else ''
        query = {}
        for param in query_string.split('&'):
            key, value = param.split('=')
            if key in query:
                query[key].append(value)
            else:
                query[key] = [value]
        return query
'''
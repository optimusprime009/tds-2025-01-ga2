import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set CORS headers to allow cross-origin requests
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.end_headers()
        
        # Handle query parameters (e.g., ?name=X&name=Y)
        query_params = self.get_query_params()
        marks = [self.get_marks(name) for name in query_params]
        
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def get_query_params(self):
        query = self.path.split('?')[1] if '?' in self.path else ''
        return [param.split('=')[1] for param in query.split('&') if param.startswith('name=')]

    def get_marks(self, name):
        # Simulating mark retrieval for demonstration
        marks = {"X": 10, "Y": 20}  # Example marks for names
        return marks.get(name, 0)


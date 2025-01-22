import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

# Load marks from a JSON file
with open(os.path.join(os.path.dirname(__file__), '../marks.json')) as f:
    MARKS = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = parse_qs(self.path.split('?')[-1])
        names = query.get("name", [])

        # Fetch marks for the provided names
        response = {"marks": [MARKS.get(name, 0) for name in names]}

        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Send JSON response
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return

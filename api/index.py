import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

# Load marks from a JSON file
marks_path = os.path.join(os.path.dirname(__file__), '../q-vercel-python.json')

# Check if the file exists and load data
if os.path.exists(marks_path):
    with open(marks_path) as f:
        MARKS = json.load(f)
else:
    MARKS = []

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = parse_qs(self.path.split('?')[-1])
        names = query.get("name", [])

        # Fetch marks for the provided names
        response = {"marks": [self.get_marks_for_name(name) for name in names]}

        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Send JSON response
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return

    def get_marks_for_name(self, name):
        # Search the list for the name and return corresponding marks, or 0 if not found
        for entry in MARKS:
            if entry['name'] == name:
                return entry['marks']
        return 0  # Default marks if name is not found

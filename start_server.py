#!/usr/bin/env python3
"""
Local HTTP Server for Digital Marketing Service Contract Application
This script starts a local HTTP server to serve the contract application.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time
from pathlib import Path

# Server configuration
HOST = 'localhost'
PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom request handler to ensure proper MIME types"""
    
    def end_headers(self):
        # Add CORS headers to allow all requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_OPTIONS(self):
        """Handle preflight requests"""
        self.send_response(200)
        self.end_headers()

def open_browser():
    """Open the browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open(f'http://{HOST}:{PORT}')

def main():
    """Main function to start the server"""
    # Change to the correct directory
    os.chdir(DIRECTORY)
    
    print(f"Starting Digital Marketing Service Contract Application Server...")
    print(f"Serving directory: {DIRECTORY}")
    print(f"Server running at: http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Create the server
    with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
        # Open browser in a separate thread
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        try:
            # Start the server
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer is shutting down...")
            httpd.server_close()
            print("Server stopped successfully.")

if __name__ == "__main__":
    main()
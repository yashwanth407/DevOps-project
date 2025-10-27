#!/usr/bin/env python3
"""
Tax Calculator Web Application Server
Serves the HTML calculator application with proper error handling and logging
"""

import http.server
import socketserver
import os
import sys
import logging
import signal
import threading
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('server.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

class TaxCalculatorHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler for the tax calculator application"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def log_message(self, format, *args):
        """Override to use our logger instead of stderr"""
        logger.info(f"{self.address_string()} - {format % args}")
    
    def do_GET(self):
        """Handle GET requests with proper routing"""
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/health':
            self.send_health_check()
            return
        elif self.path == '/status':
            self.send_status()
            return
        
        return super().do_GET()
    
    def send_health_check(self):
        """Send health check response"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "status": "healthy",
            "service": "tax-calculator",
            "timestamp": datetime.now().isoformat()
        }
        self.wfile.write(str(response).encode())
    
    def send_status(self):
        """Send server status response"""
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        status = f"Tax Calculator Server Running\nPort: {PORT}\nUptime: {time.time() - start_time:.2f} seconds"
        self.wfile.write(status.encode())

class TaxCalculatorServer:
    """Main server class for the tax calculator application"""
    
    def __init__(self, port=8082):
        self.port = port
        self.httpd = None
        self.server_thread = None
        
    def start(self):
        """Start the web server"""
        try:
            # Verify index.html exists
            if not os.path.exists('index.html'):
                logger.error("index.html not found in current directory")
                return False
            
            # Create server
            self.httpd = socketserver.TCPServer(("", self.port), TaxCalculatorHandler)
            logger.info(f"Tax Calculator Server starting on port {self.port}")
            logger.info(f"Serving directory: {os.getcwd()}")
            logger.info(f"Application URL: http://localhost:{self.port}")
            
            # Start server in a separate thread for graceful shutdown
            self.server_thread = threading.Thread(target=self.httpd.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
            
            logger.info("Server started successfully")
            return True
            
        except OSError as e:
            if e.errno == 98:  # Address already in use
                logger.error(f"Port {self.port} is already in use")
            else:
                logger.error(f"Failed to start server: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error starting server: {e}")
            return False
    
    def stop(self):
        """Stop the web server gracefully"""
        if self.httpd:
            logger.info("Shutting down server...")
            self.httpd.shutdown()
            self.httpd.server_close()
            if self.server_thread:
                self.server_thread.join(timeout=5)
            logger.info("Server stopped")

def signal_handler(signum, frame):
    """Handle shutdown signals gracefully"""
    logger.info(f"Received signal {signum}, shutting down...")
    if 'server' in globals():
        server.stop()
    sys.exit(0)

def main():
    """Main function to run the server"""
    global PORT, start_time, server
    
    # Get port from environment or use default
    PORT = int(os.environ.get('PORT', 8082))
    start_time = time.time()
    
    # Set up signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Create and start server
    server = TaxCalculatorServer(PORT)
    
    if server.start():
        logger.info("Tax Calculator application is ready!")
        logger.info("Press Ctrl+C to stop the server")
        
        try:
            # Keep the main thread alive
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            signal_handler(signal.SIGINT, None)
    else:
        logger.error("Failed to start server")
        sys.exit(1)

if __name__ == "__main__":
    main()

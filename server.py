import os
import webbrowser
from threading import Thread
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class CustomTCPServer(TCPServer):
    allow_reuse_address = True  # Allow reuse of the same port

class WebServer:
    def start(self):
        # Start the local server and open the web page
        if self.start_server():
            self.open_web_page()

    def start_server(self):
        directory = "/storage/emulated/0/website/"  # Path to your local web files
        if not os.path.exists(directory):
            print(f"Directory does not exist: {directory}")
            return False
        
        os.chdir(directory)
        print(f"Serving files from: {directory}")

        def server_thread():
            handler = SimpleHTTPRequestHandler
            with CustomTCPServer(("127.0.0.1", 2025), handler) as httpd:
                try:
                    print("Server started at http://127.0.0.1:2025")
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    print("Shutting down the server...")
                    httpd.shutdown()

        thread = Thread(target=server_thread)
        thread.daemon = True
        thread.start()
        return True

    def open_web_page(self):
        webbrowser.open("http://127.0.0.1:2025")  # Open in the default browser

if __name__ == "__main__":
    server = WebServer()
    server.start()
    input("Press Enter to stop the server...")
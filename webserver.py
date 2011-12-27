#!/usr/bin/python
# This is an original work bearing the following notice:
# Copyright Jon Berg @ turtlemeat.com
# The original author retains all original work rights
# Modifications for ZTNSDS by Quinn Ebert are "free"

# Fair warning:
# At some point, the script will be totally rewritten.  I appreciate Mr. Berg's
# work, but, I am skirting the line offering it this way...

import string, cgi, time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from subprocess import Popen, PIPE

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith(".html"):
                print "Path endswith html"
                f = open(curdir + sep + self.path) #self.path has /test.html
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            # This code was used in my local copy (but not in distribution)
            if self.path.endswith(".jpg"):
                print "Path endswith jpg"
                f = open(curdir + sep + self.path,"r+b") #self.path has /test.html
                self.send_response(200)
                self.send_header('Content-type', 'image/jpeg')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            if self.path.endswith("shutdown"):
                if (which_os() == "WIN"):
                    print "running on Windows"
                    output = Popen(["shutdown", "/s", "/t", "300"],stdout=PIPE).communicate()[0]
                if (which_os() == "MAC"):
                    print "running on Mac OS X"
                    print "NOTE: Mac uses an osascript script to facilitate shutdowns!"
                    output = Popen(["osascript", "HaltLion.scpt"],stdout=PIPE).communicate()[0]
                if (which_os() == "BSD"):
                    print "running on Linux/BSD/Other"
                    print "NOTE: you'll likely need to run as root for best results..."
                    output = Popen(["shutdown", "-h", "now"],stdout=PIPE).communicate()[0]
                f = open(curdir + sep + "byebye.html")
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            if self.path.endswith("bail_out"):
                f = open(curdir + sep + "thanks.html")
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            print "other"
            f = open(curdir + sep + "index.html") #self.path has /test.html
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            return
                
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
     

    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            
            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write("<HTML>POST OK.<BR><BR>");
            self.wfile.write(upfilecontent[0]);
            
        except :
            pass

# This is Quinn's own function: WIN, MAC, or BSD OS?
def which_os():
    from os import path
    if (path.exists("/System/Library/CoreServices/Finder.app/Contents/MacOS/Finder")):
        return "MAC"
    #FIXME: Yeah, I could really easily make this dynamic, but whatever...
    if (path.exists("C:/Windows/Notepad.exe")):
        return "WIN"
    #FIXME: Making an ass out of you and me...
    return "BSD"

def main():
    try:
        server = HTTPServer(('', 8073), MyHandler)
        print 'started httpserver...'
        if (which_os() == "WIN"):
            print "running on Windows"
        if (which_os() == "MAC"):
            print "running on Mac OS X"
        if (which_os() == "BSD"):
            print "running on Linux/BSD/Other"
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()


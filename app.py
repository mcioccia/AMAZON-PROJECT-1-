"""AI-assisted local coursework workbench; educational only, not investment advice."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import argparse
import json
import model

class Handler(BaseHTTPRequestHandler):
    def respond(self, value, status=200):
        body=json.dumps(value,allow_nan=False).encode()
        self.send_response(status); self.send_header('Content-Type','application/json')
        self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(body)

    def do_GET(self):
        if self.path=='/':
            body=(model.ROOT/'static'/'index.html').read_bytes()
            self.send_response(200); self.send_header('Content-Type','text/html; charset=utf-8'); self.end_headers(); self.wfile.write(body)
        elif self.path=='/api/base':
            self.respond({'config':model.load(),'analysis':model.analyses()})
        else: self.respond({'error':'Not found'},404)

    def do_POST(self):
        if self.path!='/api/calculate': return self.respond({'error':'Not found'},404)
        # No files are modified. Restrict browser callers to this local application.
        origin=self.headers.get('Origin')
        if origin and origin not in ('http://'+self.headers.get('Host',''),): return self.respond({'error':'Origin refused'},403)
        try:
            length=int(self.headers.get('Content-Length','0'))
            if not 0<length<20000: raise ValueError('Invalid request size')
            payload=json.loads(self.rfile.read(length))
            if not isinstance(payload,dict): raise ValueError('Expected object')
            if payload.get('diagnostic')=='terminal-domain':
                return self.respond(model.terminal_failure_demo())
            self.respond(model.calculate(payload.get('inputs',{}),break_cash=payload.get('break_cash') is True))
        except (ValueError,TypeError,KeyError) as exc: self.respond({'error':str(exc)},400)

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--port',type=int,default=8767); args=p.parse_args()
    print(model.NOTICE,flush=True); print(f'Amazon workbench: http://127.0.0.1:{args.port}',flush=True)
    ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()

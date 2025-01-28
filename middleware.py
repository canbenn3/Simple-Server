from datetime import datetime
from response import Response

def loggingMiddlewareFactory(nextMidware):
    def middleware(req):
        print(f"Request Method: {req.method}, Path: {req.uri}")
        res = nextMidware(req)
        print(f"Response Code: {res.code}, Reason: {res.reason}")
        return res
    return middleware

def staticMiddlewareFactory(nextMidware):
    def middleware(req):
        print(f"inside staticMiddlewareFactory; req.uri: {req.uri}")
        if req.uri.startswith('/static/'):
            print("\n\n\nA static file was requested\n\n\n")
            try:
                with open(f".{req.uri}", 'r') as f:
                    body = f.read()
                    return Response(
                        version='HTTP1.1',
                        code=200,
                        reason='found',
                        headers={},
                        body=body
                    )
            except FileNotFoundError:
                body = "404 Not Found"
                return Response(
                    version='HTTP1.1',
                    code=404,
                    reason='Not Found',
                    headers={},
                    body=body
                )
        else:
            return nextMidware(req)

    return middleware

def headerMiddlewareFactory(nextMidware):
    def middleware(req):
        res = nextMidware(req)
        t = datetime.today()
        logTime = f"{t.year}-{t.month}-{t.day} {t.hour}:{t.minute}:{t.second}.{t.microsecond}"

        res.headers = {
            'Connection': 'close',
            'Date': f'{logTime}',
            'Server': 'SkyNet server :o',
            'Cache-control': 'max-age=X',
            'Content-Length': f'{len(res.body)}'
        }
        if res.code == 301:
            res.headers['Location'] = 'somewhere?'
        return res
    return middleware

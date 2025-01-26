from datetime import datetime
def loggingMiddlewareFactory(nextMidware):
    def middleware(req):
        print(f"Request Method: {req.method}, Path: {req.uri}")
        res = nextMidware(req)
        print(f"res:\n{res}")
        print(f"Response Code: {res.code}, Reason: {res.reason}")
        return res
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

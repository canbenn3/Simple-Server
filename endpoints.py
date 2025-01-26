from response import Response

def home():
    return Response(
        version='HTTP1.1',
        code='200',
        reason='found',
        headers={},
        body="<h1>Bennett Cannon's home page!!!"
    )
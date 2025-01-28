from response import Response

def home():
    f = open('templates/index.html', 'r')
    return Response(
        version='HTTP1.1',
        code='200',
        reason='found',
        headers={},
        body=f.read()
    )

def about():
    f = open('templates/about.html', 'r')
    return Response(
        version='HTTP1.1',
        code='200',
        reason='found',
        headers={},
        body=f.read()
    )

def experience():
    f = open('templates/experience.html', 'r')
    return Response(
        version='HTTP1.1',
        code='200',
        reason='found',
        headers={},
        body=f.read()
    )

def projects():
    f = open('templates/projects.html', 'r')
    return Response(
        version='HTTP1.1',
        code='200',
        reason='found',
        headers={},
        body=f.read()
    )


def notFound():
    return Response(
        version='HTTP1.1',
        code='404',
        reason='Not Found',
        headers={},
        body=""
    )

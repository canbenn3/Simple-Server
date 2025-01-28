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


def redirect():
    return Response(
        version='HTTP1.1',
        code='301',
        reason='redirect',
        headers={
            'Location': '/about'
        },
        body=''
    )


def notFound():
    return Response(
        version='HTTP1.1',
        code='404',
        reason='Not Found',
        headers={},
        body="<h1>We're sorry...</h1><div>The page you're looking for doesn't exist. click <a href='/'>here</a> to navigate back to the home page.</div"
    )

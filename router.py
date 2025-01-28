from endpoints import home, notFound, about, experience, projects, redirect

def router(req):
    if req.uri == '/':
        return home()
    elif req.uri == '/about':
        return about()
    elif req.uri == '/experience':
        return experience()
    elif req.uri == '/projects':
        return projects()
    elif req.uri == '/info':
        return redirect()
    else:
        return notFound()

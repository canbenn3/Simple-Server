class Request:
    def __init__(
        self,
        method, #string
        uri, #string
        version, #string
        body, #string
        headers, #dict, the keys are the header names and values are the header values
    ):
        self.method = method
        self.uri = uri
        self.version = version
        self.body = body
        self.headers = headers

    def toString(self):
        headers = f""
        for header in self.headers:
            headers += f"{header}: {self.headers[header]}\n"

        return f"{self.method} {self.uri} {self.version}\n{headers}\n{self.body}"
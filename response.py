class Response:
    def __init__(
            self,
            version, #string
            code, #number
            reason, #string
            headers, #dict, the keys are the header names and values are the header values 
            body, #string
    ):
        self.version = version
        self.code = code
        self.reason = reason
        self.headers = headers
        self.body = body

    def toString(self):
        headerStr = f""
        for header in self.headers:
            headerStr += f"{header}: {self.headers[header]}\n"
        return f"{self.version} {self.code} {self.reason}\n{headerStr}\n{self.body}"
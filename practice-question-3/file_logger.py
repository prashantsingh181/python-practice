class FileLogger:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write("--- log ended ---\n")
        self.file.close()
        return False


with FileLogger("app.log") as log:
    log.write("Server started\n")
    log.write("Request received\n")

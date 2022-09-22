from . import templates


class App:
    def __init__(self, name: str,  version: str,
                 template_package=templates, image_name: str = None):
        self.name = name
        self.version = version
        self.image_name = image_name or name + ".app"
        self.image_repo = "somewhere.todo/"
        self.labels = dict()
        self.target_dir = "./target"
        self.template_package = template_package


class Environment:
    def __init__(self, app: App,  name: str):
        self.app = app
        self.name = name

        self.namespace = app.name + "-" + self.name
        self.replicas = 1
        self.vars = dict()

    def add_var(self, name: str, value: str) -> None:
        self.vars[name] = value

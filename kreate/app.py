from . import templates


class App:
    def __init__(self, name: str, env: str,  version: str,
                 template_package=templates, image_name: str = None,
                 namespace: str = None):
        self.name = name
        self.env = env
        self.version = version
        self.namespace = namespace or self.name + "-" + env
        self.replicas = 1
        self.vars = dict()

        self.image_name = image_name or name + ".app"
        self.image_repo = "somewhere.todo/"
        self.labels = dict()
        self.target_dir = "./target"
        self.template_package = template_package

    def add_var(self, name: str, value: str) -> None:
        self.vars[name] = value

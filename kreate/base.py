import sys
import jinja2
import pkgutil

from ruamel.yaml import YAML

from .app import Environment
from .wrapper import DictWrapper


class Base:
    def __init__(self,
                 env : Environment,
                 name: str = None,
                 filename: str = None,
                 template: str = None):
        self.env = env
        self.app = env.app
        self.kind = type(self).__name__
        self.name = name or self.app.name + "-" + self.kind.lower()
        self.filename = filename or self.name + ".yaml"
        self.template = template or self.kind.lower() + ".yaml"
        self.annotations = {}
        self.labels = {}
        self.yaml = None  # Used if you want to modify the yaml

    def kreate_yaml(self):
        self.__yaml = YAML()
        self.yaml = DictWrapper(self.__yaml.load(self.render()))

    def kreate(self) -> None:
        if self.yaml is None:
            print(self.filename)
            self.render(outfile=self.app.target_dir + "/" + self.filename)
        else:
            self.__yaml.dump(self.yaml._dict, sys.stdout)

    def annotate(self, name: str, val: str) -> None:
        self.annotations[name] = val

    def add_label(self, name: str, val: str) -> None:
        self.labels.add[name] = val

    def render(self, outfile=None):
        template_data = pkgutil.get_data(self.app.template_package.__package__,
                                         self.template).decode('utf-8')
        tmpl = jinja2.Template(
            template_data,
            undefined=jinja2.StrictUndefined,
            trim_blocks=True,
            lstrip_blocks=True)
        vars = {
            "app": self.app,
            "env": self.env,
            self.kind.lower(): self}
        if outfile:
            tmpl.stream(vars).dump(outfile)
        else:
            return tmpl.render(vars)

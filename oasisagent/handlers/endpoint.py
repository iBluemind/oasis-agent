from oasisagent.common import script_builder


class Handler(object):
    def __init__(self):
        self.builder = script_builder.ScriptFileBuilder()

    def create(self, func_id, rule):
        self.builder.read(func_id)
        self.builder.set_route(rule)
        self.builder.save()

    def update(self, func_id, rule):
        self.builder.read(func_id)
        self.builder.set_route(rule)
        self.builder.save()

    def get(self, func_id):
        self.builder.read(func_id)
        return str(self.builder.script_file)

    def delete(self, func_id):
        pass


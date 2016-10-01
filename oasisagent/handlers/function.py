from oasisagent.common import script_builder
import uuid


class Handler(object):
    def __init__(self):
        self.builder = script_builder.ScriptFileBuilder()

    def function_create(self, context, func_id, body, rule=None):
        if rule:
            self.builder.set_route(rule)
        else:
            rand = uuid.uuid4()
            self.builder.set_route(rand)

        self.builder.set_function(func_id, body)
        self.builder.save()

    def function_update(self, context, func_id, body):
        pass
        # self.builder.read(func_id)
        # self.builder.set_function(func_id, body)

    def get(self, context):
        pass

    def delete(self, context):
        pass



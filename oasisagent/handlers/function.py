from oasisagent.common import script_builder
from oasisagent.common import flask_task
import uuid


class Handler(object):
    def __init__(self):
        self.process = None
        self.erro = None
        self.builder = script_builder.ScriptFileBuilder()

    def run_service(self, function_id, body, rule, method):
        self.builder.set_route(rule, method)
        self.builder.set_function(function_id, body)
        self.builder.save()

        self.process, self.erro = flask_task.run_flask(function_id)

    def function_create(self, context, function_id, body, rule, methods):
        self.run_service(function_id, body, rule, methods)

        if self.erro == '':
            return "OK"

    def function_update(self, context, function_id, body, rule, methods):
        self.process.kill()

        self.run_service(function_id, body, rule, methods)

        if self.erro == '':
            return "OK"

    def function_delete(self, context, function_id):
        self.process.kill()






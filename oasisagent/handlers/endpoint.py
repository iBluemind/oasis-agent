from oslo_config import cfg
from oasisagent.common import script_builder
import subprocess

CONF = cfg.CONF

class Handler(object):
    def __init__(self):
        self.builder = script_builder.ScriptFileBuilder()

    def endpoint_create(self, context, func_id, rule):
        self.builder.read(func_id)
        self.builder.set_route(rule)
        self.builder.save()

        cmd = ['python', cfg.CONF.agent.function_location]
        fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout


        # (self, args, bufsize=0, executable=None,
        #          stdin=None, stdout=None, stderr=None,
        #          preexec_fn=None, close_fds=False, shell=False,
        #          cwd=None, env=None, universal_newlines=False,
        #          startupinfo=None, creationflags=0):
        # # fd_popen.close()
        print fd_popen.returncode


    def endpoint_update(self, context, func_id, rule):
        self.builder.read(func_id)
        self.builder.set_route(rule)
        self.builder.save()

    def get(self, context, func_id):
        self.builder.read(func_id)
        return str(self.builder.script_file)

    def delete(self, context, func_id):
        pass


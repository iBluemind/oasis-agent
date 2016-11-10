from oslo_config import cfg
import subprocess

CONF = cfg.CONF


def run_flask(function_id):
    flask_function = "%s/%s.py" % (cfg.CONF.agent.function_location, function_id)
    cmd = ['python', flask_function]
    fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # (stdoutdata, stderrdata) = fd_popen.communicate()
    erro = None
    return fd_popen, erro

    # how to catch error?

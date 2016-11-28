from oslo_config import cfg
import subprocess

CONF = cfg.CONF


def run_flask(function_id):

    # flask_function = "%s/%s/%s.py" % (cfg.CONF.agent.function_location, function_id, function_id)
    # execfile(flask_function, dict(__file__=flask_function))

    # cmd = ['python', flask_function]
    # fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # # (stdoutdata, stderrdata) = fd_popen.communicate()
    # erro = None
    # return fd_popen, erro

    retval = subprocess.call(
        cfg.CONF.agent.function_location+'/pip install flask', shell=True
    )
    if retval == 0:
        subprocess.call([cfg.CONF.agent.function_location + '/python', cfg.CONF.agent.function_location + '/' + function_id+'.py'])
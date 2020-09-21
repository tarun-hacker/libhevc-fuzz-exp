import os
import time 
import subprocess

fuzzer_path = os.path.dirname(os.path.realpath(__file__))   
p = None
try:
    while True:
        if (p is None) or (p.poll() is not None):
            print("Detected Program Termination ... \n\nRestarting")
            p = subprocess.Popen([os.path.join(fuzzer_path,"hevc_dec_fuzzer"),"corpus"])
            print("Started a new process with id: {}".format(p.pid))
except:
    if (p is not None) and (p.poll() is None):
        p.kill()
    
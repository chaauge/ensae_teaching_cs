"""
copy the documentation to the website
"""
import sys
import os
sys.path.append(os.path.abspath("../pyquickhelper/src"))
sys.path.append(os.path.abspath("../pyensae/src"))
sys.path.append(os.path.abspath("../ensae_teaching_cs/src"))
sys.path.append(os.path.abspath("../pymyinstall/src"))

from pyquickhelper.loghelper import fLOG
from pyquickhelper.jenkinshelper import JenkinsExt
from ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, engines_default

fLOG(OutputPrint=True)
fLOG("start")

js = JenkinsExt('http://localhost:8080/', None, None,
                fLOG=fLOG, engines=engines_default())

setup_jenkins_server(js,
                     overwrite=True,
                     delete_first=False,
                     location="d:\\jenkins\\pymy",
                     disable_schedule=False)

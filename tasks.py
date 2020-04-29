import logging

from subprocess import Popen, PIPE

from data import Result, Response
from settings import config

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def run_ansible(project, subproject, ref):
    log.info(f'Starting job for {project} {ref}')
    command = ['ansible-playbook', '-i', 'inventory.py',
               f'playbooks/recipes.yml', '-e', f'ref={ref}',
               '-e', f'project_to_deploy={project}',
               '-e', f'subproject_to_deploy={subproject}',
               '--tags=deploy']
    str_command = ' '.join(command)
    log.info(f'Command will be {str_command}')
    p = Popen(command,
            stdout=PIPE,
            stderr=PIPE,
            cwd=config.working_dir_for_ansible,
            )
    p.wait()
    log.info(f'Done with {project}.{subproject} {ref}, return code: {p.returncode}')
    OUT = p.stdout.read().decode('utf-8')
    log.info(f'stdout is {OUT}')
    if p.returncode == 0:
        return Response(Result.Success, OUT)
    ERR = p.stderr.read().decode('utf-8')
    log.info(f'and stderr is {ERR}')
    OUT += "\nSTDERR:\n" + ERR
    return Response(Result.Failure, OUT)

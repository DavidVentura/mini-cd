from subprocess import Popen, PIPE

from data import Result, Response

ansible_path = '/home/david/git/labs-infrastructure/'


def run_ansible(playbook, tag):
    p = Popen(['ansible-playbook', f'playbooks/{playbook}.yml', '-e', f'tag={tag}'],
            stdout=PIPE,
            stderr=PIPE,
            cwd=ansible_path,
            )
    p.wait()
    OUT = p.stdout.read().decode('utf-8')
    if p.returncode == 0:
        return Response(Result.Success, OUT)
    OUT += "\nSTDERR:\n" + p.stderr.read().decode('utf-8')
    return Response(Result.Failure, OUT)


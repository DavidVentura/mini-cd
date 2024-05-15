.PHONY: all copy

all: dist/rq dist/ansible-playbook Makefile
	mkdir -p dist
	pip install -e .
	shiv -e 'mini_cd.web:main' -o dist/webserver -E .

dist/ansible-playbook: Makefile
	shiv -c ansible-playbook -o dist/ansible-playbook ansible==9.2.0 pyyaml boto3

dist/rq: Makefile
	shiv -c rq -o dist/rq rq

copy:
	scp dist/* cd:bin/

all: dist/rq dist/ansible-playbook
	mkdir -p dist
	pip install -e .
	shiv -e 'mini_cd.web:main' -o dist/webserver -E .

dist/ansible-playbook:
	shiv -c ansible-playbook -o dist/ansible-playbook ansible==2.9.18

dist/rq:
	shiv -c rq -o dist/rq rq

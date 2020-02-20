
Minimal continuous deployment API. Upon receiving a request to deploy, it will execute ansible based on the payload.

Accepted requests get put on a redis queue, and are drained/executed by workers.

The output of the work is available as the task result.

You can "scale" the workers to match your needs by enabling/starting more workers (`systemctl start worker@1 .. worker@n`).

# Requirements:

* Python3.5+
* Redis
* Ansible

(see requirements.txt)

# Usage 
There are only three routes:

```
/deploy/<string:repo>/<string:tag>, methods=['POST']
/queue/<string:job_id>, methods=['GET']
/job_result/<string:job_id>, methods=['GET']
```

You submit work to `deploy` and get redirected to wait on `queue` and `job_result`.

```
$ http localhost:8080/deploy/recipes/0.1
HTTP/1.1 202 ACCEPTED
Location: http://localhost:8080/queue/cc9fee61-f00c-4edf-9379-6e62557fbfa2
```

```
$ http http://localhost:8080/queue/cc9fee61-f00c-4edf-9379-6e62557fbfa2
HTTP/1.1 303 SEE OTHER
Location: http://localhost:8080/job_result/cc9fee61-f00c-4edf-9379-6e62557fbfa2
```

```
$ http http://localhost:8080/job_result/cc9fee61-f00c-4edf-9379-6e62557fbfa2
HTTP/1.1 200 OK

PLAY [recipes] ************************************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************************************************************************************
ok: [192.168.20.116]

TASK [ensure tag is set] **************************************************************************************************************************************************************************************************************************************
skipping: [192.168.20.116]

TASK [stat frontend] ******************************************************************************************************************************************************************************************************************************************
ok: [192.168.20.116]

TASK [stat backend] *******************************************************************************************************************************************************************************************************************************************
ok: [192.168.20.116]

TASK [deploy frontend] ****************************************************************************************************************************************************************************************************************************************
ok: [192.168.20.116]

TASK [deploy backend] *****************************************************************************************************************************************************************************************************************************************
ok: [192.168.20.116]

TASK [stat frontend] ******************************************************************************************************************************************************************************************************************************************
ok: [192.168.20.116]

TASK [stat backend] *******************************************************************************************************************************************************************************************************************************************
ok: [192.168.20.116]

TASK [restart backend when updated] ***************************************************************************************************************************************************************************************************************************
skipping: [192.168.20.116]

TASK [ensure frontend dir exists] *****************************************************************************************************************************************************************************************************************************
ok: [192.168.20.116]

TASK [update frontend when updated] ***************************************************************************************************************************************************************************************************************************
skipping: [192.168.20.116]

PLAY RECAP ****************************************************************************************************************************************************************************************************************************************************
192.168.20.116             : ok=8    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

```

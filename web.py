import os
import json

from settings import config
from data import Result, Response
from tasks import run_ansible

from flask_api import FlaskAPI, status
from flask import url_for, make_response
from waitress import serve
from redis import StrictRedis
from rq import Queue as Rqueue

app = FlaskAPI(__name__)
q = Rqueue(connection=StrictRedis())


@app.route("/deploy/<string:repo>/<string:tag>", methods=['POST', 'GET'])
def deploy(repo, tag):
    repo = repo.lower()
    job = q.enqueue(run_ansible, config.repo_mappings[repo], tag)
    job_key = job.key.decode('utf-8').lstrip('rq:job:')
    url = url_for('get_queue', job_id=job_key, _external=True)
    response = make_response()
    response.headers['Location'] = url
    return response, status.HTTP_202_ACCEPTED


@app.route("/queue/<string:job_id>", methods=['GET'])
def get_queue(job_id):
    job = q.fetch_job(job_id)
    response = make_response()
    if job is None:
        return "", status.HTTP_400_BAD_REQUEST

    if not job.get_status() in ['finished', 'failed']:
        return "", status.HTTP_200_OK
    else:
        url = url_for('get_status', job_id=job_id, _external=True)
        response.headers["Location"] = url
        return response, status.HTTP_303_SEE_OTHER


@app.route("/job_result/<string:job_id>", methods=['GET'])
def get_status(job_id):
    job = q.fetch_job(job_id)
    if job is None:
        return "", status.HTTP_400_BAD_REQUEST
    if job.is_failed:
        return {'Exception': job.exc_info}, status.HTTP_406_NOT_ACCEPTABLE

    result = job.result.result
    msg = f'<pre>{job.result.message}</pre>'
    if result == Result.Failure:
        return msg, status.HTTP_400_BAD_REQUEST

    return msg, status.HTTP_200_OK


if __name__ == "__main__":
    serve(app)

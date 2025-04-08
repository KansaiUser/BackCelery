# Background Tasks

- Basic

Call
```bash
$ uvicorn main:app --reload
```

Initiate a job in the http://127.0.0.1:8000/docs page and you will get the ID and then call the `/task-status` endpoint 

and check the file `log.txt`
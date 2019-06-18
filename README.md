# rjob
Dummy simple remote task executor

# Description

Upload local directory to remote servers, executes tasks and collects
results back to local host

Requires at least SystemD 236 on the target host

## Auto generated environment variables

|Environment variable| Meaning                               |
|--------------------|---------------------------------------|
| `RESULT`           | Destination directory                 |
| `DEPLOYMENT_NUM`   | Total number of deployments (servers) |
| `DEPLOYMENT_INDEX` | Deployment index                      |
# rjob

![PyPI - License](https://img.shields.io/pypi/l/rjob.svg)
![PyPI](https://img.shields.io/pypi/v/rjob.svg)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/rjob.svg)
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=4UKBSN5HVB3Y8&source=url)

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
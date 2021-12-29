# PythonFakeVisitos

Screen shot of IP logger site:
[![N|Solid](https://github.com/8-DK/PythonFakeUrlVisitors/raw/main/test/iplogger.JPG)](https://nodesource.com/products/nsolid)
## Features

- Add multiple proxy server list.
- Add multiple user agents.
- Choose random proxy from list
- Change timeout for each request

This script choose random proxy from list and using this proxy visit to given URL in infinite loop. This will create unique users visit to given URL.

## Requirements

This script use requests module in python which you have to install using pip.
```sh
pip install requests
```
## How to use 

Add costume user agents to user_agents.txt file.
Add user proxy server IP to to proxy_list.txt file.
run script:
```sh
python fakevisitor.py
```

## License
MIT

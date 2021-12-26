# PythonFakeVisitos

Screenshot of IP logger site:
[![N|Solid](https://github.com/8-DK/PythonFakeUrlVisitors/raw/main/test/iplogger.JPG)](https://nodesource.com/products/nsolid)
## Features

- Add multiple proxy server list.
- Add mulptile user ajents.
- Choose randome proxy from list
- Change timeout for each request

This script choose randome proxy from list and using this proxy visite to given URL in infinite loop. This will create unique users visite to given URL.

## Requirements

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.
```sh
pip install requests
```
## How to use 

Add user custome user ajents to user_agents.txt file.
Add user proxy server IP to to proxy_list.txt file.
run script:
```sh
python fakeVisitors.py
```

## License
MIT

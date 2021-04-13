Raspberry device client

# install
```
sudo apt install python3
sudo apt install python3-pip
git clone git@github.com:Crtrpt/raspd.git
cd raspd
pip3 install -r requirements.txt
```

# run test 
```
python3 -m unittest discover -s ./tests/ -p "*test.py"
```

## application layer protocol

report  device capability
```
{
  "action": "report",
  "payload": {
      cpu_usage_rate: 0.2,
      memery_usage_rate: 0.8
  }
}
```

report  capability data
```
{
  "action": "report",
  "payload": {
      cpu_usage_rate: 0.2,
      cpu_usage_rate: 0.8
  }
}
```

read   capability data
```
{
  "action": "read",
  "payload": [
      "cpu","cpu_temp"
  ]
}
```

set capability config
```
{
  "action": "config",
  "payload": [
      "key":"value",
      "key2":"value2"
  ]
}
```

remote exec code
```
{
  "action": "exec",
  "payload": "exec some code from remote"
}
```
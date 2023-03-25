# ip-monitor
/etc/systemd/system/ip_monitor.service
```
[Unit]
Description=IP Monitor Service
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 ip_monitor.py
WorkingDirectory=/opt/ip_monitor/

StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=my_service

[Install]
WantedBy=multi-user.target
```
.bashrc

```bash
function fun1()
{
   good_ip="89.40.4.133"
   ip=$(curl -s localhost:5000)
   if [[ "$ip" == "$good_ip" ]]
   then
           echo -e "\e[36m$ip\e[0m"
   else
           echo -e "\e[31m$ip\e[0m"
   fi
}


export PS1="\$(fun1) \[\e[32m\]\w \[\e[91m\]\$(parse_git_branch)\[\e[00m\]$ "
```

Python file:::
import json
json_example = open('json_example.json').read()
print(json_example)
json_dict = json.loads(json_example)
int_name = json_dict["ietf-interfaces:interface"]["name"]
int_name


***json_example.json***
{
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet2",
        "description": "Wide Area Network",
        "enabled": true,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.0.2",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

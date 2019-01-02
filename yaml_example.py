Python file:::
import yaml
yaml_example = open('yaml_example.yaml').read()
print(yaml_example)
yaml_dict = yaml.load(yaml_example)
int_name = yaml_dict["ietf-interfaces:interface"]["name"]
int_name


*** yamle_example.yaml***
ietf-interfaces:interface:
  name: GigabitEthernet2
  description: Wide Area Network
  enabled: true
  ietf-ip:ipv4:
    address:
    - ip: 172.16.0.2
      netmask: 255.255.255.0

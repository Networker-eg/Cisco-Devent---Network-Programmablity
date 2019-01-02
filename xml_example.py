Python file:::
import xmltodict
xml_example = open('xml_example.xml').read()
print(xml_example)
xml_dict = xmltodict.parse(xml_example)
int_name = xml_dict["interface"]["name"]
intname


***xml_example.xml file is as below***
<?xml version="1.0" encoding="UTF-8" ?>
<interface xmlns="ietf-interfaces">
  <name>GigabitEthernet2</name>
  <description>Wide Area Network</description>
  <enabled>true</enabled>
  <ipv4>
    <address>
      <ip>172.16.0.2</ip>
      <netmask>255.255.255.0</netmask>
    </address>
  </ipv4>
</interface>

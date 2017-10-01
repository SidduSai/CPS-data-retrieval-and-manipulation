from requests.auth import HTTPBasicAuth
from historian import PiWebAPIClient

client = PiWebAPIClient("d8cf2232", 443, "piwebapi",  HTTPBasicAuth("Administrator", ""))

print(client.get_range("*-1d", None, "D8CF2232", "SWAT_SUTD:RSLinx Enterprise:P4.HMI_LIT401.Pv", True))
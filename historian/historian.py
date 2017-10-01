import requests
import csv

# @ToDo
# Update/Edit Data
# Push Automatically

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class InvalidAuth(Exception):
	def __init__(self, message, errors):
		super(InvalidAuth,self).__init__(message)
		self.errors = errors

class PiWebAPIClient:

	def __init__(self, host, port, path, auth):
		self.host = host
		self.port = port
		self.path = path

		self.auth = auth

		self.address = "https://%s:%d/%s" %(host, port, path)

		self.tags = {}
		self.tag_names = set()
		self.server_webid = {}

		self.check_auth()
		self.load_tags()

	def check_auth(self):
		response = requests.get(self.address, auth=self.auth, verify=False)
		if response.status_code == 401:
			raise InvalidAuth("Invalid Auth Error")

	def load_tags(self):
		response = requests.get(self.address+"/dataservers", auth=self.auth, verify=False)


		data = response.json()

		for item in data["Items"]:
			self.server_webid[item["Name"]] = item["WebId"]
			link=item["Links"]["Points"]
			response = requests.get(link, auth=self.auth, verify=False)
			data = response.json()

			for point in data["Items"]:
				name, data_type, recorded, value, endvalue = point["Name"], point["PointType"], point["Links"]["RecordedData"], point["Links"]["Value"], point["Links"]["EndValue"]

				self.tag_names.add(name)

				store = {}
				store["data_type"] = data_type
				store["recorded"] = recorded
				store["value"] = value
				store["endvalue"] = endvalue

				self.tags[item["Name"]] = self.tags.has_key(item["Name"]) and self.tags[item["Name"]] or {}
				self.tags[item["Name"]][name] = store

	def get_dataservers(self):
		return self.tags.keys()

	def get_all_tags(self):
		return list(self.tag_names)

	def get_tags(self, server):
		if server not in self.tags:
			return "This DataServer doesn't exist"
		return self.tags[server].keys()

	def get_server_webids(self, server):
		return self.server_webid

	# Functions operating on single tags

	def get_range(self, start, end, server, tag, save_as_csv=False, filterex=None):

		if server not in self.tags:
			return "This DataServer doesn't exist"
		if tag not in self.tags[server]:
			return "This Server Doesn't Have This Tag"

		path =self.tags[server][tag]["recorded"]

		output = []

		fname = "%s-%s-%s-%s.csv"%(server,tag,start,end)

		while True:

			response = requests.get(path, params={"startTime": start, "endTime": end, "maxCount": 1000, "filterExpression": filterex}, verify=False, auth=self.auth)

			data = response.json()

			# Empty
			if "Items" not in data or not data["Items"]:
				break

			# Last Item
			if len(data["Items"]) == 1 and data["Items"][0]["Timestamp"] == start:
				break

			for item in data["Items"]:
				if item["Timestamp"]==start:
					continue
				output.append((item["Timestamp"], item["Value"]))

			start=data["Items"][-1]["Timestamp"]

		if save_as_csv:
			with open(fname, "wb") as out:
				csv_out = csv.writer(out)
				csv_out.writerow(["timestamp", "value"])
				for row in output:
					csv_out.writerow(row)
			return "Written to %s, contains %d rows"%(fname, len(output))
		else:
			return output


	def get_current_value(self, server, tag):
		if server not in self.tags:
			return "This DataServer doesn't exist"
		if tag not in self.tags[server]:
			return "This Server Doesn't Have This Tag"

		current_value_link = self.tags[server][tag]["value"]
		response = requests.get(current_value_link, auth=self.auth, verify=False)

		return response.json()['Value'], response.json()['Timestamp']


	def get_end(self, server, tag):
		if server not in self.tags:
			return "This DataServer doesn't exist"
		if tag not in self.tags[server]:
			return "This Server Doesn't Have This Tag"

		current_value_link = self.tags[server][tag]["endvalue"]
		response = requests.get(current_value_link, auth=self.auth, verify=False)

		return response.json()['Value'], response.json()['Timestamp']


	# Functions that operate on Multiple Tags

	def get_ranges(self, start, end, server, tags, save_as_csv=False, filterex=None):
		result = {}
		for tag in tags:
			result[tag] = self.get_tags(start, end, server, tag, save_as_csv, filterex)
		return result

	def get_current_values(self, server, tags):
		result = {}
		for tag in tags:
			result[tag] = self.get_current(server, tag)
		return result

	def get_ends(self, server, tags):
		result = {}
		for tag in tags:
			result[tag] = self.get_end(server, tag)
		return result

	def search_query(self, q, scope=None, fields= None, count=1000):
		pass

	def __str__(self):
		return "Connected to %s" %(self.address)
import requests, threading, re

thr = int(input("Threads: "))

def serang():

	while True:		try:

			headers = {

			    'authorization': '{"DeviceId":"b7e1f8640a293dbc21eafe86e1015d4c","GoogleId":"","FacebookId":"","Token":"gCUxHbW11M4xXQz5oYomUDtuMfWE8k2g","Timestamp":1655072719,"Hash":"28a2d60c255dbc3950cb23b725648052286f158d"}',

			    'use_response_compression': 'true',

			    'Accept-Encoding': 'gzip',

			    'Host': 'kitkabackend.eastus.cloudapp.azure.com:5010',

			}

			response = requests.get('http://kitkabackend.eastus.cloudapp.azure.com:5010/round/finishv2/2', headers=headers)

			if response.status_code == 200:

				trof = response.text.split('"SkillRating":')[1].split(',')[0]

				print(f"Trof -> {trof}")

			else:

				print(f"[{response.status_code}] Failed")

		except Exception as e:

			pass

for _ in range(thr):

	t = threading.Thread(target=serang)

	t.start()

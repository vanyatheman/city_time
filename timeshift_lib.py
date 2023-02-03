import datetime

import requests


ABSTRACTAPI_URL = (
	'https://timezone.abstractapi.com/v1/current_time/?'
	'api_key=426964117ff54f6e8c11e34cf602a68e&location='
)

class AbstractAPI:
	"""Class for addressing to API."""
	
	def __init__(self):
		self.cities = []

	def fetch_city_data(self, city_name):
		city_data = requests.get(self.ABSTRACTAPI_URL+city_name).json()
		return {
			'gmt_offset': city_data['gmt_offset'],
			'name': city_name
		}

	def get_local_time(
		self,
		gmt_offset,
		current_utc_time=datetime.datetime.now(datetime.timezone.utc)
	):
		'''
	Get current time of a timezone.

	Parameters:
		- 'gmt_offset': timezone offset in hours from UTC time.
		- 'current UTC': current UTC time.
	'''
	return (current_UTC_time
			+ datetime.timedelta(hours=gmt_offset)).strftime('%H:%M')


class InMemoryAPIMock:
	def __init__(self, cities):
		self.cities = cities

	def fetch_city_data(self, city_name):
		if city_name in cities:
			return city_name.timezone
		else:
			print(f'City {city_name} is not found')
			city_data = requests.get(ABSTRACTAPI_URL + city_name).json()

			location = city_data['requested_location']
			print(f'City {location} is added')

		return {
			'gmt_offset': city_data['gmt_offset'],
			'name': city_name
		}	



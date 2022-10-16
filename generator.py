import random
from google.cloud import pubsub_v1
import time
from datetime import datetime
import json
import sys


class generator:
	def __init__(self, symbol, timeout, last_price):
		self.symbol = symbol
		self.timeout = timeout
		self.last_price = last_price

	def iterate(self):
		publisher = pubsub_v1.PublisherClient()
		topic_path = publisher.topic_path('dataform-demo-365207', 'stockdata')
		last_price = self.last_price
		record = {}
		while True:
			change_percent = random.randint(-15, 15)
			# every once in a while, we deliberately insert erronous record with price=0
			error = random.randint(0, 100)
			last_price = round(last_price / 100 * (100 + change_percent))

			record["timestamp"] = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
			record["symbol"] = self.symbol
			# every once in a while, we deliberately insert erronous record with price=0
			if error < 95:
				record["price"] = last_price
			else:
				record["price"] = 0
			json_record = json.dumps(record, indent=4)
			#print (json_record)			
			future = publisher.publish(topic_path, json_record.encode("utf-8"))
			id = future.result(None)
			print(str(id))
			time.sleep(self.timeout)


def main(symbol, timeout):
	last_price = random.randint(10, 100)
	# First argument is the stock symbol and the second is interval between iterations

	g = generator(symbol, timeout, last_price)
	g.iterate()


if __name__ == "__main__":
	main(sys.argv[1], int(sys.argv[2]))

import csv
import re
def main():
	# Only select data that has the following location. 
	location = ["Bhutan", "Bumthang", "Chhukha", "Dagana", "Gasa", "Haa", "Lhuentse", 
		"Mongar", "Paro","Pema Gatshel", "Punakha", "Samdrup Jongkhar", "Samtse", "Sarpang", 
		"Thimphu", "Thrashigang", "Trashiyangtse", "Trongsa", "Tsirang", "Wangdue Phodrang", 
		"Zhemgang", "Phuentsholing"]

	# Read the file from raw_data folder and write in cleaned_data folder
	with open('./CSVdata/raw_data/20-28Dec.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		with open('./CSVdata/cleaned_data/clean_20-28Dec.csv','w') as clean_csv:
			for row in csv_reader: 
				data_location = row[5].title()

				# Check to see if the location in the data match any in the location array. 
				if any(word in data_location for word in location):
					# Delete the Bhutan appearing after a Dzongkhag name
					if "Bhutan" in data_location: 
						final_location = data_location.replace("Bhutan", "")

						# Some locations have only Bhutan as the location. Need to add location back. 
						if final_location == "":
							final_location = data_location.replace(" ", "Bhutan")

						else: 
							# This removes all special characters except for letters and space. 
							final_location = re.sub('[^A-Za-z0-9]+', '', final_location)

					# remove special characters that messes the CSV
					tweet_text = re.sub('[^A-Za-z0-9]+', ' ', row[1])
					tweet_text = tweet_text[1:] # remove the first letter which is always b. 
					hash_tags = re.sub('[^A-Za-z0-9]+', ' ', row[3])
					username = re.sub('[^A-Za-z0-9]+', ' ', row[2])
					username = username[1:] # remove the first letter which is always b.


					data = "{date_time},{tweet_text},{username},{hash_tags},{follower_count},{location} \n".format(
						date_time = row[0],
						tweet_text = tweet_text,
						username = username,
						hash_tags = hash_tags,
						follower_count = row[4],
						location = final_location)
					
					print(data)
					print("\n")
					clean_csv.write(data)
					

if __name__ == '__main__':
	main()




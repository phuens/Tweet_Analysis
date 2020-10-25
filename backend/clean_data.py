import csv
import re
def main():
	with open('./CSVdata/20-28Dec.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		# Only select the data that has the following location. 
		location = ["Bhutan", "Bumthang", "Chhukha", "Dagana", "Gasa", "Haa", "Lhuentse", 
		"Mongar", "Paro","Pema Gatshel", "Punakha", "Samdrup Jongkhar", "Samtse", "Sarpang", 
		"Thimphu", "Thrashigang", "Trashiyangtse", "Trongsa", "Tsirang", "Wangdue Phodrang", 
		"Zhemgang", "Phuentsholing"]


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
						# print(row[5], final_location)

					else: 
						# This removes all special characters except for letters and space. 
						location = re.sub('[^A-Za-z0-9]+', '', final_location)
						print(location)



if __name__ == '__main__':
	main()

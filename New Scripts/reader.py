import serial
import dataParser
import filesManager
import datetime
from picamera import PiCamera

date = datetime.date.today()

ser = serial.Serial('/dev/ttyACM0', 9600)
s = [0]
time = str(datetime.datetime.now())
camera = PiCamera()

values = []
counter = 0
n = 10  # liczba odczytow do sredniej

#tworzenie folderu i pliku z danymi

print('Czy stworzyc folder? [Y/N]:')
createFolder = input()
if createFolder.upper() == 'Y':
	folderPath = filesManager.createFolder('Archive')
else:
	folderPath = '/home/pi/Desktop/Archive/' + str(date)

print('Badanie z podgladem [Y]:\nBadanie bez podgladu [N]\nBadanie reczne [R]')
examinationType = input()

print('Wprowadz nazwe badania: ')
recordName = input()# Nazwa badania

recordsTxt = open(filesManager.createTxtFile(recordName, folderPath), 'a')
filesManager.writeHeader(recordsTxt, recordName)

# temporaryCounter = 0  # Konczenie petli po 100 odczytach FOR TEST ONLY!!!!
if examinationType.upper() != 'N':
	camera.start_preview(fullscreen=False, window=(20,20,640,480))

camera.start_recording(folderPath+"/Videos/"+time+".h264")

temporaryCounter = 0
readingNo = 0 #licznik dla badania 'recznego'

try:

	while True:

		if examinationType == 'Y' or examinationType == 'N':
			temporaryCounter = 0
		
		if temporaryCounter < 1:
			pass
		else:
			print('Nacisnij enter zeby wykonac odczyt')
			waitForResponse = input()
			temporaryCounter = 0
		
		

		read_serial = ser.readline()
		s[0] = ser.readline()

		lista = dataParser.splitter(s[0])

		if counter < n+1:

			values.append(lista)

		else:

		# Odczyt sredniej z <n> wartosci i zapis do pliku

			
		
			content = str(dataParser.readValues(values, n))

			if examinationType == 'R':
				readingNo += 1
				print('Odczyt nr: '+str(readingNo))
				filesManager.writeToTxtFile('Odczyt nr: '+str(readingNo), recordsTxt)

			print(dataParser.readValues(values, n))
			filesManager.writeToTxtFile(content, recordsTxt)

			counter = 0
			values = []

			if examinationType == 'R':
				temporaryCounter += 1 

			camera.annotate_text=("%s | %s" %(recordName, content))

		counter += 1
	
except KeyboardInterrupt:
	print('\nBadanie zakonczone')
	recordsTxt.close()
	if examinationType.upper != 'N':
		camera.stop_preview()
	camera.stop_recording()
	
		

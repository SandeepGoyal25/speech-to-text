# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
path = open('F:\Python\Git Practice\projects\Proposal JNU_Sandeep Goyal_200810147441.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 2nd page.
from_page = pdfReader.getPage(2)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
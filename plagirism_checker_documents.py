import PyPDF2
from PyPDF2.utils import PdfReadError
import docx

import magic

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import sys
import math




def pdfReader(filename): # use better library if found

    try:
        pdfFileObject = open(filename,'rb')
        
    except IOError as e:
        print("Failed to open file, ",e)

    try:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        #handling warning
    except PdfReadError as e:
        print(e)
        sys.exit(1)
    
    
    num_of_pages = pdfReader.numPages
    count = 0
    text = ""

    while count<num_of_pages:
        pageObject = pdfReader.getPage(count)
        text += pageObject.extractText()
        count +=1

    if text != "":
        text = text
    else:
        pass #read scanned pdfs


    tokenize_text = word_tokenize(text)
    
    return tokenize_text


def docxReader(filename):

    try:
        document = docx.Document(filename)
        
    except IOError as e:
        print("Failed to open file, ",e)

    fullText = []

    for paragraph in document.paragraphs:
        fullText.append(paragraph.text)
    
    return fullText


def txtReader(filename):

    try:
        textFile = open(filename,'r')
        
    except IOError as e:
        print("Failed to open file, ",e)

    return textFile.readlines()


def getNormalizeDocxText(listOfParagraphs):

    word_list = []
    paragraph_words_list = []
    character_list = []
    
    for paragraph in listOfParagraphs:
        if paragraph == '':
            continue
        
        for character in paragraph:

            if character.isalnum():
                character_list.append(character)     
            elif len(character_list)>0:
                word = "".join(character_list)
                word = word.lower()
                paragraph_words_list.append(word)
                character_list = []
                
        if len(character_list)>0:
            word = "".join(character_list)
            word = word.lower()
            paragraph_words_list.append(word)

    word_list.extend(paragraph_words_list)

    return word_list


def getNormalizeText(listOflines):

    wordlist = []
    character_list = []

    for line in listOflines:
        for character in line:

            if character.isalnum():
                character_list.append(character)
            elif len(character_list)>0:
                word = "".join(character_list)
                word = word.lower()
                wordlist.append(word)
                character_list = []

        if len(character_list)>0:
            word = "".join(character_list)
            word = word.lower()
            wordlist.append(word)

    return wordlist


def getNormalizeTextPdf(listOfWords):

    word_list = [word.lower() for word in listOfWords]

    return word_list


def getValidateWords(wordList):

    punctuations = ['(',')',';',':','[',']',',','.','-','_','&','|']
    stop_words = stopwords.words('english')

    validate_wordList = []

    for word in wordList:
        if (word not in punctuations) and (word not in stop_words):
            validate_wordList.append(word)

    return validate_wordList


def getPdfDataWrapper(filename):

    word_list = pdfReader(filename)
    
    normalized_wordlist = getNormalizeTextPdf(word_list)

    validated_wordlist = getValidateWords(normalized_wordlist)

    return validated_wordlist


def getDocxDataWrapper(filename):

    list_of_paragraphs = docxReader(filename)
    
    normalized_wordlist = getNormalizeDocxText(list_of_paragraphs)
    
    validated_wordlist = getValidateWords(normalized_wordlist)
    
    return validated_wordlist



def getTextDataWrapper(filename):

    list_of_lines = txtReader(filename)

    normalized_wordlist = getNormalizeText(list_of_lines)

    validated_wordlist = getValidateWords(normalized_wordlist)

    return validated_wordlist


def getDocumentType(filename):

    try:
        
        documentTypeString = magic.from_file(filename)

        if "PDF document" in documentTypeString:
            return "pdf"
        elif "Microsoft Word" in documentTypeString:
            return "docx"
        elif "ASCII text" in documentTypeString:
            return "txt"
        else:
            return None

    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    

def SuitableDocReader(filename,docType):

    dic_documentFuncs = {"pdf":getPdfDataWrapper,"docx":getDocxDataWrapper, \
                         "txt":getTextDataWrapper}

    return dic_documentFuncs[docType](filename)



def count_frequency(wordlist):

    D = {}

    for word in wordlist:

        if word  in D:
            D[word]+= 1
        else:
            D[word] = 1

    return D


def inner_product(frequencyDict1,frequencyDict2):

    sum = 0.0

    for word in frequencyDict1:
        if word in frequencyDict2:
            sum += frequencyDict1[word]*frequencyDict2[word]

    return sum


def getVectorAngle(frequencyDict1,frequencyDict2):

    numerator = inner_product(frequencyDict1,frequencyDict2)

    denominator = math.sqrt(inner_product(frequencyDict1,frequencyDict1) * \
                            inner_product(frequencyDict2,frequencyDict2))

    return math.acos(numerator/denominator)


def DocumentDistance():

    document1 = input("\nEnter first file name : \n")

    document1_type = getDocumentType(document1)

    if document1_type != None:
        print("\n"+str(document1)+" is a valid '"+str(document1_type)+ \
                                                          "' document.")
    else:
        print("\n"+str(document1)+" is not a valid document.")
        sys.exit(1)
        
    print("\nSuitable document type for matching : '" + \
                                       str(document1_type)+"'")
    document2 = input("\nEnter second file name : \n")

    document2_type = getDocumentType(document2)

    if document2_type != None:
        print("\n"+str(document2)+" is a valid '"+str(document2_type) \
                                                        +"' document.")
    else:
        print("\n"+str(document2)+" is not a valid document.")
    
    document1_wordlist = SuitableDocReader(document1,document1_type)
    document2_wordlist = SuitableDocReader(document2,document2_type)

    document1_freq_mapping = count_frequency(document1_wordlist)
    document2_freq_mapping = count_frequency(document2_wordlist)
    
    document_distance = getVectorAngle(document1_freq_mapping, \
                                        document2_freq_mapping)

    return document_distance
    

def PlagiarismCalculator():

    document_distance = DocumentDistance()

    plagiarism_percent = (1-(document_distance/1.57))*100

    return (document_distance,plagiarism_percent)


def PlagiarismInit():

    for i in range(26):
        print('*',end='')

    print('PLAGIARISM CALCULATOR',end='')

    for i in range(26):
        print('*',end='')

    print("\n\nSupported Document Files : .txt(ASCII),.pdf,.docx")

    print("\n\nNote: Same Document Type Files maps better output.")


def PlagiarismCalcWrapper():

    PlagiarismInit()

    (DocumentDistance,PlagiarismPercentage)= PlagiarismCalculator()

    print("\nApproximate Document Distance = %.2f"%DocumentDistance)
    print("Approximate Plagiarism Percent = %.2f"%PlagiarismPercentage)


def main():
    
    PlagiarismCalcWrapper()


if __name__ =='__main__':
    main()
    
'''
print(len(getPdfDataWrapper('Computer Graphics.pdf')))
print(len(getDocxDataWrapper('Computer Graphics.docx')))
print(len(getTextDataWrapper('Computer Graphics.txt')))
print(SuitableDocReader('Computer Graphics.docx',getDocumentType('Computer Graphics.docx')))


print(count_frequency(SuitableDocReader('Computer Graphics.docx',getDocumentType('Computer Graphics.docx'))))
print(count_frequency(SuitableDocReader('Computer Graphics.txt',getDocumentType('Computer Graphics.txt'))))
print(count_frequency(SuitableDocReader('Computer Graphics.pdf',getDocumentType('Computer Graphics.pdf'))))
'''

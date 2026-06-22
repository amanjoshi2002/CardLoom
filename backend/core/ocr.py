import easyocr

# reader = easyocr.Reader(['en'])
# result = reader.readtext("2.jpg")

# for item in result:
#     print(item[1])



def ocr_predict(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    extracted_text = []
    for item in result:
        extracted_text.append(item[1])
    
    return extracted_text
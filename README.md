# recognise_and_translate
Recognize Han Zi and translate to english (python)

This project depends on Tesseract
which can be obtained here:
https://github.com/tesseract-ocr/tesseract/wiki

Also, you need the training data for your expected language, get it from here:
https://github.com/tesseract-ocr/tesseract/wiki/Data-Files

You would need to unzip the training data for your language to 
\Tesseract-OCR\tessdata\.traineddata

You would need to add Tesseract Binary to system path variable

## python packages
- Pillow
- pytesseract
- translate

## Test results

```
(venv) E:\work\python\translator\recognise_and_translate>python src\test\python\testbench.py
translate result:
你好可爱
you should be rated as top 10 cutest Chinese men

translate result:
可以陪我睡觉吗
Can I sleep with me?
```
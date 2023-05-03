
<h1>OCR Text Recognition with Pytesseract</h1>

<p>This is a simple Python script that uses the pytesseract library to perform OCR text recognition on an image. It reads an image file, extracts the text from it using pytesseract, and then saves the extracted text in a new text file.
Getting Started</p>
<h3>Prerequisites</h3>
<ul>
    <li>Python 3</li>
    <li>pytesseract</li>
    <li>Pillow (PIL)</li>
</ul>

<h3>Installation</h3>

<p>Install pytesseract library:<p>
    <code contenteditable >pip install pytesseract</code>
    
<p>Install Pillow (PIL) library:</p>
    <code>pip install Pillow</code>
    
<p>Install Tesseract OCR:</p>
    <code>sudo apt install tesseract-ocr</code>
    
    
<p>Download additional language data (if needed):</p>

<p>If you need to perform OCR on languages other than English, you may need to download additional language data. For example, to perform OCR on Russian text, you can download the rus.traineddata file from the tesseract-ocr/tessdata repository and move it to the tessdata folder in the tesseract-ocr installation directory.
</p>

<h3>Usage</h3>

<ul>
<li>Clone or download the repository.</li>
<li>Save the image you want to extract text from in the same directory as the script.</li>
<li>Open a terminal and navigate to the directory containing the script.</li>
</lu>

<hr>
<p>Run the script using the command:</p>
<code>python ocr.py</code>

<p>The extracted text will be saved in a new text file with the prefix "Result" followed by the name of the image file.</p>


import pdfkit
config = pdfkit.configuration(wkhtmltopdf = r'"C:\Users\Ronit Murpani\Downloads\wkhtmltox-0.12.6-1.mxe-cross-win64\wkhtmltox\bin\wkhtmltopdf.exe"')
pdfkit.from_file(r'C:\VIT IT 2020-2024\Major Project\Cryptocali-Major\templates\Experiment1.html', 'Experiment1.pdf', configuration = config, 
                options = {'--enable-local-file-access': None,'--run-script': 'enableTransparency.js'})  
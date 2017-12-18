# Goal of the tool

The goal is to create and modificate ISO 19139 metadata that are compatible with GeoNetwork

# Structure of the tool

The tool is divided in three parts:
* Direct creation of the metadata using a web form
* Upload of an already created metadata
* Creation of metadata using Excel

# Direct creation of the metadata using a web form
The creation of the metadata using the web form is the easiest way for the user to create its metadata.The code is composed of two main parts: First, the user is asked to fill the web form (it corresponds to the `index3.py` file). When the form is validated, it is processed (`XML_b2d.py`) and the metadata can be uploaded(`webapp.py`). To get further information, please see following sections.

## Structure of the web form – `index3.py`
The web form is created by combining different files:
* HTML template – The main structure of the web form is described in this file.
* Address book and the list of keywords: Formats, Subject of study, Project phase, Location and variables – This files may change over time and the administrator only needs to change these files to update the all Metadata tool

All these files are combined using the `index3.py` code. The template function of python is used. The fields to replace in the html template are designated thanks to the “$” [dollar] symbol. All the little files (format.csv, subject_study.csv, project_phase.csv, Contact.csv, variable.csv) are opened in `index3.py`; they are processed and gathered in a dictionary. As the dollar ($) symbol is used in the html template, any java script, containing this symbol had to be removed from the template but they have been added or combined with information of the little files in the dictionary.

## Processing of the form – `webapp.py` and `XML_b2d.py`
`Webapp.py`

The `webapp.py` code is used to collect the elements filled by the user in the template, launch the `XML_b2d.py` function in order to process and create the XML file and finally show the result to the user through an html interface. The collection of the elements is done very easily: the name of the elements in the html form and their respective description filled by the user can be recuperated. They are gathered in another dictionary. The `B2d_XML2.py` function is then launched to create the XML metadata using the elements of the new dictionary. Finally, an Html interface allows the user to download the created metadata.

`B2d_XML2.py`
The `B2d_XML2.py` function is used to process the XML template, and fill it with the information filled by the user in the html form. The XML template has been created in GeoNetwork so that the metadata follows the requirement of ISO 19139 and is compatible with GeOrchestra. To process it, the XML template is read and parse using the lxml module of python. This parsing has been chosen so that even if one structure element of the XML changes, the program still works. The parsed XML is then filled with the elements of the dictionary. The XML file is then saved on the server using the “short_title” as file name.

## Upload of data
When the user has created his metadata, he can join the respective data and upload it on the CDGP server. To do so, he has to click on the “validate” button. An html interface (`webbapp1.py`) appears. The user can upload the data. When he clicks on the “upload” button, the data and the metadata are gathered in a zip file. The user can see the results and download the created zip file by clicking on the Zip file logo (`data.py`)

# Upload of an already created metadata
The goal here is to upload an already created metadata in order to modify it.

`Upload.html`
This is the web interface allowing the user to upload its already created metadata. The required file format is XML. Only ISO 19139 metadata created using this tool are accepted. When the metadata is uploaded, the XML is processed using the upload1.py code and `XML_B2d2.py`function.

`XML_B2d2.py`
This function is used to parse the uploaded XML metadata. The parsing is done using the lxml module of python. All the information contained in the file are saved in different variables. They are then saved in a new dictionary (data).

`Upload1.py`
This code is combining all the information contained in different files. It is very similar to the index3.py
code. The only difference is the use of information from the XML which is used to complete the fields.
In particular, the code gathers the following files:
* A html template.
* The same little files (Contact, Formats, Subject of study, Project phase, Location and variables) are also opened
* The dictionary returned by the XML_B2d2.py function. This dictionary is completed with the information from the previous files, as was done in the `index3.py` code.

# Create metadata using excel tool
The goal is to create a large number of metadata all at once. This tool is especially interesting to create a large number of similar metadata. A documentation is available for the user on the excel tool page. The processing is done using the `excel2xml.py` code and the `B2d_XML2_excel.py` function. These codes are equivalent to the `webapp.py` program and the `B2d_XML2.py` function. Only small adjustments have been done to comply with the different way to enter information and the iteration applied.

`excel2xml.py`
This code is the equivalent of the webapp.py program. The information filled in the Excel template (saved in csv format) are gathered in a dictionary. The `B2d_XML2_excel.py` is launched in order to create the metadata. All the created metadata are gathered in a zip file that can be downloaded from the HTML page by clicking on the icon of the zip file.

`B2d_XML2_excel.py`
Equivalent to the `B2d_XML2_excel.py`, this function enables to create the metadata. The only
difference is the use of the iteration.

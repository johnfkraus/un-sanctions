# un-sanctions

Status: work in process.

Steps:

1.  Convert public XML file into a Pandas dataframe.

2.  Parse the comments for reference numbers.  Use the reference numbers to map sources (individuals, entities) to targets (other individual, entities).

3. Render a directed graph to show the relationships.

TODO:

Add interactive legend.  https://docs.bokeh.org/en/latest/docs/user_guide/annotations.html

Notes:

Downloaded updated UN Sanctions list from: https://scsanctions.un.org/resources/xml/en/consolidated.xml
Converted consolidated-202303.xml to consolidated-202303.json using https://codebeautify.org/xmltojson.
Also, converted xml to csv using same website.



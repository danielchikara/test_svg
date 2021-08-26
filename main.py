from lxml.etree import XMLParser,parse
import errno
import re
import os

try:
    os.mkdir('xml_target')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

with open('empresario_9-01.svg','r') as f:
    p = XMLParser(huge_tree=True)
    doc= parse(f,parser=p)
    svg= doc.getroot()
    list_g = svg.findall(".//{http://www.w3.org/2000/svg}g")
    
    for elem in list_g:
        if elem.find('[@id=\'Base_Niño_Americano_xA0_Image_1_\']'):
            print(elem)
            parent=elem.getparent()
            parent.remove(elem)
        if elem.find('[@id=\'Sombras_Niño_Americano_xA0_Image_1_\']'):
            print(elem)
            parent=elem.getparent()
            parent.remove(elem)
        if  elem.find('[@id=\'Color_Niño_Americano_xA0_Image_1_\']'):
            print(elem)
            parent=elem.getparent()
            parent.remove(elem)
    doc.write('xml_target/enterprise_storye_2.svg')






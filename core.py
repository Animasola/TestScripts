# -*- coding: cp1251 -*-

#windows-1251
import dbf

from x_parser import TechCardXml


tc_parser = TechCardXml(xml_path='..\XML_FILES\TP_S.xml')
tc_parser.init()




#print 'Arguments: %s' % str(sys.argv)
raw_input("Press Enter to continue...")


# Docs:
# https://docs.python.org/2/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.get
# http://pythonhosted.org//dbf/

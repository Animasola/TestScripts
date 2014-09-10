# -*- coding: utf-8 -*-
from xml.etree import ElementTree


class TechCardXml(object):

    def __init__(self, xml_path=''):
        self.documents = []
        self.relations_dump = []
        self.tree = ElementTree.parse(xml_path)
        self.root = self.tree.getroot()

    def parse_all_tp(self):
        for tp in self.root.findall('tp'):
            el_type, ref_id = None, None
            obozn, name = None, None
            tp_data = self.root.find(
                './/form[@id="%s"]' % tp.find('relation').attrib['ref'])
            for child in tp_data:
                if child.attrib['name'] == u'Обозначение':
                    obozn = unicode(child.attrib['value'])
                elif child.attrib['name'] == u'Тип документа':
                    name = unicode(child.attrib['value'])
                else:
                    continue
            for child in tp:
                self.documents.append({
                    'obozn': obozn,
                    'name': name,
                    'element_type': child.attrib['elementtype'],
                    'ref_id': child.attrib['ref'],
                })

    def grab_relations_dump(self):
        # OBOZN, TIP_DOC, ITEM_TYPE, ITEM_ID, REL_TYPE, EL_TYPE, REF_ID, MAT_REF_ID
        for document in self.documents:
            

    def init(self):
        self.parse_all_tp()
        self.grab_relations_dump()

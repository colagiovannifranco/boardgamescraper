from io import StringIO 
from lxml import etree


class Parser:
    
    xpath_celdas_nombre = "//table[@id='collectionitems']/tr/td[3]/div[2][contains(@id,'results_objectname')]"
    xpath_geek = "//table[@id='collectionitems']/tr/td[4]/text()"
    xpath_average = "//table[@id='collectionitems']/tr/td[5]/text()"
    xpath_voters = "//table[@id='collectionitems']/tr/td[6]/text()"
    
    def __init__(self, html):
        
        self.html = html
        self.tabla = []
        
        self.htmlparser = etree.HTMLParser()
        self.html_tree = etree.parse(StringIO(html), self.htmlparser)
                
    def clean_entero(self, string_entero):
        if "N/A" in string_entero:
            return
        else:
            return int(string_entero.replace('(','').replace(')',''))
    
    def clean_flotante(self, string_flotante):
        if "N/A" in string_flotante:
            return
        else: 
            return float(string_flotante.replace('\n','').replace('\t',''))
    
    def download_tabla(self):
        
        celdas_nombre = self.html_tree.xpath(self.xpath_celdas_nombre)

        name = []
        year_string = []
        
        for c in celdas_nombre:
            n = c.xpath("a/text()")
            name += n
            year = c.xpath("span/text()")
            if year:
                year_string += year
            else:
                year_string.append("N/A")

        geek_string = self.html_tree.xpath(self.xpath_geek)
        average_string = self.html_tree.xpath(self.xpath_average)
        voters_string = self.html_tree.xpath(self.xpath_voters)

        year = list(map(self.clean_entero,year_string))
        voters = list(map(self.clean_entero,voters_string))

        geek = list(map(self.clean_flotante,geek_string))
        average= list(map(self.clean_flotante,average_string))

        self.tabla = list(zip(name,year,geek,average,voters))
        return self.tabla
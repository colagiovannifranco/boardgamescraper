import scrapy
from items import GameItem

class GameListParser:
    
    xpath_celdas_nombre = "//table[@id='collectionitems']/tr/td[3]/div[2][contains(@id,'results_objectname')]"
    xpath_geek = "//table[@id='collectionitems']/tr/td[4]/text()"
    xpath_average = "//table[@id='collectionitems']/tr/td[5]/text()"
    xpath_voters = "//table[@id='collectionitems']/tr/td[6]/text()"
    
    def __init__(self, response):
        
        self.tabla = []
        
        self.html_tree = response.selector
                
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
            n = c.xpath("a/text()").getall()
            name += n
            year = c.xpath("span/text()").getall()
            if year:
                year_string += year
            else:
                year_string.append("N/A")

        geek_string = self.html_tree.xpath(self.xpath_geek).getall()
        average_string = self.html_tree.xpath(self.xpath_average).getall()
        voters_string = self.html_tree.xpath(self.xpath_voters).getall()

        year = list(map(self.clean_entero,year_string))
        voters = list(map(self.clean_entero,voters_string))

        geek = list(map(self.clean_flotante,geek_string))
        average= list(map(self.clean_flotante,average_string))

        self.tabla = list(zip(name,year,geek,average,voters))
        
        lista_item = []

        for i in self.tabla:
            game_item = GameItem(name = f'{i[0]}', year = i[1], geek = i[2], average = i[3], voters = i[4])
            lista_item.append(game_item)
        return lista_item

class GameSpider(scrapy.Spider):
    name = "games"
    start_urls = [f'https://boardgamegeek.com/browse/boardgame/page/{i}' for i in range(1, 1138)]

    def parse(self, response):
        p = GameListParser(response)
        return p.download_tabla()


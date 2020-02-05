import csv


tabla_completa = []

for i in range(1, 1138):
    print(f'bajando pagina {i}')
    r = Downloader(f'https://boardgamegeek.com/browse/boardgame/page/{i}')
    r.download_page()
    p = Parser(r.html)
    p.download_tabla()
    tabla_completa += p.tabla
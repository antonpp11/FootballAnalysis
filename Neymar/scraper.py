import requests
from bs4 import BeautifulSoup
import pandas as pd



class Scraper():
    def __init__(self, player_name, player_number):
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        self.years_season_dict = {
        "2013" : "ES1",
        "2014" : "ES1",
        "2015" : "ES1",
        "2016" : "ES1",
        "2017" : "FR1",
        "2018" : "FR1",
        "2019" : "FR1",
        "2020" : "FR1"
        }
        self.player_name = player_name
        self.player_number = player_number
        self.base_url = f"https://www.transfermarkt.com/{player_name}/leistungsdatendetails/spieler/{self.player_number}/plus/1?"

    def main(self):
        print(self.get_url_for_season(2017))

    def get_url_for_season(self, year):
        league = self.years_season_dict.get(str(year))
        return f"{self.base_url}saison={year}&verein=&liga=&wettbewerb={league}"
        


if __name__ == "__main__":
    neymar = Scraper("neymar", "68290")
    neymar.main()
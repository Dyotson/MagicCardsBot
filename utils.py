import pandas as pd
import requests
from bs4 import BeautifulSoup


class MagicCardsBot:
    def __init__(self, excel_file):
        print("Loading cards from Excel file...")
        self.cards = []
        self.prices = []
        self.card_df = pd.read_excel(excel_file)

    def load_cards(self):
        print("Loading cards...")
        self.cards = self.card_df["Link"].to_list()

    def get_cards_data(self):
        print("Getting cards prices...")
        for link in self.cards:
            r = requests.get(link)
            soup = BeautifulSoup(r.content, "html.parser")
            name = soup.find("h1", class_="productView-title").text
            price = soup.find("span", class_="price price--withoutTax").text
            print(f"{name} - {price}")
            self.prices.append(price)

    def create_dataframe(self):
        self.card_df["Price"] = self.prices
        self.card_df.to_excel("cards_prices.xlsx")

from utils import MagicCardsBot

CardsBot = MagicCardsBot("TestExcel.xlsx")
CardsBot.load_cards()
CardsBot.get_cards_data()
CardsBot.create_dataframe()

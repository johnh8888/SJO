import random

class DataFeed:

    def get_odds(self):

        # 模拟真实赔率API（可替换 Betfair / OddsAPI）
        return {
            "book1": {
                "home": round(random.uniform(1.6, 2.4), 2),
                "draw": round

import random

class DataFeed:

    def get_match_data(self):

        # 模拟真实xG（可替换API）
        return {
            "xg_home": round(random.uniform(1.2, 2.0), 2),
            "xg_away": round(random.uniform(0.8, 1.6), 2),

            "odds": {
                "home": round(random.uniform(1.6, 2.3), 2),
                "draw": round(random.uniform(2.8, 3.6), 2),
                "away": round(random.uniform(3.0, 5.0), 2)
            }
        }

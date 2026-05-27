def implied_prob(odds):

    return {k: 1 / v for k, v in odds.items()}


def detect_1x2_arbitrage(odds):

    inv = sum(1 / o for o in odds.values())

    if inv < 1:
        return {
            "type": "1X2 ARB",
            "profit": round((1 - inv) * 100, 2)
        }

    return None


def detect_edge(model_prob, odds):

    implied = implied_prob(odds)

    edges = {}

    for k in odds:
        edges[k] = model_prob[k] - implied[k]

    return edges

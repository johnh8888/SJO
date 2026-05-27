def model_prob(xg_home, xg_away):

    total = xg_home + xg_away

    return {
        "home": xg_home / total,
        "draw": 0.25,
        "away": xg_away / total
    }

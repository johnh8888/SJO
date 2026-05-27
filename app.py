from flask import Flask, render_template, jsonify

from data import DataFeed
from strategy import model_prob
from arbitrage import detect_1x2_arbitrage, detect_edge
from rl_agent import RLAgent

app = Flask(__name__)

feed = DataFeed()
agent = RLAgent()

bankroll = 1000


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def data():

    global bankroll

    d = feed.get_match_data()

    model = model_prob(d["xg_home"], d["xg_away"])

    arb = detect_1x2_arbitrage(d["odds"])
    edges = detect_edge(model, d["odds"])

    state = agent.state(edges)
    action = agent.act(state)

    pnl = 0

    if action == "BET":

        pnl = bankroll * 0.02 * max(edges["home"], 0)

    bankroll += pnl

    if arb:
        arb_msg = arb
    else:
        arb_msg = None

    return jsonify({
        "xg": {
            "home": d["xg_home"],
            "away": d["xg_away"]
        },
        "odds": d["odds"],
        "edges": edges,
        "rl_action": action,
        "arbitrage": arb_msg,
        "pnl": round(pnl, 2),
        "bankroll": round(bankroll, 2)
    })


if __name__ == "__main__":
    app.run(debug=True)

class StakeHistoryReport:
    def __init__(self, total_tx, breakdown, net, peak, low, volatility, history):
        self.total_transactions = total_tx
        self.breakdown = breakdown
        self.net_profit_loss = net
        self.peak_balance = peak
        self.lowest_balance = low
        self.volatility = volatility
        self.history = history
class StakeMonitor:
    def __init__(self, transactions_df):
        self.df = transactions_df

    def peak(self):
        if self.df.empty:
            return 0
        return self.df["balance_after"].max()

    def lowest(self):
        if self.df.empty:
            return 0
        return self.df["balance_after"].min()

    def volatility(self):
        if len(self.df) < 2:
            return 0
        return self.df["balance_after"].std()

    def changes(self):
        return self.df["balance_after"].diff().fillna(0).tolist()
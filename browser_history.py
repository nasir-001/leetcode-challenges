class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url: str) -> None:
        self.current_index += 1
        self.history = self.history[0: self.current_index]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.current_index = max(0, self.current_index-steps)
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        self.current_index = min(len(self.history)-1, self.current_index+steps)
        return self.history[self.current_index]

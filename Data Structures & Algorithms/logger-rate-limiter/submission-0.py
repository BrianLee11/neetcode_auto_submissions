class Logger:

    def __init__(self):
        self.dictionary_logger = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.dictionary_logger:
            # comes before the timeframe
            if timestamp < self.dictionary_logger[message]:
                return False
            # comes on or after the timeframe
            else:
                # update
                self.dictionary_logger[message] = timestamp + 10
                return True
        else:
            # first occurrence.
            self.dictionary_logger[message] = timestamp + 10
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

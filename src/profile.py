class Profile:
    def __init__(self, transport, freq, spread, code, bandwidth, tx):
        self.is_transport = transport
        self.frequency = freq
        self.spreading_factor = spread
        self.coding_rate = code
        self.bandwidth = bandwidth
        self.transmit_power = tx
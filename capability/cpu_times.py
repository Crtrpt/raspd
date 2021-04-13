import psutil

class cpu_times:
    def run(self):
        return psutil.cpu_times()
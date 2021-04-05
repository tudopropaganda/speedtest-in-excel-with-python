import os
import time
from datetime import datetime, timedelta

import pandas as pd
from speedtest import Speedtest

REPEAT_MODE = True  # If False will run only once
MINUTES_TO_RERUN = 15


class Speedometer(Speedtest):
    def __init__(self):
        super().__init__()

        self.timestamp = None
        self.download_speed_Mbps = None
        self.upload_speed_Mbps = None
        self.ping_ms = None
        self.provider = None
        self.ip = None
        self.mb_sent = None
        self.mb_received = None

    def run_speedtest(self):
        print('*** Connecting to Speedtest.net ***')
        print('1 | 2 --> Testing your DOWNLOAD speed... please wait')

        # Use superclass' methods to test the speeds
        self.download()

        print('2 | 2 --> Testing your UPLOAD speed... please wait\n')
        self.upload()

        # Define our custom parameters based on Speedtest's results
        # Basically converting results given in bits to mb
        self.timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.download_speed_Mbps = self.bit_to_mb(self.results.download)
        self.upload_speed_Mbps = self.bit_to_mb(self.results.upload)
        self.ping_ms = int(self.results.ping)
        self.provider = self.results.client.get('isp')
        self.ip = self.results.client.get('ip')
        self.mb_sent = self.bit_to_mb(self.results.bytes_sent)
        self.mb_received = self.bit_to_mb(self.results.bytes_received)

    def print_results(self):
        # Will print the results only in the terminal
        print('-' * 50)
        print(f"""
                Download:   {self.download_speed_Mbps} Mbps
                Upload:     {self.upload_speed_Mbps} Mbps
                Ping:       {self.ping_ms} ms
                Provider:   {self.provider}
            """)
        print('-' * 50)

    def export_data(self):
        # Export the results to a csv file
        # Create a new file with headers or append data in an existing one
        data = {
            'results': {'timestamp': self.timestamp,
                        'download_speed_Mbps': self.download_speed_Mbps,
                        'upload_speed_Mbps': self.upload_speed_Mbps,
                        'ping_ms': self.ping_ms,
                        'provider': self.provider,
                        'ip': self.ip,
                        'mb_sent': self.mb_sent,
                        'mb_received': self.mb_received}
        }

        df = pd.DataFrame.from_dict(data, orient="index")

        filename = 'database.csv'

        header = False if os.path.isfile(filename) else True
        df.to_csv(filename, mode='a', header=header, index=False)

        print(f'File {filename} has been {"created" if header else "updated"}.')

    @staticmethod
    def bit_to_mb(value):
        return round(value * (10 ** -6), 1)


def main():
    speedometer = Speedometer()
    speedometer.run_speedtest()
    speedometer.print_results()
    speedometer.export_data()


def keep_running():
    if REPEAT_MODE:
        while True:
            main()

            again = datetime.now() + timedelta(minutes=MINUTES_TO_RERUN)
            print(f'Sleeping for {MINUTES_TO_RERUN} minutes. Will run again at {again}')
            print('please keep this window open')
            time.sleep(MINUTES_TO_RERUN * 60)

    else:
        main()


if __name__ == '__main__':
    keep_running()

import argparse
import logging
from oanda_api import OandaAPI

def run_daily_generator(granularity, count):
    """
    Generate historical data files for Forex pairs.
    :param granularity: Granularity of the data (e.g., 'D', 'H1').
    :param count: Number of data points to fetch.
    """
    oanda = OandaAPI()
    all_pairs = oanda.get_all_forex_pairs()

    for pair in all_pairs:
        try:
            oanda.update_historical_data(pair, granularity=granularity, count=count)
            logging.info(f"Updated historical data for {pair} with granularity {granularity} and count {count}")
        except Exception as e:
            logging.error(f"Failed to update data for {pair}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate historical data files for Forex pairs.")
    parser.add_argument("--granularity", type=str, default="H1", help="Granularity of the data (e.g., 'D', 'H1').")
    parser.add_argument("--count", type=int, default=1000, help="Number of data points to fetch.")

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    run_daily_generator(args.granularity, args.count)

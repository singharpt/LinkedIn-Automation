import pickle
import os
from dotenv.main import load_dotenv
load_dotenv()

cache_filename = os.environ['CACHE_FILENAME']


class Cache:

    def __init__(self):
        self.cache = set()

    def get_cache(self):
        print("Reading the cache...")
        try:
            self.cache = pickle.load(open(cache_filename, "rb"))
        except (OSError, IOError) as e:
            pickle.dump(self.cache, open(cache_filename, "wb"))

    def run_cache_check(self, seen_email_list):
        """
        This function gets a list of emails available.
        It checks if the emails were mailed earlier.
        If yes, it filters the seen emails.
        Returns a list of all unseen emails.
        """

        self.get_cache()

        if not self.cache:
            return seen_email_list

        unseen_email_list = []

        for item in seen_email_list:
            if item['Email'] not in self.cache:
                unseen_email_list.append(item)

        return unseen_email_list

    def update_cache(self, unseen_email_list):
        """
        This function gets a list of emails available.
        Updates the current cache
        Stores the cache to the disk
        """

        print("Adding new emails to the cache...")
        for item in unseen_email_list:
            self.cache.add(item['Email'])

        print("Saving cache to the disk...")

        with open(cache_filename, 'wb') as fp:
            pickle.dump(self.cache, fp)

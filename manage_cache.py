import os
from dotenv.main import load_dotenv
load_dotenv()

# set the path of the cache file
script_dir = os.path.dirname(os.path.abspath(__file__))
cache_filepath = os.path.join(script_dir, "cache.txt")


class Cache:
    def __init__(self):
        self.cache = None

    def get_cache(self):
        print("Reading the cache...")
        try:
            with open(cache_filepath, 'r', encoding='utf-8') as rfile:
                self.cache = set([line.strip() for line in rfile])
                print(self.cache)
        except FileNotFoundError:
            self.cache = set()

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
        self.cache.update(item['Email'] for item in unseen_email_list)

        print("Saving cache to the disk...")
        with open(cache_filepath, 'w', encoding='utf-8') as wfile:
            for line in self.cache:
                wfile.write(line+'\n')

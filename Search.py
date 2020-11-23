# Import required modules
import requests
from datetime import date
import json
import re
from termcolor import colored
import sys


class Search():
    """Provides news to the user based on a keyword search from ALL AROUND THE GLOBE!!"""
    
    def keyword_input(self):
        """This function gets the keyword that the user wishes to search with.

            Args:
                self (obj): Instance of the Search class.

            Returns:
                user_choice (str): Keyword chosen by the user
        """

        # Ask the user to input the keyword that they want to search with
        self.user_choice = input("Enter your search term:\n>> ")
        # Return the user's choice
        return self.user_choice


    def json_news_search(self, keyword):
        """This function retrieves json data from News API with the keyword chosen by the user.

            Args:
                self (obj): Instance of the Search class.
                keyword (str): Keyword chosen by the user.

            Returns:
                json_data (dict): Contains status, totalResults and articles.
        """

        # Get's news based on the keyword!! Sorted by date with newest first and has language set to English
        url = "https://newsapi.org/v2/everything?q=+%s&sortBy=publishedAt&language=en&apiKey=da26c545082f4a15bea0275598e69c54" % keyword
        # Request to get the results from the API
        request = requests.get(url)
        # Store it as json data
        json_data = request.json()
        return json_data

    
    def formatted_data_search(self, data):
        """This function creates a final string that is formatted with the title of the headline, the source, the date it
            was published and a short description. It also makes the title, source, and date  GREEN.

            Args:
                self (obj): An instance of the Search class.
                data (dict): Results from the News API in json.
            
            Returns:
                text (str): Formatted string with the titles, source, date and description.
        """

        # Check whether the status of the API is ok
        if data["status"] == "ok":
            # Find how many articles there are with the users search
            num_of_articles = int(data["totalResults"])
            # Whichever is the minimum of 10 and the number of articles
            num_display = min(num_of_articles, 10)
            # Create an empty string that the title, source, date and description can be appended to
            text = ""
            # If there are no articles to display
            if num_display == 0:
                text += "* There is no news associated with your search."
                return text
            # If there are 1 - 10 articles to display
            else:
                # Create an index variable to traverse through the articles
                index = 0
                # Since index starts from 0, it must be less than the number of articles
                while index < num_display:
                    # Create an empty string to add the title, source and date to
                    title = ""
                    # Create an empty string to add the description to
                    description = ""
                    # Find the date from the json data
                    date_unformatted = data["articles"][index]["publishedAt"]
                    # Use RegEx to parse out the date
                    date_formatted_regex = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_unformatted)
                    # If a published date exists
                    if date_formatted_regex:
                        date_formatted = date(int(date_formatted_regex.group(1)), int(date_formatted_regex.group(2)), int(date_formatted_regex.group(3))).strftime("%B %d, %Y")
                    # If no published date exists
                    else:
                        date_formatted = "No date published"
                    # Add the title of the article, source of the article and the date to title in GREEN
                    title += colored("* " + data["articles"][index]["title"] + " - " + data["articles"][index]["source"]["name"] + " - " + date_formatted + "\n", "green")
                    # Add the title into text
                    text += title
                    # If there is a description available
                    if data["articles"][index]["description"]:
                        description += "\t - " + data["articles"][index]["description"] + "\n"
                        text += description
                    # If there are no descriptions available
                    else:
                        description += "\t - No description available.\n"
                        text += description
                    # Increment the index variable by 1
                    index += 1
                # Return the final text containing all the titles, sources, dates and descriptions
                return text
        # If the status of the server is not ok
        else:
            sys.exit("Server Status: %s | Oops this is awkward :( I'm trying to connect but it seems like the server is down... Please try again later" % colored(data["status"], "red"))
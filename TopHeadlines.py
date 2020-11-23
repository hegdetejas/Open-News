# Import required modules
import requests
from datetime import date
import json
import re
from termcolor import colored
import sys


class TopHeadlines():
    """Provides news to the user based on TopHeadlines from INDIA!!!"""

    def category_option(self):
        """This function takes user input and stores their selection for which Top Headline they would like to see out of:
                -Business
                -Entertainment
                -General
                -Health
                -Science
                -Sports
                -Technology

            Args:
                self (obj): Instance of TopHeadlines class.

            Returns:
                category_chosen (str): String representation of [1-7] which is the category chosen by the user.
        """

        # Ask the user which category they would like
        self.category_chosen = input("Select which category you would like headlines for:\n[1] Business\n[2] Entertainment\n[3] General\n[4] Health\n[5] Science\n[6] Sports\n[7] Technology\n>> ")
        # Check whether they input an integer
        try:
            # If the number is less than 1 or greater than 7
            if int(self.category_chosen) < 1 or int(self.category_chosen) > 7:
                print("Invalid option. Choose a category by selecting a number between [1-7] inclusive.")
                return self.category_option()
            # Valid number input is stored
            else:
                return self.category_chosen
        # If input is not an integer
        except ValueError:
            print("Invalid option. Choose a category by selecting a number between [1-7] inclusive.")
            return self.category_option()


    def json_news_headlines(self, option_number):
        """Get the json data from News API.

            Args:
                self (obj): Instance of TopHeadlines class.
                option_number (str): String representation of the option chosen by the user.

            Returns:
                json_data (dict): Contains status, totalResults and articles.
        """

        # Create a dictionary to pair the user input with the actual name of the category
        options = {"1" : "business", "2" : "entertainment", "3" : "general", "4" : "health", "5" : "science", "6" : "sports", "7" : "technology"}
        # Store the name of the category that the user chose
        chosen_option = options[option_number]
        # Gets INDIAN NEWS! WOOHOo
        url = "https://newsapi.org/v2/top-headlines?country=in&category=%s&sortBy=publishedAt&apiKey=da26c545082f4a15bea0275598e69c54" % chosen_option
        # Request to get the results from the API
        request = requests.get(url)
        # Store it as json data
        json_data = request.json()
        return json_data


    def formatted_data_headlines(self, json_data):
        """This function creates a final string that is formatted with the title of the headline, the date it was published
            and a short description. It also makes the titles and date in GREEN.

            Args:
                self (obj): An instance of the TopHeadlines class.
                json_data (dict): Results from the News API.
            
            Returns:
                text (str): Formatted string with the titles, date and description.
        """

        # When it is possible to retrieve data from the API
        if json_data["status"] == "ok":
            # Create an empty string to append all the text into
            text = ""
            # Create an empty index variable to help with traversing through stories
            index = 0
            # Traverse through the top 10 stories
            while index < 9:
                # Reset the title everytime a new story is found
                title = ""
                # Reset the description everytime a new story is found
                description = ""
                # The date is one of the elements of the dictionary
                date_unformatted = json_data["articles"][index]["publishedAt"]
                # Use RegEx to parse the date
                date_formatted_regex = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_unformatted)
                # If there is a matching date
                if date_formatted_regex:
                    date_formatted = date(int(date_formatted_regex.group(1)), int(date_formatted_regex.group(2)), int(date_formatted_regex.group(3))).strftime("%B %d, %Y")
                # If there is no date published
                else:
                    date_formatted = "No date published"
                # Add the date and the title of the article to string title and format it so the colour is GREEN
                title += colored("* " + json_data["articles"][index]["title"] + " - " + date_formatted + "\n", "green")
                # Add the title and date to the text
                text += title
                # If there is a description available
                if json_data["articles"][index]["description"]:
                    # Add the description of the article to description with a tab space infront and a dash.
                    description += "\t - " + json_data["articles"][index]["description"] + "\n"
                    # Append the description to the text
                    text += description
                # If there is no description available
                else:
                    description += "\t - No description available.\n"
                    text += description
                # Increment the index by 1
                index += 1
            # Return the final string that contains all the titles, dates and descriptions
            return text
        # If the status of the server is not ok
        else:
            sys.exit("Server Status: %s | Oops this is awkward :( I'm trying to connect but it seems like the server is down... Please try again later" % colored(json_data["status"], "red"))
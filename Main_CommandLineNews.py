# Import required modules
from problem5_TopHeadlines import TopHeadlines
from problem5_Search import Search


class CommandLineNews():
    """Brings you the very best of the daily news! Either search by Top Headlines in India!!! Or by keyword around the globe."""
    
    def get_started(self):
        # Welcome the user
        print("\nWelcome to Command Line News!\n")
        self.input_checker()

    def input_checker(self):
        """This function checks whether a user wants to view the Top Headlines or wants to Search by keyword.

            Args:
                self (obj): Instance of CommandLineNews class.
            
            Returns:
                True: If Top Headlines is chosen.
                False: If Search is chosen.
        """
        
        # Store which option is chosen  by the user
        option_chosen = input("Please make a choice: [1] Top Headlines [2] Search\n>> ")
        # Top Headlines
        if option_chosen == "1":
            self.top_headlines()
            # Ask the user if they would like to run the program again
            self.more_news(input("Would you like to find more news articles? [y/n]\n>> "))
        # Search
        elif option_chosen == "2":
            self.search()
            self.more_news(input("Would you like to find more news articles? [y/n]\n>> "))
        # Invalid input
        else:
            print("Invalid input. Enter either '1' or '2'.")
            return self.input_checker()


    def top_headlines(self):
        # Create an instance of TopHeadlines
        top_headlines = TopHeadlines()
        # Store which category is chosen by the user e.g. Business, Technology...
        category_chosen = top_headlines.category_option()
        # Convert the news to json
        json_data = top_headlines.json_news_headlines(category_chosen)
        # Convert json into readable formatted output
        final_string_headlines = top_headlines.formatted_data_headlines(json_data)
        # Print final output
        print(final_string_headlines)

    def search(self):
        # Create an instance of Search
        search = Search()
        # Store the keyword that the user wishes to search by
        keyword_choice = search.keyword_input()
        # Convert the news to json
        json_data = search.json_news_search(keyword_choice)
        # Convert the json data into readable formatted output
        final_string_search = search.formatted_data_search(json_data)
        # Print final output
        print(final_string_search)
        

    def more_news(self, user_input):
        """This function processes the input from the user regarding if they would like more news.

            Args:
                self (obj): Instance of CommandLineNews class.
                user_input (str): Must be [y/n] indicating if they would like more news or not.

            Returns:
                main(): If the user would like more news, start the program over again.
                print(): Say bye to the user if they would not like more news.
        """

        # When the user wants more news
        if user_input == "y":
            return main()
        # When the user does not want more news
        elif user_input == "n":
            print("Thank you for using CommandLineNews! Have a nice day :)")
            return
        # When the input is invalid
        else:
            return self.more_news(input("Invalid input. Please enter [y/n]. Would you like to find more news articles?\n>> "))



# DRIVER CODE
def main():
    """This function creates the news object and calls functions from TopHeadlines and Search to display the news to the user."""
    
    # Create an instance of CommandLineNews
    news = CommandLineNews()
    news.get_started()


if __name__ == "__main__":
    main()
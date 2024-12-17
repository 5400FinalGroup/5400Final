## Data Preparation

To support our exploration of online toxicity in AI art discussions, we collected tweets containing the query "AI Art" as test data. Using the X (formerly Twitter) API via the Tweepy library, we dynamically managed rate limits with multiple API keys. The collected data was stored in JSON format, retaining essential fields such as the tweet ID, text, and timestamp. Duplicates were removed based on unique tweet IDs to ensure the dataset's integrity. For training, we utilized a labeled dataset from the [Jigsaw Unintended Bias in Toxicity Classification](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data), which provided a solid foundation for building and validating our models.

For preprocessing, we applied a rigorous cleaning pipeline to standardize the data. Unwanted elements such as hashtags, mentions, URLs, non-English words, and special characters (e.g., punctuation, emojis) were removed. The text was converted to lowercase, and duplicate entries were eliminated. Using the NLTK library, stopwords were filtered out, and stemming was applied to reduce words to their root forms for effective analysis.

The cleaned tweets were structured into a Pandas DataFrame, with unnecessary columns removed for clarity. The resulting dataset was then exported as a CSV file, ready for further analysis and model training.

For access to all of our data used in this project, please see the link in the [Data](#data) Section.

## Data {#data}

The data used for training the machine learning models is stored in a Google Drive folder, and is publicly available for reference. The web app and the associated package are based on a fixed training set that has been preprocessed and used for training the models (Decision Tree, SGD Regression, and LSTM).

This training set contains labeled comments related to AI art discussions, and it serves as the foundation for predicting the toxicity of user-submitted comments.

For more details on accessing the data, please refer to the appropriate sections in the repository or follow the links to the Google Drive.

[Clik Here](https://drive.google.com/drive/folders/1sf55eVN4-7yXEqG6ucAwWtQQ9Klx7KHt?usp=sharing).

## Web App: Toxicity Analysis

We’ve developed a Flask-based web application to analyze the toxicity of comments, specifically targeting AI art discussions. The app uses pre-trained machine learning models (Decision Tree, SGD Regression, and LSTM) to predict toxicity scores for user-submitted comments. This tool allows for quick, accessible analysis and is designed to make toxicity detection more accessible beyond just AI art.

To use the app, follow the instructions in the [Web App README](./app/README.md).

Here is a demo video showcasing the app in action: [Watch Demo](https://drive.google.com/drive/folders/19lgwRHGh3OYQ3scmR-haQzbSbdO8L0MP?usp=sharing).

Here is a glimpse of the web app interface: ![](./images/web_app.png)

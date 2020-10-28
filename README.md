# Food Items Detection Web App

In this repo, I've trained Named Entity Recognition (NER) Spacy model on Yelp food reviews dataset. Trained model takes in text and find food items in the provided reviews. As local/traditional items are not included in the dataset, model may not extract food items well in such cases but works well on common items among countries like pizza, sandwich, burger, ice cream, desert etc. Total of 570 tagged reviews were used in the training process.

I've also made a small flask web application that lets user enter review in text-box, if review is too long then, user can upload pdf review file and app will parse the provided pdf file and extract the text in it. Extracted food items will be shown on the same page one item per line.

## Run Food Items Detection Web App

To run the flask app locally, follow the steps below.

- First clone the repo, open terminal/cmd and change the path to the cloned directory/Web App.
- Set or export the path in terminal/cmd,
- `export FLASK_APP=app.py` (Unix, Linux, macOS, etc.)
- `set FLASK_APP=app.py` (Windows)
- Finally, run the app by typing following command in terminal/cmd
- `flask run` (Same for windows, linux, etc.)
- Copy local host address and open your favourite browser and paste it in the address bar and enter.
- A simple black UI will pop up, hit the "Choose File" button and select any image.
- Hit the "upload button" and it will show the prediction result along with your uploaded image with the bounding box.
- Have fun with face mask detection.


In `test reviews` directory, i've provided some real reviews from zomato's website, you can try that as well. Enjoy the food items.

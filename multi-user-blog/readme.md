Multi User Blog

Currently running at: https://nth-gasket-151202.appspot.com/blog

app.yaml file contains information for Google App Engine to run project

To browse the app during debug, use the google app engine. Add the exhisting application directory ./multi-user-blog to Google App Engine. 
Select the multi-user-blog project, select the green run arrow in the top left of the app engine. When the status circle next to the 
project turns green, select the browse button in the app engine. The app should now display in your browser.

In order to deploy the project to the Google Cloud SDK, navigate to the ./multi-user-blog directory in the command line, and type
"gcloud init" into the terminal and press enter. Follow the instructions by logging in to your google account, and selecting the project
from the Google SDK you wish to work on. After completion, enter "gcloud app deploy app.yaml" into the terminal and press enter. The app should
be deployed to [project-name].appspot.com.

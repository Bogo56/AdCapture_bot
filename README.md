<h1 align="center">
  <br>
  <a href=""><img src="https://res.cloudinary.com/dawb3psft/image/upload/v1647932180/Portfolio/xbot.png" alt="AdCaptureBot" width="300"></a>
</h1>

<h4 align="center">Python-Kivy App for automated monitoring of competitor's Facebook ads.</h4>

<p align="center">
  <a href="https://img.shields.io/badge/Made%20with-Python-blue">
    <img src="https://img.shields.io/badge/Made%20with-Python-blue"
         alt="Gitter">
  </a>
  <a href="https://img.shields.io/tokei/lines/github/Bogo56/AdCapture_bot">
      <img src="https://img.shields.io/tokei/lines/github/Bogo56/AdCapture_bot">
  </a>
  <a href="https://img.shields.io/github/languages/count/Bogo56/AdCapture_bot?color=f">
    <img src="https://img.shields.io/github/languages/count/Bogo56/AdCapture_bot?color=f">
  </a>
  <a href="https://badgen.net/github/commits/Bogo56/AdCapture_bot">
    <img src="https://badgen.net/github/commits/Bogo56/AdCapture_bot">
  </a>
</p>

<p align="center">
  <a href="#about-the-project">About The Project</a> •
  <a href="#check-out-the-project">Check out the Project</a> •
  <a href="#project-workflow">Project Workflow</a> •
  <a href="#project-structure">Project Structure</a> 
</p>

## Built With
###  Languages
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://res.cloudinary.com/dawb3psft/image/upload/v1647933330/Portfolio/kv-lang.png">
<p>
  
### Frameworks
<p>
<img src="https://res.cloudinary.com/dawb3psft/image/upload/v1647933068/Portfolio/kivy.png">
</p>

### Databases
<p>
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white">
</p>

### Additional Libraries and Technologies
<p>
  <img src="https://img.shields.io/badge/Imaging-Pillow-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Web Scrape-Selenium-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Packaging-PyInstaller-blue?style=for-the-badge">
</p>

## About The Project
This is an app that is inspired by a **REAL-world scenario**, that we **had at the company** (Digital-Marketing company) I'm working at. The idea of it was to **automate some repetative tasks** that me and my colleagues had to do. The **goal of this app was to save some time for my team and increase it's productivity** by spending it on much more usefull tasks.

## Description of the problem
So basically Facebook has a section - (https://www.facebook.com/ads/library) - where anyone can see if a certain page currently has active ads and what they are. You can also filter your search by category, keywords, countries etc. A lot of times we needed to manually visit the page, make multiple screenshots for different competitors that a client has and then collect all those screenshots and send them on email to the client. Sometimes this was done a couple of times a week - loosing about 2-3 hours of productive time per person per month.

### And the Solution
I wanted to create a solution that would be usefull to all my teammates and not just myself. That's why a simple script was not enough. So i had to create an app that could be used by anyone and mainly non-coders. This is how I came up with this project.

## How To Use
1. Insert the id's of the pages you would like to take screenshots of into the Database.
2. Add the email you're sending to.
  a. once inserted the data is persisted for every time the app is opened   

### Fully automated mode
* In this mode the app does all the work of making the screeshots, generating a PDF from them and sending it to the chosen email - with the click of a single button.


## Project Workflow
Here, I'm outlining very briefly the phases that the project went trough from start to finish.

### Phase 1 - Creating Data
Before creating the app, I needed some data. In this case I needed a lot of recipes - at least a couple of hundred. So where do I get that data? Well, I actually decided to create it myself, or let's use the term "borrow it"😁 from another site (only for the sake of the project). SOO I did a research on the popular cooking websites in Bulgaria, and chose one with proper structure for scraping. Then I wrote a couple of scripts in Python using the Pandas Library that:

  1. Scraped the summary info of the recipes, shown in the "All Recipes Section", while going trough all results pages - inserting the info into a DB.
  2. Visited every individual recipe page and scraped it's full description and ingredients - updating the recipe data in the DB.
  3. Scraping once more - this time downloading the images (that I later upload on Cloudinary) - updating the recipes with the image links in the DB.
  
### Phase 2 - Making Data Accessible
So now that I had the data, I had to make it available to be consumed by another entity - e.g. frontend. So I created a simple API in Flask that delivered the data
to my frontend application.

### Phase 3 - Creating the Frontend
Now that I have laid the foundation, I could start working on the App itself.

### Phase 4 - Deployment
I have deployed the simple Flask API to my own server in the beginning, so I could test the frontend app during development with it.

I deployed the frontend to Heroku - since this would save me some time with server configuration.

## Project Structure

* All scraping scripts are placed in `./api_python/seed` folder
* The actual frontend App in `./javascript` folder follows the MVC architecture.

```
📦 RecipeApp
├─.gitignore
├─.idea
├─ README.md
├─ api_python
│  ├─ api.py
│  ├─ config.py
│  ├─ requirements.txt
│  ├─ resources
│  |  └─ routes.py
│  └─ seed
│     ├─ api_model.py
│     ├─ downloader.py
│     ├─ images
│     ├─ recipes.db
│     └─ scraper.py
├─ img
│  ├─ bookmark.png
│  ├─ bookmark_grad.png
│  ├─ check.png
│  ├─ clock.png
│  ├─ error.svg
│  ├─ favicon.png
│  ├─ icons.svg
│  ├─ logo.png
│  ├─ minus.png
│  ├─ notes_.png
│  ├─ people.png
│  ├─ plus.png
│  ├─ pngegg.png
│  ├─ recipe_4.jpg
│  ├─ sample_food.jpg
│  ├─ spin1.png
│  ├─ spin1.svg
│  ├─ spinner.png
│  └─ spinner.svg
├─ javascript
│  ├─ config.js
│  ├─ controller.js
│  ├─ errors.js
│  ├─ helpers.js
│  ├─ model.js
│  └─ views
│     ├─ bookmarksView.js
│     ├─ errorHandler.js
│     ├─ eventHandlers.js
│     ├─ loginView.js
│     ├─ recipeView.js
│     └─ searchView.js
├─ main.html
└─ style.css
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)


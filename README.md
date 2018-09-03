<p align="center"><img src="https://wicsdvc.com/img/logo.png" height="200"></p>

# DVC WiCS Website
Our official website!

Scroll down below to learn how you can contribute to our website!

<hr>

**Table of Contents**

* [Install](#install)
  * [Prerequisite](#prerequisite)
  * [Forking](#forking)
  * [Cloning](#cloning)
  * [Installing Dependencies](#installing-dependencies)
* [Develop](#develop)
  * [Tech Stack](#tech-stack)
  * [Project Structure and Files](#project-structure-and-files)
  * [Making Changes](#making-changes)
  * [Using Git](#using-git)
* [Contribute](#contribute)
  * [Making Pull Request](#making-pull-request)
  * [Contributors](#contributors)

<hr>

## Install

### Prerequisite

Before we start, you need to have these installed in your computer:
* [Git](https://git-scm.com/)
* [Node.js](https://nodejs.org/en/)

### Forking

1. Login to your GitHub account.
1. Click the "Fork" button at the top right of this repository.<br>
  <img src="https://github-images.s3.amazonaws.com/help/bootcamp/Bootcamp-Fork.png" height="50"><br>
  This should create a fork of the repository in your own account.<br>
  The forked repository is usually located in `https://github.com/<YOUR USERNAME>/wics-dvc.github.io`.

### Cloning

1. In your forked repository page, click the green "Clone" button at the top right of the page.<br>
  <img src="https://help.github.com/assets/images/help/repository/clone-repo-clone-url-button.png" height="50"><br>
1. Copy the link that popped up.<br>
  <img src="https://help.github.com/assets/images/help/repository/https-url-clone.png" height="100"><br>
1. Open a terminal (Mac) or command line (Windows).<br>
1. Type `git clone <THE COPIED URL>` and press enter.<br>
  (E.g.: `git clone https://github.com/nadyafebi/wics-dvc.github.io.git`)<br>
1. If successful, there should be a new folder called `wics-dvc.github.io` in your computer.

### Installing Dependencies

1. Open a terminal/command line in the project folder.
1. Type `npm install` and press enter.<br>
  This will install all Node.js modules that we need to develop this project.
1. Type `npm install gulpjs/gulp-cli -g` and press enter.<br>
  This will install Gulp (see the [Tech Stack](#tech-stack) section below to learn more).

Now you're all set to develop the website!

## Develop

### Tech Stack

* [**Node.js**](https://nodejs.org/en/)<br>
  Node.js is a JavaScript run-time environment that executes JavaScript code outside of a browser.<br>
  We use it so we can work with Gulp and Panini in our project.
* [**Gulp**](https://gulpjs.com/)<br>
  Gulp is a toolkit for automating development workflow.<br>
  When any of the HTML files changed, it calls Panini to process those files.
* [**Panini**](https://github.com/zurb/panini)<br>
  Panini is a simple HTML files generator.<br>
  It will convert the templates in the `src` folder into HTML pages.
* [**Bootstrap**](https://getbootstrap.com/)<br>
  Boostrap is a responsive front-end framework for designing websites.<br>
  It makes our website looks pretty!

### Project Structure and Files

* `wics-dvc.github.io`
  * All the HTML files inside this folder are the one being served to the website.<br>
    (E.g.: `https://wicsdvc.com/` points to `index.html`)<br>
    **Any changes to HTML files directly inside this folder will be overwritten by Panini.**<br>
    **Instead, change the HTML files inside the `src` folder.**
  * `css/main.css`<br>
    This CSS files is the one we use to customize our website. It also overwrites Bootstrap components.
  * `img`<br>
    Put any images inside this folder.
  * `src`
    * `layouts/default.html`<br>
      This is the default layout. Any code here will be applied to all the pages. You can add/remove CSS files, JS files, and fonts here.
    * `pages`<br>
      All the pages here will be converted by Panini to a full HTML files in the main folder.<br>
      (E.g.: `wics-dvc.github.io/src/pages/index.html` => `wics-dvc.github.io/index.html`)
    * `partials`<br>
      This folder store HTML components that can be reused in multiple pages.

**Files and folders that are not mentioned in the above list should not be changed or removed.**

### Making Changes

You can use your favorite text editor to change any of the files.

Before starting:
1. Open a terminal/command line.
1. Type `npm start` and press enter.

This will run Gulp in the terminal. Do not close this terminal while you're developing.

To see the website you're developing, open the `wics-dvc.github.io/index.html` file.
Every time you make any changes, you can just refresh the browser (as long as the Gulp terminal is open).

### Using Git

Git is a version control system for tracking changes in computer files.

After you've finished changing the website:
1. Open a terminal/command line.
1. Type `git add *` and press enter.
1. Type `git commit -m "<DESCRIBE YOUR CHANGES HERE>"` and press enter.<br>
  (E.g.: `git commit -m "Add new pages"`)
1. Type `git push` and press enter.

This whole process will add and upload your changes to GitHub. You can see the new changes you made at the forked repository page.

If you want to finalize your changes to the actual website, check out the next section.

## Contribute

### Making Pull Request

1. Go to your forked repository page.
1. Click the 'Pull Requests' tab on top of the page.
1. Click the 'New Pull Request' button on the right.
1. Describe your changes in the form.
1. Click 'Create Pull Request' if you're done.

Congrats for making it this far! If we accept your pull request, the changes you made can be seen in our website and we will add your name to the list below.

### Contributors

* Nadya Djojosantoso ([@nadyafebi](https://github.com/nadyafebi))

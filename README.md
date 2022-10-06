# **The Underwater Gang**

## **1. About** 

View the live project here: https://the-underwater-gang.herokuapp.com/.

The Underwater Gang is the website for a community of scuba divers; it currently offers: 
  - a blog for users to share their knowledge and experience on all things scuba; 
  - a personal logbook for divers to log their dives.

## **2. General User Goals** 

### **2.1 Site Owners' Goals**
The goal of the three owners is to see their website become the trusted companion for a thriving community of scuba divers.  
They want to offer a platform where ideas, tips, safety advice, personal experiences and stories can be shared by all divers, experienced or not. To do so, they offer a blog where registered users can write and comment posts. For the community to receive true value and reliable information, all posts and comments must be approved before being published. This will make sure that the site owners - who are experienced divers themselves - can filter out incorrect and potentially harmful information.
In addition to the blog, each registered user is offered a personal logbook, where dives with their specific info (e.g. location, depth, etc.) can be logged. This is an important tool for scuba divers, allowing them to keep track of their progress and experiences; at the same time, with its potential to encourage users to come back to the website, it is also a key feature for the growth of The Underwater Gang's community.

### **2.2. User Goals**
* New divers:
New divers are the first category of website users. Having recently discovered this amazing sport, they naturally want to expand their knowledge of it; they come to the website as they search for resources online. 
* Pro divers:
The second category of users is made up of experienced divers looking for a platform of like-minded people; they desire to share what they have learnt over the years, as well as to hear from other long-time practitioners such as diving instructors or divemasters (i.e. underwater tour guides).
Both types of users can find a place not only to read from, but also to contribute to with their own posts.

## **3. Wireframes & Database, User Stories & Agile Development**

A detailed report regarding user stories and agile development can be found here: [Wireframes & Database, User Stories & Agile Development](documentation/Agile.md).

## **4. Features**
### 4.1 *Existing features*

This section will provide an overview of the website. Where available, two different screenshots of each page/section will be provided, in order to show the difference in outlook depending on the status of the user (not/authenticated).

* Homepage

![The Underwater Gang's homepage](documentation/images/home.png)

The homepage concisely informs users of what the website is and what to expect from it.

* Site logo & Navigation Bar - General

![The site logo and navigation bar - general](documentation/images/navbar-general.png)

The navbar for general users shows the basic functions available. The blog is accessible by everyone, whereas the logbook main page will prompt non-authenticated users to sign in or sign up.

* Site logo & Navigation Bar - Authenticated user

![The site logo and navigation bar - authenticated user](documentation/images/navbar-signedin.png)

The navbar for authenticated users changes to reflect their current status. The "Sign in" and "Sign up" icons disappear, being replaced by "Write", "Log" and "Logout".

* Blog - General

![Blog - general](documentation/images/blog-general.png)

The blog page available to all users, regardless of their status. It offers the possibility to browse and read posts.

* Blog - Authenticated user

![Blog - authenticated user](documentation/images/blog-signedin.png)

The blog page available to signed-in users. It offers the additional feature of writing a new post through the page-top button.

* Post content - General

![Post content - general](documentation/images/post-general.png)

The post content available to all users, regardless of their status.

* Post content - Authenticated user (1)

![Post content - authenticated user 1](documentation/images/comment-box.png)

The first extra feature available to authenticated users, showing an additional section to post comments.

* Post content - Authenticated user (2)

![Post content - authenticated user 2](documentation/images/comments.png)

The second extra feature available to authenticated users, showing each post's comments, if available.

* Post content - Authenticated user (3)

![Post content - authenticated user 3](documentation/images/no-comments.png)

An invitation for authenticated users to be the first person to leave a comment where none is present.

* Post - Write

![Create post form](documentation/images/post-create.png)

The form to create a new post. It offers the possibility to upload an image, write a title and the main content.

* Post - Choices

![Update and delete buttons](documentation/images/post-choices.png)

The two buttons at the bottom of each post show only for logged in users who are the creators of the post in question. They redirect the user to the update or delete pages.

* Post - Update

![Update post form](documentation/images/post-update.png)

The form to update a post. It comes with the previous content already filled in.

* Post - Delete

![Delete post form](documentation/images/post-delete-msg.png)

A message that requires user confirmation for the deletion of a post.

* Logbook - General

![Logbook - general](documentation/images/logbook-prompt.png)

The logbook's main page available to unauthenticated users, prompting them to either sign in or sign up.

* Logbook - Authenticated user

![Logbook - authenticated user](documentation/images/logbook-main.png)

The logbook's main page available to authenticated users, showing the button to log a new dive, as well as all the previous ones and the possibility to update or delete them.

* Dive content - General

![Dive content - general](documentation/images/dive-content.png)

The dive content with all the info previously submitted by the user.

* Dive - Create

![Dive form - create](documentation/images/log-dive.png)

The form to log a dive.

* Dive - Update

![Dive form - update](documentation/images/update-dive.png)

The form to update a dive. It comes with the previous content already filled in.

* Dive - Delete

![Dive deletion warning](documentation/images/delete-dive.png)

A message that requires user confirmation for the deletion of a dive.

* Sign in page

![Sign in page](documentation/images/sign-in.png)

The sign in page for registered users.

* Sign up page

![Sign up page](documentation/images/sign-up.png)

The sign up page for new users.

* Sign out page

![Sign out page](documentation/images/sign-out.png)

The sign out page for logged in users.


### 4.2 *Features left to implement*
* *Diver's friendbook*
   * The goal of the website is to create a community, not only to provide a blog platform and an individual logbook. For this reason, in the future divers will be able to add friends on their profile, thus creating meaningful human connections that hopefully extend into the real world (and sea).
* *Standard-size image*
   * The images at the top of each blog post currently vary in size. A future version of the project will provide standardised measurements to improve the aesthetic balance.

## **5. Validation and Performance**
### 5.1 *Validator Testing*
* HTML
   * The final version of the code is free of errors when passed through the official W3C Markup Validator via URI.  
   However, a difference was noted upon checking the .html files individually as opposed to validation via URI. Since this is a Django-based project, the source code had to be retrieved by right-clicking on each page in the front-end, then selecting the "View page source" option. In fact, the markup validation service is not able to recognize the Jinja templating language and throws several errors because of this.

   ![W3C HTML Validation](documentation/images/html-validation.png)

* CSS 
   * No errors were found when passing through the official W3C Jigsaw Validator.

   ![W3C CSS Validation](documentation/images/css-validation.png)

* PEP8
   * The .py files in the blog and logbook apps were passed individually through the https://www.pythonchecker.com/ PEP8 validator. The general results vary from around 50% to more than 90%, showing however no errors. In order to explain this gap in results, two things need to be noted here: 
     1) The lower results are mostly due to unimplemented suggestions with regard to spacing before and after some operators (such as, for instance, the "=" sign); in this case, I have decided not to implement the given suggestions as they were not crucial to the overall style or syntax.
     2) Some indentation warnings not raised by the linter in the Gitpod environment were instead raised by the above mentioned checker. In this case, I have thought it safest to follow the suggestions of the linter in Gitpod, since it is there that the code was written. The indentation warnings were, in any case, merely related to the breaking of a function's arguments into two lines (for matters of overall line length) and were not Python syntactic errors.  

### 5.2 *Responsiveness*
The site is fully responsive. 
Manual testing has been performed on the following three devices:  
- MacBook Pro (Retina, 13 inch, Late 2013);
- iPad Pro (12.9 inch, Third Generation);
- Xiaomi Redmi 5 (5.7 inch).

### 5.3 *Lighthouse Report*

* Mobile

![Lighthouse report for mobile](documentation/images/lighthouse-report-mobile.png)

As observable in the report screenshot, mobile performance is lower on mobile than on desktop. This will be improved in future versions of the project by applying modifications such as, for instance, those related to the size of the images.

* Desktop

![Lighthouse report for desktop](documentation/images/lighthouse-report.png)

### 5.4 *Accessibility*

A first Lighthouse report returned a score of 79/100 for accessibility, due to several missing aria-label attributes on buttons and links. After implementing the due corrections, the final score is 97/100.

### 5.4 *Internal links*

Every link on the website is fully functioning.

## **6. Testing and Bugs**

The manual tests run on the project can be found here: [Testing](documentation/testing.md).  
User stories tests can be found here: [User Stories & Agile Development](documentation/Agile.md).  

## **7. Deployment**

The detailed procedure for deployment can be found here: [Deployment](documentation/deployment.md).

## **8. Technologies Used**
* Languages and Frameworks
   * **HTML5**
   * **CSS3**
   * **Python**
   * **Django**
   * **Bootstrap**

* Websites and Softwares
   * **Balsamiq**: used to create the website's wireframes (see the 'documentation/wireframes' folder)
   * **Font Awesome**: FA's icons were used to create the social media links found in the website's footer.
   * **Git**: Git was used for version control through the Gitpod terminal, to add, commit and push the project's updates to GitHub.
   * **GitHub**: GitHub was used to store the project's repository.
   * **Heroku**: Heroku was used to host the deployed project.
   * **Google Fonts**: Google Fonts was used to import the two fonts in use on the website, namely the "Permanent Marker" and "Exo 2" ones.
   * **ColorSpace and ColorHunt**: The color palette used in the project was created on these websites.
   * **Asana**: Used for creating and storing user stories, and to keep track of the development process.
   * **Pexels**: For post images.
   * **Icons8**: For the homepage drawing.

## **9. Credits**
### 9.1 *Credits*
All code was written by me personally. However, during the development process I relied considerably on the Code Institute *I Think Therefore I Blog* walkthrough project and Corey Schafer's Django tutorials. 
### 9.2 *Content*
The entirety of the content found on the website has been created by me personally. I drew from my personal experiences as a new scuba diver to create the text found in the two posts by the website creators, while creating other content for the remaining posts.
### 9.3 *Media*
All the images displayed on the website were downloaded from Unsplash.com and Pexels.com. Here follows the list of the photographers whose work has made this project possible:
   * *Welcome to our blog!* photo by Pixabay 
   * *Exploring Uncharted Waters* photo by Pia
   * *Recoinnassance Dives* photo by Aviv Perets  
   * *Whale Shark!* photo by Emma Li
   * *About us...* photo by Ayman Zaki

The drawing on the homepage was downloaded from Icons 8.

## **10. Acknowledgments**

This project would have been impossible without the help of some incredible people, whom I wish to thank here.
- A special thank you goes to my mentor, Mr Richard Wells, for continuous guidance, suggestions and much needed encouragement. Thank you also for pushing me to do more, to go beyond my limits. It is a lesson I am still in the process of learning.
- Thank you to the talented people of the Tutoring team that helped me out: Ed, Alex, John and Sean. You have been very kind and tremendously helpful as I struggled with some parts of my project.
- The highest praise and thanks go to God, the greatest Coder of all eternity. To Him, who has shown his eternal love for all of us in Jesus Christ. To Him, whom I owe everything.






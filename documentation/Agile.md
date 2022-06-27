# **User Stories & Agile Development**

## **1. Wireframes**

The detailed wireframes for this project can be found here: [Wireframes](/documentation/wireframes.md).

## **2. User Stories - Description and Testing**
### **2.1 User Stories - Description** 

In crafting the user stories for The Underwater Gang, I made use of the MoSCoW technique.

This section details all the user stories I created for the project. It is a complete list, inclusive both of those I have not brought to completion as a result of changes/obstacles encountered during the development process as well as those originally intended as future-release features.

No. | User Story
--- | ----------
1   | As an admin, I want to present a clear landing page so that users can quickly understand the site's goals and feel drawn to become a member. 
2   |As a registered user, I can write new posts so I can actively contribute to the community with my experience and learn from other contributors'.
3   | As a registered user, I can create, read, update and delete my own posts so that I am always free to modulate my participation in the community.
4   | As a registered user, I can like or unlike a post so I can interact with the content.
5   | As a registered user I can comment on a post so I can be involved in the conversation.
6   | As an admin I can view comments on each post so I can moderate the conversation as necessary.
7   | As an unregistered/registered user I can view the number of likes on a post so I can start reading from the most popular ones.
8   | As a user, I can create a personal account so I can become part of the community, contribute to its blog and have my personal diver's profile.
9   | As a site user (both registered and unregistered) I can open a post so I can read it in its entirety.
10  | As an unregistered/registered user I can view a paginated list of posts so I can get an instant and clear glance at the available posts.
11  | As an unregistered/registered user I can view a list of posts so I can easily select one to read.
12  | As an admin/registered user, I can create draft posts so I can finish writing the content later.
13  | As an admin, I can approve comments so that inappropriate and/or offensive content can be left out of the community.
14  | As an admin, I can manage all blog posts so that the community may be a place which offers true value and correct information to all its users.
15  | As a registered user, I can log a new dive so I can keep track of my progress and experiences underwater.
16  | As a registered user, I can always view a list of previous dives on my profile's page so I can easily access them at any time.
17  | As a registered user, I can create, read, update and delete my dives so I can keep my personal logbook updated and relevant.
18  | As a registered user, I can store all posts together so I can easily return to previous conversations.
19  | As a registered user, I can see all posts of the same user so I can benefit from all of their contributions if I have enjoyed previous posts by them.
20  | As a registered user, I can add other divers as friends so I can keep in touch with them and their ongoing diving adventures.
21  | As a registered user, I can log a dive shared with another user so I can keep track of shared underwater adventures.

### **2.2 Testing User Stories** 

#### **2.2.1 Successful User Stories**
No. | User Story | Result
--- | ---------- | ------
1   | As an admin, I want to present a clear landing page so that users can quickly understand the site's goals and feel drawn to become a member. | Pass
2   |As a registered user, I can write new posts so I can actively contribute to the community with my experience and learn from other contributors'. | Pass
3   | As a registered user, I can create, read, update and delete my own posts so that I am always free to modulate my participation in the community. | Pass
4   | As a registered user, I can like or unlike a post so I can interact with the content. | Pass
5   | As a registered user I can comment on a post so I can be involved in the conversation. | Pass
6   | As an admin I can view comments on each post so I can moderate the conversation as necessary. | Pass
8   | As a user, I can create a personal account so I can become part of the community, contribute to its blog and have my personal diver's profile. | Pass
9   | As a site user (both registered and unregistered) I can open a post so I can read it in its entirety. | Pass
10  | As an unregistered/registered user I can view a paginated list of posts so I can get an instant and clear glance at the available posts. | Pass
11  | As an unregistered/registered user I can view a list of posts so I can easily select one to read. | Pass
13  | As an admin, I can approve comments so that inappropriate and/or offensive content can be left out of the community. | Pass
14  | As an admin, I can manage all blog posts so that the community may be a place which offers true value and correct information to all its users. | Pass

#### **2.2.2 User Stories for Future Release**
In this section I will focus on the user stories that did not make it to the first release of the project, explaining the reason for each one.

No. | User Story  | Result
--- | ----------  | ------
7   | ~~As an unregistered/registered user I can view the number of likes on a post so I can start reading from the most popular ones.~~ <br> I decided to discard this feature during development purely for aesthetic reasons. I decided the post card had too much information on it and left it to the title and the post image, rather than the number of likes, to draw the reader's interest to the post.  | Fail
12  | ~~As an admin/registered user, I can create draft posts so I can finish writing the content later.~~ <br> This is a secondary feature that I failed to implement due to lack of time. In the current release, users cannot save posts and drafts, only complete the writing in a single sitting.   | Fail
15  | ~~As a registered user, I can log a new dive so I can keep track of my progress and experiences underwater.~~ <br> Failed to complete because of time constraints. The logbook features were intended as first-release features. However, due to the complexity of the project and me learning to work with new technologies (Django and Bootstrap), I had to reduce the scope of the project and postpone these features to a future release. This applies to User Stories n.16 and n.17 too.   | Fail
16  | ~~As a registered user, I can always view a list of previous dives on my profile's page so I can easily access them at any time.~~ See n.15.  | Fail
17  | ~~As a registered user, I can create, read, update and delete my dives so I can keep my personal logbook updated and relevant.~~ See n.15.  | Fail
18  | As a registered user, I can store all posts together so I can easily return to previous conversations. <br> Originally planned as a future-release feature.  | N/A
19  | As a registered user, I can see all posts of the same user so I can benefit from all of their contributions if I have enjoyed previous posts by them. <br> Originally planned as a future-release feature.  | N/A
20  | As a registered user, I can add other divers as friends so I can keep in touch with them and their ongoing diving adventures. <br> Originally planned as a future-release feature.  | N/A
21  | As a registered user, I can log a dive shared with another user so I can keep track of shared underwater adventures. <br> Originally planned as a future-release feature.  | N/A
<br>

## **3. Agile Development**

The tool I chose to keep track of my work is Asana, due to its popularity and my willingness to acquaint myself with a known platform for Agile development.
On Asana, I created my user stories according to the MoSCoW technique, assigning them a specific color according to their status in order to have a visual aid through the process.

### **3.1 The project's kanban board at the final stage of development**

![Kanban board - 1](/documentation/images/project-board-1.png)
![Kanban board - 2](/documentation/images/project-board-2.png)
![Kanban board - 3](/documentation/images/project-board-3.png)

### **3.2 Things to note/improve:**
- *Poor planning:* as I started working on my project, I realised my planning had been insufficient in terms of the specificity necessary to each user story. This resulted, for instance, in subsequent updates to some user stories, as well as in a back-and-forth process between the *In progress* and *Done* sections of the board at various stages.
- *Lack of user story points:* Due to me learning both a new framework and a new methodology (Agile) I found it impossible to give an estimate of the points for each user story. For this reason, I relied solely on the MoSCoW paradigm. 


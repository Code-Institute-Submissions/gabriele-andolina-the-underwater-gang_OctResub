# **Testing and Bugs**

## **1. Testing**

This project was tested manually. Here follows a list of the tests that were carried out.  

No. | Action | Result
-- | -- | --
1 | Display homepage | ✔︎
2 | Navbar links are properly connected and lead to their related page | ✔︎
3 | Navbar displays general links for unregistered/unauthenticated users | ✔︎
4 | Blog posts open upon click | ✔︎
5 | Blog posts only reveal image, main content, and likes and comments number if opened by an unregistered or unauthenticated user | ✔︎
6 | Navigation buttons allow for navigation within the blog page, leading the user to the requested page | ✔︎
7 | Sign in page shows its related form | ✔︎
8 | Sign in button allows the user to enter its account | ✔︎
9 | Successful sign in message shows after sign in | ✔︎
10 | Navbar links change to reflect logged in status and functionality for registered users | ✔︎
11 | Blog page and navbar show "Write a post" and "Write" buttons when user is logged in | ✔︎
12 | "Write" button on navbar and "Write a post" button on blog page lead to post form | ✔︎
13 | Post form allows upload of image, title and content | ✔︎
14 | Post form cannot be submitted without key information | ✔︎
15 | Blog post displays comment form for registered users | ✔︎
16 | When present, blog post shows previous comments | ✔︎
17 | If the authenticated user is also the post's author, the blog displays "Update this post" and "Delete this post" buttons  | ✔︎
18 | "Update this post" button allows user to update post | ✔︎
19 | Update confirmation message shows when post is updated | ✔︎
20 | "Delete this post" buttons allow user to delete post | ✔︎
21 | Delete confirmation message shows to confirm post deletion | ✔︎
22 | Delete confirmation message shows when message is deleted | ✘
23 | Logbook page and navbar show "Log a dive" and "Log" buttons when user is logged in | ✔︎
24 | "Log" button on navbar and "Log a dive" button on logbook page lead to dive form | ✔︎
25 | Dive form correctly shows all Dive model fields | ✔︎
26 | Dive form cannot be submitted without key information (title, date, location, diving site) | ✔︎
27 | Dive card leads to full dive details | ✔︎
28 | "Update" and "Delete" buttons correctly show on each dive card | ✔︎
29 | "Update" button allows user to update dive | ✔︎
30 | Update confirmation message shows when dive is updated | ✔︎
31 | "Delete" button allows user to delete dive | ✔︎
32 | Delete confirmation message shows to confirm dive deletion | ✔︎
33 | Delete confirmation message shows when dive is deleted | ✘
34 | Log out link leads to log out form | ✔︎
35 | Log out confirmation message shows after log out | ✔︎
36 | Sign up link leads to sign up form | ✔︎
37 | Sign up form effectively creates user profile | ✔︎
38 | Admin: Admin page shows comments and posts sections to manage site content | ✔︎
39 | Admin: Comment actions include "delete" and "approve" | ✔︎
40 | Admin: Post actions include "delete" | ✔︎
41 | Admin: Post status can be changed from "draft" to "published" to show post in blog page | ✔︎
42 | Admin: Logbook page shows sign in/sign up prompt for unauthenticated users | ✔︎
43 | Admin: Access to personal dives by unauthorised users is forbidden | ✔︎

## **2. Known Bugs**

No. | Description 
-- | --
1 | Delete confirmation message fails to show when message is deleted
2 | Heart icon in post content templates shows gray background and smaller font than comment icon
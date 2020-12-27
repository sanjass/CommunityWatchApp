
# [Community Watch](https://communitywatch.herokuapp.com/)
Team Justice League, final project for 6.170 (Software Studio) class at MIT.

<p align="center">
  <img src="public/favicon.ico" width=300 />
</p>


### Purpose and Functionality

Community Watch is an app that allows the citizens of Cambridge to stay up to date on local crimes and engage in community discussion on crimes in neighborhoods as well.

#### Key Purposes:

- Provides a visual for citizens to understand crimes in neighborhoods
An Interactive visual provides benefits like real-time filtering, interactive hoverability for crime statistics, etc. Citizens can now better make out crime patterns in particular neighborhoods by observing the geography of it easily.
Provides a platform for community discussion on crimes


- Citizens can now openly talk about crime with others in a safe space. This safe space is ensured by rules regarding flagging of posts and replies. Having the power to engage in community discussion on crime keeps the community well-informed on what community concerns are.


- Provides a personal feed for crimes for the neighborhoods you follow
Users can follow certain neighborhoods to stay updated on the crimes in those neighborhoods and the community discussion relevant to those neighborhoods as well. This provides a more personal way of knowing what crimes and posts are relevant to you while filtering out the noise of other neighborhoods.



## Installation
```
sudo npm install
```

## Usage

```
sudo npm run build
sudo npm run serve

sudo npm run awesome //in a separate terminal tab
```
Navigate to `localhost:8080` in your browser


### Authorship:
* **Sanja Simonovikj**:
  * initial Vue setup
  * src
    * components/NeighborhoodList.vue
    * components/NeighborhoodListItem.vue
    * components/Navbar.vue
    * components/ChangeUserCredentials.vue
    * components/DeleteAccount.vue
    * components/Signin.vue
    * components/Signup.vue
    * components/Signout.vue
    * components/UserProfile.vue
    * components/UserSettings.vue
    * views/Account.vue
    * components/FlagPostIcon.vue
    * components/PostItem.vue (small changes)
    * components/Feed.vue (small changes)
    * views/Main.vue (small changes, date filter)
    * other minor changes, bug fixes etc
  * models:
    * Neighborhoods.js
    * Users.js
    * Posts.js (flag related content)
  * routes:
    * neighborhoods.js
    * users.js
    * session.js
    * posts.js (flag-related content)

* **Wenbo Shi**:
  * populateDB
    * addcoordinate.py
    * postdata.py
  * db
    * db_config.js
  * models
    * Feeds.js
    * Downvotes.js
    * Upvotes.js
  * routes
    * feeds.js
    * downvotes.js
    * upvotes.js
    * minor part of crimes.js
  * src
    * part of components/Map.vue
    * minor part of components/Navbar.vue
    * views/MyNeighborhood.vue
    * components/UpvotePostIcon.vue
    * components/DownvotePostIcon.vue
    * part of components/PostItem.vue

* **Stuti Vishwabhan**:
  * src
    * components/Map.vue
    * components/CrimeList.vue
    * components/CrimeListItem.vue
    * components/Main.vue
    * components/Feed.vue
    * components/PostItem.vue
    * components/DeletePostIcon.vue
    * components/DeleteReplyIcon.vue
    * components/PostAndReplyModal.vue
    * components/ReplyItem.vue
    * components/ReplyModal.vue
  * db:
    * db_config.js
  * models: 
    * Posts.js
    * Replies.js
  * routes:
    * crimes.js
    * posts.js
    * replies.js
    * validators.js
    
* **Fernando Herrera**:
  * src
    * App.vue
    * router.js
    * main.js
    * Main.vue  (combined all vue routers into one page)
    * components/Feed.vue
    * components/UserSettings.vue
    * components/CrimeList.vue
    * components/CrimeListItem.vue
    * components/map.vue
    * components/NavBar.vue
  * models:
    * Crime.js
    * Feed.js (small changes)
    * Neighborhoods.js (small changes)
  * routes:
    * crimes.js
    * feed.js (small changes)

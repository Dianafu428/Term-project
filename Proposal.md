# Term Project Proposal

## The Big Idea

- **Main Idea**:
    - Establish a Covid-19 content aggregator website that collects the number of positive cases across some major towns (ex. Babson campus, Newton, Wellesley, etc.) in the Greater Boston area. 
    - Through the website, users can easily access the pandemic data and check the update at any time as well as choosing to see the cases in a certain town.
- **Topics**:
    - Website building and design.
    - Scrapy will also be used to collect and aggregate data from other websites.
- **Minimum Viable Product**:
    - The website will have a home page with a scroll down list.
    - When users click on the scroll down list, names of towns will be provided.
    - By selecting a specific town, related data will show up on the page.
- **Stretch Goal**:
    - Provide convenience for users as they no longer need to check data for different towns by visiting different websites or databases.
    - Help users be aware of the real-time pandemic situation around their residence.

## Learning Goals

- **Shared Goals**:
    - To build a basic, functional website.
    - To be able to use scrapy to collect data from different websites.
- **Individual Goals**:
    - To strengthen understanding of python (function, database, libraries, and framework).
    - To employ skills from class into real life problems.
    - To enhance logical thinking and analytical skills.

## Implementation Plan

- [ ] **Content Aggregator**: 
    - Use libraries such as *requests* for sending HTTP requests and *BeautifulSoup* to parse and scrape the necessary content from the sites.
    - Use libraries such as *celery* or *apscheduler* to implement content aggregation as a background process.
    - Potential framewors that we can use: https://scrapy.org/

- [ ] **Web Design**
    - Use libraries such as *Flask* or *Django* to build website framework
    - Use java and Spring Boot to create a website: https://start.spring.io/


## Project Schedule

- [ ] **9/21-10/5**: Gather information, learn scrapy functions and frameworks, set up fundamental HTTP requests and scrape the necessary content from sites
- [ ] **10/5-10/19**: Work on scraping content from various sites, creating database, finish any visualization/content format 
- [ ] **10/19-11/16**: Work on web design, create a website/homepage that enables users to choose the location and display scraped content properly
- [ ] **11/16-11/30**: Integration. Work on final deliveries.

## Collaboration Plan

- **Weijia**: mainly focus on content aggregator (scraping)
- **Diana**: mainly focus on web design
- We will help each other to finish each part through the process (indepent but also collaborative) and integrate our results at the end.

## Risks

- **Scraping**: not familiar with scraping technique, ignoring existing APIs, inappropriate crawling frequency, failure to dealing with target website changes
- **Web Design**: not very confient with our web development skills, may not able to design a pretty website
- **Integration**: may have trouble with integrating codes

## Additional Course Content

- **Flask**: the web apllication course on 10/15
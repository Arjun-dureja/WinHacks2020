# WinHacks2020 - CoronaBase
**Fighting COVID-19 by reducing the gap between resource distributers and product manufacturers**
*Uzair Ahmed, Arjun Dureja, Shoeb Islam, Niranjan Krishnaswamy*

**[https://devpost.com/software/covidbase](https://devpost.com/software/covidbase)**

## Inspiration
As we are currently in the midst of a pandemic, we wanted to create a system that streamlines the distribution process for companies that want to contribute their services in creating commodities in the battle against COVID-19. Such necessities that are rapidly depleting in quantity include N95 masks and ventilators. CoronaBase involves the usage of a regularly updated database that contains the information of companies that agree to provide resources in the production of these aforementioned items. This database seeks to attract the attention of production companies that specialize in these products and hopefully aids in bridging the gap between the producing and the supplying sectors. 

## What it does
We have implemented CoronaBase using a three-paged website, a database, and various Python scripts. Firstly, the initial page of the website has a button to initiate parsing so that when it is clicked, the web scraping script starts. This scraped information is then filled into the first collection of the database, and will also be displayed on page 2 of the site. Each data entry has its own email button, which when clicked, initiates the email script to respective company officials who are potential resource providers. Afterward, a receiver will parse whatever data comes to it (from email replies), and this data gets set to the second collection of the database. Finally, the third page of the website displays this data.

## How we built it
We build CoronaBase using a myriad of technologies, including Python, MongoDB Atlas/Compass, Google Cloud Platform, and Bootstrap. We utilized MongoDB as our database to store all the data, which was gathered by using some magical Python scripts. These scripts were used to scrape data from the APMA website and to automatically email companies who might have an interest in providing supplies for the production of commodities. These emails, which were sent for the purpose of these aforementioned companies to fill out, utilized a template similar to the online 'buyandsell.gc.ca' form. Companies who happened to send emails with their information regarding their supplies are parsed and get sent back to the MongoDB database. The Bootstrap website is hosted on Google Cloud and acts as an admin dashboard to keep track of companies and emails. It pulls data from the database and displays it in a clear and coherent manner. 

## Challenges we ran into
One of the major challenges that we faced was strategically dividing tasks amongst the team members in accordance with each individuals' expertise. With time, we were able to assess each others' skills and divide work accordingly to achieve our goal.

One of the major technical challenges we had to overcome was figuring out how to import the data as CSV files into MongoDB. This was overcome by researching, testing and debugging our code to finally be able to write a Python script that imported these files as parameters into the database.

## Accomplishments that we're proud of
The main goal of CoronaBase was accomplished to a certain extent as we were able to create a product that will greatly strengthen the connection between manufacturers and distributors.

## What we learned
We learned how to utilize MongoDB to store data in an efficient manner and send this data to a Boostrap website to display clearly and coherently.

## What's next for CoronaBase
We seek to increase the depth of CoronaBase to support the growth and production of more products besides N95 gas masks and ventilators and be able to provide this service to a greater demographic.


**Note**
Due to technical difficulties with domain.com, it was not possible to link our domain.com registered domain to our website. Our domain.com link is maintainyour.space.
# OpenWeatherBot
This project was born with the goal of preventing me from forgetting again the laundry hanging outside on rainy days finding my clothes soaked when I return home.
Definitely not one of the most important problem in the world, but for sure it is a  real problem for out-of-town students like me.
Since I am not a person who checks the weather on a daily basis, I need a system that informs me of the weather through means that I am already used to using. For this reason I choose to create a telegram bot that will tell me everything that I need to know.

## Goals
- I will create a telegram bot that every morning at 7:00 will notify me through a message about the the weather of the day, warning me if it will rain or snow and reporting main 	     informations such as max and min temperatures.

## Requirements
- The bot must send me a message every morning at 7:00 
- The bot must create a clear and short message  
- The bot must run for free

# Development

## Telegram
The first thing to do is creating a telegram bot through Telegram itself and its bot BotFather. I won’t say much about this because there are already hundreds of guides that explain how to do it. I chose for the name “WeatherBot🌤” and for the username “A_Great_Weather_Bot” (it was my 27th choice as all those before had already been taken).   

## OpenWeather
To take the weather forecast I chose the site “OpenWeather” that offers an API to have access to weather forecast in almost every place in the world. 
I subscribed to their plan “One Call API 3.0” that allow you to make the first daily 1000 API calls for free and on their website it is possibile to set a limit on the API calls, so I just put the limit at 100 to pay nothing .
Here https://openweathermap.org/api you can find all the informations about the API and the different plans.

## Python
Informing me on the internet seemed to see that python is the most used language for telegram bots with a lot of libraries free to use. I never worked with it before but this project it is a great excuse to start studying it. 

## AWS
Since the bot has to run forever I need some place to run it that it is not my computer. I decided to chose the Amazon Web Services to create a virtual machine and use it as a server for two reason:
1)Since the project is quite small I can use the free plan. 
2)It is a service used by many companies so I think that learn how to use it may come in handy in the future.
Setting the time of the virtual machine in order to synchronize it with Italian time was not immediate since Amazon Linux doesn’t work exactly like other distributions, this guide really help me: https://stackoverflow.com/questions/57960715/changing-timezone-in-ec2-linux-instance.
To put the scripts on the amazon server and run it forever I followed the following tutorial: https://www.youtube.com/watch?v=xXirbnUB3NU&t=324s.

##Conclusion
This projects was very interesting ,nice and easy to do. I found a solution to one of my problems respecting all the requirements and i learned some very interesting stuff and I developed the bot so that also my friends, or anyone that is interested, con use it freely. 

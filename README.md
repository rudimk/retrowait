# retrowait.py
A Python adaptation of XKCD's "Backward in Time" | http://xkcd.com/1017/



First, an introduction to the algorithm in question:

![The Comic](http://imgs.xkcd.com/comics/backward_in_time.png)



> "People tell me I have too much time on my hands, but really the problem is that there's too much time, PERIOD."



And that, folks, is why I built Retrowait. A simple Python package that takes the amount of progress you've made on a particular task, and calculates the corresponding year in the Gregorian calendar, from now till 1 AD. But that's not it. It then queries Wikipedia, to get a quick summary about that particular year! This is particularly suited for situations where you're:

1. Stuck in a lecture that stolidly refuses to end;
2. Dealing with a tech team standup and wondering why you ever started writing code;
3. Waiting for *Game of Thrones* to stream, and wondering who's sitting on the Iron Throne next;
4. |INSERT SITUATION OF CHOICE HERE.|



Others have written similar packages. Mine's better. I write the best Python code. Nobody writes better code than me. I've got great plans. Nobody plans better.



In the future, you'd be able to:

1. Go even farther back in time, because obviously - to make time go *really* fast, you have to go back *really* far. I'm telling you, time only makes sense if you go backwards.
2. Consume this amazing algorithm through Slack and Messenger bots, while you're waiting for another person to freaking type out his/her message. Let's make waiting great again!
3. Uh..mobile app? Hybrid progressive web |INSERT FANCY TREND| app? Oh, damn it.

See? Told ya.



## Installation

If you're a virtualenv fan, great. If you aren't, great. Whatever makes your clock tick - all you have to do is this:

`pip install retrowait`



## Usage

For now, it's Python-only. Soon, there will be bots and apps and shit.

First, import the retrowait package: 

`import retrowait as rw`

Next, create a `Wait` class, passing the progress of your super boring task as a percentage. So if you're 12% done with something:

`w = rw.Wait(progress=12)`

And that's it! To see what the calculated year was, use `w.year` - or if you want the full date, there's `w.back_date`. To check out Wikipedia's summary for that year, call the `info` function - `w.info()`.



## Issues

1. As of now, Python's datetime capabilities don't include BC dates. That's a bummer - it was such a fun time! Unfortunately, this also means that if `progress` is more than 61%, it breaks. Which is stupid.
2. Another thing that is a little tough with datetime, is using non-integers in datetime algebra. It sounds pretty obvious mathematically - but apparently it isn't. 
3. It would be nice to pretty-print more information from Wikipedia for a particular year.

Track these issues [here](https://github.com/rudimk/retrowait/issues). Feel like helping me telescope time? Fork, write code, open a PR. 


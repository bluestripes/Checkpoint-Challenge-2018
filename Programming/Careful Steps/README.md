> Careful Steps  
> [This](https://s3.eu-central-1.amazonaws.com/csh-static/careful_steps/4ddd88c6cd5cf1c40916763a7185b2fcb589c2cdfd6530646104e4cd2f21b91b.zip) is a bunch of archives we've found and we believe a secret flag is somehow hidden inside them.  
> We're pretty sure the information we're looking for is in the comments section of each file.  
> Can you step carefully between the files and get the flag?  
> Good luck!  

Apparently, a bunch of archives is 2000 archives (!!!). Not much in them (Boring.txt in some with 0 bytes but still).<br>
First thing first, we should identify the archives formats. Using binwalk, apparently they are splitted to two types - Zips and Rars.<br><br>

In the description, they mention that there is something in the comments of each file. After running a quick check using unzip (for the Zips) and unrar (for the Rars), it seems that every file has the comment in format of "[letter],[number]".<br>
Ok, nice. So like you should guess, the letters should be the flag's content. But what is the number?<br><br>

My first thought was the it's the index or the number in the name of the archive. But then I encounter with a negative one.<br>
So, this must be a "jump". E.g, for the comment "W,1062" in unzipme.0, the letter "W" should be added to the flag and then we should move to 0+1062=1062 file (unzipme.1062). For the commment "e,530" in unzipme.1062, the letter "e" should be added to the flag and then we should move to 1062+530=1592 (unzipme.1592). For the comment "l,390" in unzipeme.1592, the letter "l" should be added to the flag and then we should move to 1592+390=1982 (unzipme.1982). For the comment "l,-831" the letter "l" should be added to the flag and we should move to 1982-831=1151 (unzipme.1151).<br><br>

And so on...<br>
So I wrote a python script that will that, and added to it a limit of jumps (so it won't get into an endless loop).<br>
The first limit I chose was 200, and I got the following message:  
> Welldonebuddy!Youseemtobeabletostepcarefullythroughthefiles.Thisisyourflag:flag{ARc#vies_Are_The_Best}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

It has no spaces but I can still read this message. And it seems like there is an endless loop which will add the "}" character to the message. After playing with the limits, I found out that 120 is the golden value:
> Well done buddy!You seem to be able to step carefully through the files.This is your flag:**flag{ARc#vies_Are_The_Best}**

(I add the whitespaces between the words)  
Sweet :sunglasses: I liked this challenge! Another 20 points for me.

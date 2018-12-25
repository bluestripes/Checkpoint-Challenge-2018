> Protocol  
> Hi there!  
> We need to extract secret data from a special file server.  
> We don't have much details about this server, but we did manage to intercept traffic containing communication with the server.  
> We also know that this secret file's path is: /usr/SeCret.txt  
> You can find the sniff file [here](https://s3.eu-central-1.amazonaws.com/csh-static/protocol/309958e3de79da065908366e1635603c7bd573561fd95752791be72a.pcap).  
> Please tell us what the secret is!  
> Good luck!  

So likes the description mentioned, there is a pcap file. The challenge is like finding a needle in a haystack so I needed to filter out some frames.  
Because we are looking for a txt file, I assumed that the file extension ".txt" should appear in one of the frames.  
So, I opened the pcap file in Wireshark and entered the filter *frame contains ".txt"*. The result was one frame.   
Next, I wanted to see all the "conversion" that the frame is included in. So I followed the TCP stream of it (Wireshark is awesome!).  
I got the following stream between 35.157.111.68:20076 to 10.10.11.7:55815 :

> 0 8 Welcome!  
> 1 5 HELLO  
> 1 5 HELLO  
> 2 3 XOR  
> 2 4 19C0  
> 3 18 /usr/chocolate.txt  
> 3 252 0x5aa80x76a30x76ac0x78b40x7ce00x70b30x39a70x6ba50x78b40x35e00x70b40x39a70x70b60x7cb30x39b90x76b50x39a50x77a50x6ba70x60e00x6ea80x70a30x71e00x7aa10x77e00x7ba50x39b50x6aa50x7de00x6daf0x39a70x76e00x7bb50x60e00x74af0x6ba50x39a30x71af0x7aaf0x75a10x6da50x19ee  

From first glance, it's clear that the commands' format is: <command's id> <command's length> <command>.
In another glance it looks like that the user suppose to get a "xor key" and then it can ask for a file.
So, because I'm no so good at math (or xoring) I wrote a python script that will do it for me (in this repository).  
At first it will send the "1 5 HELLO" command.   
Next, the "2 3 XOR" command.  
And for last, asking for /usr/SeCret.txt.

After the first run, the remote program answered with the flag **flag{you_haVe_Got_It!}**.  
I like the pcap analysis challenges, and it was a cute/easy one (and worths 30 points).

> Diego's Gallery  
> Recently I've been developing a platform to manage my cat's photos and keep my flag.txt safe. Please [check out](http://35.194.63.219/csa_2018/diegos_gallery/_mdbrypbibxrz/).
> To avoid security loop holes such as SQL injections I developed my own scheme.  
> A short description is available [here](http://35.194.63.219/csa_2018/diegos_gallery/_mdbrypbibxrz/scheme.txt)

The description implies that a kind of SQL injection is going to be used.  
When Diego's gallery's site, there is a registration form, where the user can put a username and password, and sign-up in order to see the 9 photos of Diego's cat (WTF?!).  
After taking a look at the scheme Diego developed, it looks pretty straight forward.  

> Every line in my DB look's like this:  
> START|||username|||password|||role|||END

So in order to exploit it, the input for the username field should be _<any username>_|||_<any_password>_|||admin|||END\nSTART|||_<any_username>_, and in the password input field there should be anything.  
This inputs should add 2 lines to the database: one for a new admin account and the other for the regular account.  

And viola! a [admin-panel](http://35.194.63.219/csa_2018/diegos_gallery/_mdbrypbibxrz/admin-panel/index.php?view=log.txt) was opened.  
This page contains 2 buttons (whose both alerts "Not implemented yet") and a text area containing an error log.  
If you'll look at the address you'll see a get request with the parameter view=log.txt. Suspicious.  
It's pretty obvious that the view paramter should be changed from **log.txt** to **flag.txt**.   
So I changed it and found the flag **flag{M3Ow_MeOw_M3Ow}** in the text area where the error log was.

This challenge pretty basic as well, and worth 20 points. The CTF engine getting warmer.

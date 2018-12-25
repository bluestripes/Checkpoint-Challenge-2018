> Return Of The Robots  
> Robots are cool, but trust me: their access should be limited!  
> [Check it out](http://35.194.63.219/csa_2018/return_of_the_robots/_avnznothmlyp/)
  
When starting a test on a website, every pentester will check the robots.txt (as the first thing). So I did it and came with the following records:  

> User-agent: *  
> Disallow: /secret_login.html

Well secret_login.html. :unamused:  
So I opened [this path](http://35.194.63.219/csa_2018/return_of_the_robots/_avnznothmlyp/secret_login.html), and found a found a password input.
I tried a blind random password, a got the alert "Try Again!". So, javascript is involved here.  

>	function r(n){for(var r=0,o=0,e="",t=0;t<n.length;t++)n[t].toLowerCase()!=n[t]&&(r+=1),8==++o?(e+=String.fromCharCode(r),r=0,o=0):r<<=1;alert(e)}  
> function auth(n){if("SzMzcFQjM1IwYjB0JDB1dA=="==btoa(n))var a="mYSqyDYmwBYzNOdhnLDzljcTtTIpiVBCjIHOAmJNmNSXrkIvyQRaTOLJhQWmroOrdJRfSTVZdBZQsYajfJPGxrWMfVqRPCQKdCuVjgSQtPyScJkkzJapmwyDiXXCRieNxVEYRBQmfFBsUAQKuLQMfTgTrEMAuIyiyoJzhvcZevLhhzvLlgFyzaoKmKCGJNlY";else a="sRnDjXnrzAZVoxXnjSWLUoyWtgQpzziflCuxapkGjYEcrUADyMZlgunEaXLqYncWlHGpIVMvltZxveoE";r(a)}
		
As you can see there is a "auth" function (which is suspicious) and a "r" function.  
So of course I checked the "auth" function. In it there is an if, that checks if the function's input in base64 form is equals to "SzMzcFQjM1IwYjB0JDB1dA==".  
SzMzcFQjM1IwYjB0JDB1dA== is K33pT#3R0b0t$0ut. Looks promising for the password.  

After inserting this to the password input, I got the alert with the flag **flag{robots_STAy~out!!!}**

This challenge is pretty basic, and worth 10 points. But a pretty cute way to start.

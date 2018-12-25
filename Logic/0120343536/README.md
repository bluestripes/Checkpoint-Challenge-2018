> 0120343536  
> flag{JXNHBJC_CDQCYOYDYO$I_LBC_B_H$NNOQRX_O@XB}
> Not so fast...  
> They say the only place where flags come before work is the dictionary, [ours](http://35.194.63.219/csa_2018/0120343536/_ffcqlscwljgz/dictionary.txt) is no different  
> Note: flag letters are all capital  

It looks like that flag's content is scrambled and we should find the equivalent words/letters in the given dictionary.<br><br>
The easiest letter to start with is "B". In the dictionary contains 2 words with 1 letters - "A" and "B". I guess it's "B"="A".<br><br>
Next, let's take a look at "LBC". "B"="A", so we are looking for 3-letters words in the dictionary with "A" in the middle. The options are "DAD", "GAG", "NAN" and "WAS". Because the first letter is not the same as the last letter, the only option is "WAS".<br><br>
Awesome, so "B"="A", "L"="W", "C"=S.  
Now, let's take a look at "XNHBJC". We know that the 5th letter is "A" and the last letter is "S". In addition, we know that the first letter and the 6th letter are the some. The options in the dictionary are "MCADAMS", "PERHAPS", "SURPASS". "MCADAMS" is not good because the third letter is not "B" in "JXNHBJC". "SURPASS" is not good as well because "C" is not the first letter in "JXNHBJC". So this leaves us with "PERHAPS".<br><br>

Great! We found out that "B"="A", "L"="W", "C"=S, "J"="P", "X"="E", "N"="R" and "H"="H".  
Continuing to "O@XB". The third letter should be "E" and the last character should be "A". The only options are "AREA" and "IDEA". We know that "N"="R", so "AREA" is not an option. So, "IDEA" is the only one.<br><br>

Easy. We found out that "B"="A", "L"="W", "C"=S, "J"="P", "X"="E", "N"="R", "H"="H", "O"="I" and "@"="D".  
From here it's pretty easy. The only option for "H$NNOQRX" is "HORRIBLE" and the only option for "CDQCYOYDYO$I" is "SUBSTITUTION".<br><br>

So, the flag is **flag{PERHAPS_SUBSTITUTION_WAS_A_HORRIBLE_IDEA}**. Nice, 60 points.

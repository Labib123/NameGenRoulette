NameGenRoulette is a program that gereates names for startup and cross-check if the domian name exists and show the user a name with available domain name 

How it works! 

1- Using ebird.api as a wordlist to find the potential startup name. Can use other api though   
2- open up godaddy.com using selenium webdriver  
3- look up the domain name  
4- if the .com is available then print name to the screen 
5- let the user decide wherther to continue or to open up the site by using command-based interface menu.py 

Installation

pip install selenium
pip install ebird-api
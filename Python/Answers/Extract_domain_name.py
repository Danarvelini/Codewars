#https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

#TODO
from urllib.parse import urlparse

def domain_name(url):
    domain = urlparse(url).netloc
    return domain
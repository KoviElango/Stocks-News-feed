import spacy
import pandas as pd
import requests
import streamlit as st
from bs4 import BeautifulSoup

st.title("Buzzing Stocks :zap:")

def extract_text_from_rss(rss_link):
    #this will parse XML and extract headings from links in a python list
    headings = []
    r1=requests.get("https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms")
    r2=requests.get(rss_link)
    soup1 = BeautifulSoup(r1.comtent, features = 'lxml')
    soup2 = BeautifulSoup(r2.comtent, features = 'lxml')
    headings1 = soup1.findAll('title')
    headings2 = soup2.findAll('title')
    headings = headings1 + headings2
    return headings

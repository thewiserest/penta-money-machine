from yahoo_finance import Share
import yfinance as yf
import streamlit as st
import pandas as pd

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

icon("search")
st.markdown("**Type the Ticker Symbol name into the textbox below (Apple as AAPL), then Hit the Button.**")
selected = st.text_input(" ", "AAPL")
button_clicked = st.button("Submit")


#
stock = yf.Ticker(selected)

# get stock info
dic=stock.info

name= dic['shortName']
marketCap = dic['marketCap'] ###stock price time oustanding shares
enterpriseValue = dic['enterpriseValue']   ### marketcap+debt-cash
currency=  dic['currency']              ### what is the currecy
out=dic["sharesOutstanding"]
priceop=dic["regularMarketOpen"]
priceend=dic["previousClose"]

x=(str('{:,}'.format(marketCap))+" "+currency)
y=(str('{:,}'.format(enterpriseValue))+" "+currency)
a=(str('{:,}'.format(priceop))+" "+currency)
b=(str('{:,}'.format(priceend))+" "+currency)
q=(str('{:,}'.format(out))+" "+"Shares")

st.write(pd.DataFrame({'Title': ["Company", "Enterprise Value", "Market Capitalization","Shares Outstanding","Regular Market Open Price","Previous Close Price"],
                     'Vaule': [name, y, x, q,a,b]}))
st.markdown("**Don't Know the Stock Ticker Look it Up Below**")
st.components.v1.iframe(src="https://en.wikipedia.org/wiki/Lists_of_companies_by_stock_exchange_listing", width=850, height=250, scrolling=True)








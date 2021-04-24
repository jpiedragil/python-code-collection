'''
speedtest.py

Source code for "Internet Speed Test"(https://bit.ly/32PlVAF) article,
written by Ayushi Rawat
'''
# Import necessary module
#
import speedtest

st = speedtest.Speedtest()

# Fetch the dwonload speed
#
d_st = st.download()

# Fetch the upload speed
#
u_st = st.upload()

# Fetch ping
st.get_servers([])
ping = st.results.ping

# Display the result
#
print("Your ping is", ping)
print("Your download speed is", d_st)
print("Your upload speed is", u_st)

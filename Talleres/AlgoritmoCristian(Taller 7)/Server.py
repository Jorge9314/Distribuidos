import xmlrpc.client
import time

s = xmlrpc.client.ServerProxy('http://localhost:8001')

"""
print(s.timew())
print(s.timep())
time.sleep(1)
print(s.timew())
time.sleep(1)
print(s.timep())
"""
print(s.sinc())
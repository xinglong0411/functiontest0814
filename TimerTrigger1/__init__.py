import requests

url = "https://api.support.microsoft.com/v0/queryidresult"

payload = "{\"query_parameters\":[{\"name\":\"selectedRCID\",\"values\":[\"975796e2-7621-df11-aa33-001b78438cb4\"]},{\"name\":\"severity\",\"values\":[\"1\",\"2\",\"3\",\"4\"]},{\"name\":\"aadUpn\",\"values\":[\"xinzhen@microsoft.com\"]}],\"queryid\":\"UNASSIGNED_CASES_MYCASES\"}"
headers = {
  'MS-CV': 'pKtCxYWtyvjKwH+O3G5OT4.15.91',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Imh1Tjk1SXZQZmVocTM0R3pCRFoxR1hHaXJuTSIsImtpZCI6Imh1Tjk1SXZQZmVocTM0R3pCRFoxR1hHaXJuTSJ9.eyJhdWQiOiI1NmJjMDQ0Yy03NjQ0LTRiZTYtYmM1Mi0zN2QxNzhiNWE2NDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWF0IjoxNTk1OTM4NTgzLCJuYmYiOjE1OTU5Mzg1ODMsImV4cCI6MTU5NTk0MjQ4MywiYWlvIjoiQVdRQW0vOFFBQUFBNGdQQ2QrdEMvU1dVeEtWMmwwSHhialdsQlVpci9TRytrOUxkYnhkcjBIaUV0d1RJZG1lcGtSeTJ0VWFTM2xEUGhQSysrVEN4U3FSb2tSWTVVNHNWKzJBczd4Y3pvQTFHL3E0L3hXTEl0ei9YMWluK1VZc3N5WTI2TGZ0eWJWcHIiLCJhbXIiOlsicnNhIiwibWZhIl0sImZhbWlseV9uYW1lIjoiWmhlbmciLCJnaXZlbl9uYW1lIjoiRGVubmlzIiwiaXBhZGRyIjoiMTY3LjIyMC4yNTUuMjIiLCJuYW1lIjoiRGVubmlzIFpoZW5nIiwibm9uY2UiOiJhZWU2MmYzZi03OGUzLTQ5ZjYtOGQzMi1kYjVmNDc4ZDU0M2UiLCJvaWQiOiJkYzVkOTQ2My0zMjk2LTQ2ZDEtYjI4NS1jODk4ZmE0MThmYjYiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjE0Njc3MzA4NS05MDMzNjMyODUtNzE5MzQ0NzA3LTI0Nzc0MzEiLCJyaCI6IjAuQVFFQXY0ajVjdkdHcjBHUnF5MTgwQkhiUjB3RXZGWkVkdVpMdkZJMzBYaTFwa0FhQU44LiIsInN1YiI6InJ5Nkw3cThUMkpFamt3RHFpLXdhNVF0UlpVeHdWN2ZSeFFQSnZqd2hZMlUiLCJ0aWQiOiI3MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDciLCJ1bmlxdWVfbmFtZSI6InhpbnpoZW5AbWljcm9zb2Z0LmNvbSIsInVwbiI6InhpbnpoZW5AbWljcm9zb2Z0LmNvbSIsInV0aSI6IlkwSVJ2MV9UM0VpREtkc0poLUFQQUEiLCJ2ZXIiOiIxLjAifQ.neK8NKPrCnc55Djxt8ikSDDLJtZkqvERRNc5XHeTdAJ7jsGly1r8yIXJv0JTpd3g4jIxxWwdWc3a5eofYPvMmCLHNRTkQYgc8lTBdqrHE6bI1i0-INkhTovxA4tat1qbq1lbwouVxW0s1BKLuK_ElIVphZ7e_b_UugYdy3HVInpDfanxt1wDhZRxZWO-izWbYPz9ae3VtJ-AvzxxnwT52cM31udeHJQFMCIjm7yxbc1HswUWy48tbJ88SZjnOIOZk0lLYqo-mBMcDUMxEPH6-pD-pgVqjGhyPpbBP7NzBgDMKBQLJXci_-Byq9I6Ek1JipTSlaAwh7IBKwTEUsjxNQ',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
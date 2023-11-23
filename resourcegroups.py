import requests
import json

url = "https://management.azure.com/subscriptions/0ae17f0e-d317-4a45-915a-5029e257e1ca/resourcegroups/lab4?api-version=2021-04-01"

headers = {
    'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE3MDA3NTQ4MDEsIm5iZiI6MTcwMDc1NDgwMSwiZXhwIjoxNzAwNzYwMDkwLCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBQjVDK1FQK3NFa0JrVzRLRXVCK2MwRnhTMWR1UGFocExkbHBnQlhaTmkzM3RTV3dOUFA4K2Y0VGxVQzd6VXd3b25vTFRGUGlFc0d4SWZFRWdDL0xwU3hzVzByb1JkdmpGTkIrRmwyTDZ6bms9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTmpva3UiLCJnaXZlbl9uYW1lIjoiTWljaGFlbCIsImdyb3VwcyI6WyI4MTA4YzUwMy1kNjU2LTQyY2YtOGVlNC04OTQ0YWVmMGZhZGUiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4N2Y2MDAzZC05NDcwLTQzOGYtYmZlZi04MTNiMzdmYzJiNjgiLCI4MzhhMjg5YS04NGE0LTRjYTgtYWVlYy1iMzFlYzFkNzFkNGEiLCI0ZGMwM2I5Zi0xYjZjLTQ0MTUtYWMwNS04MjQyNzEzYzc1MjAiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiLCJhYmQ0OWRmZC1jZWZiLTRjMzYtYWQ2Ny0yNWZkOWZmZDMzN2YiXSwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTQ3LjI1Mi4xOS45MCIsIm5hbWUiOiJDMjEzMTQxODYgTWljaGFlbCBOam9rdSIsIm9pZCI6IjAyMjkwZjk3LTNlMTctNGRiNC04YTVlLWI3YzZiMjI0NmJmOSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MDIyOTg4NDktMTczNDcwNTEzMS0zMTIwMDI0MDAxLTQzOTI4IiwicHVpZCI6IjEwMDMyMDAxODMxRUNEQ0EiLCJyaCI6IjAuQVRFQXl4ZGpka2pwWDA2TTdOcThqaV9WMmtaSWYza0F1dGRQdWtQYXdmajJNQk14QU5vLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6IjJHUFZibHV1Q3Y2eWhRcER4ck9pal9SWlJFbXhEbmFBR29YV1lWcEZ5bmciLCJ0aWQiOiI3NjYzMTdjYi1lOTQ4LTRlNWYtOGNlYy1kYWJjOGUyZmQ1ZGEiLCJ1bmlxdWVfbmFtZSI6IkMyMTMxNDE4NkBteXR1ZHVibGluLmllIiwidXBuIjoiQzIxMzE0MTg2QG15dHVkdWJsaW4uaWUiLCJ1dGkiOiJ6bXhXM1p4aGgwaXZabkMyRzlFUEFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.oBAIGvKctJrujVev7Nda6EezuKlBWeBM9I63vFjopKuRYUT7313uN2HR4NwDgIwcv_EyIagKl1ktbm5FAZQxtQsHCycvFR91Rhcp0JFoOKPFocVj8-ptWHL9Ajj9Jyz_GYlu2fG_WGfcfHyYHUbckFQLaqs0mTKgTv_roBPsQvNrKUmL89mCSn9-MiAT-OLyKfrp9N5Rv1jXcg1aFWOuUlC1_Hvjv8j4CeUTiojGyExudK66ObCNmLiyriXkX1qm8GxfVCN24A4AJTn8OAeJRB91ZHDEXA3po16rvzZlAKiksKSchdu7yXeO9wjjnm5ApbpJha8s-SDlmYDl8yjoGQ',
    'Content-type': 'application/json'
}

data = {

    'location': "westeurope"

}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
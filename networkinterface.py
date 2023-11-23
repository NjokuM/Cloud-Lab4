import requests
import json

url = "https://management.azure.com/subscriptions/0ae17f0e-d317-4a45-915a-5029e257e1ca/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/nic4?api-version=2023-05-01"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE3MDA3NTUzMTMsIm5iZiI6MTcwMDc1NTMxMywiZXhwIjoxNzAwNzU5NTEzLCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBSVpXTXoyOGtMckM0QXFaUGg5clk0c2x0SEVXM01TZHUxVW5PMEFqZ1YwS3lGME5McTBjZGFuQTROZGt5U251NVk4bEZsOFVYbktuZ2dnRkcranhITnlYZENia0pCY1p6VnMxY0dCczNKL2s9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTmpva3UiLCJnaXZlbl9uYW1lIjoiTWljaGFlbCIsImdyb3VwcyI6WyI4MTA4YzUwMy1kNjU2LTQyY2YtOGVlNC04OTQ0YWVmMGZhZGUiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4N2Y2MDAzZC05NDcwLTQzOGYtYmZlZi04MTNiMzdmYzJiNjgiLCI4MzhhMjg5YS04NGE0LTRjYTgtYWVlYy1iMzFlYzFkNzFkNGEiLCI0ZGMwM2I5Zi0xYjZjLTQ0MTUtYWMwNS04MjQyNzEzYzc1MjAiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiLCJhYmQ0OWRmZC1jZWZiLTRjMzYtYWQ2Ny0yNWZkOWZmZDMzN2YiXSwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTQ3LjI1Mi4xOS45MCIsIm5hbWUiOiJDMjEzMTQxODYgTWljaGFlbCBOam9rdSIsIm9pZCI6IjAyMjkwZjk3LTNlMTctNGRiNC04YTVlLWI3YzZiMjI0NmJmOSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MDIyOTg4NDktMTczNDcwNTEzMS0zMTIwMDI0MDAxLTQzOTI4IiwicHVpZCI6IjEwMDMyMDAxODMxRUNEQ0EiLCJyaCI6IjAuQVRFQXl4ZGpka2pwWDA2TTdOcThqaV9WMmtaSWYza0F1dGRQdWtQYXdmajJNQk14QU5vLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6IjJHUFZibHV1Q3Y2eWhRcER4ck9pal9SWlJFbXhEbmFBR29YV1lWcEZ5bmciLCJ0aWQiOiI3NjYzMTdjYi1lOTQ4LTRlNWYtOGNlYy1kYWJjOGUyZmQ1ZGEiLCJ1bmlxdWVfbmFtZSI6IkMyMTMxNDE4NkBteXR1ZHVibGluLmllIiwidXBuIjoiQzIxMzE0MTg2QG15dHVkdWJsaW4uaWUiLCJ1dGkiOiJBYWY3anBSOGRrQ21RUDk2bndULUFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.eNyGQRt00iOW3rOc3STJHU_h97YegjLZQRnADgYlUvWWtWrGfuH4dkrQkPEUzYzKeT4EhgWu58kVUgFKLBLOldtZCxDwiA_X0JTLn_OcZ8UtZOKY1PEuOSx5Kn-ngBbhShvEJahgXozx7OVp-pt55NuIXKhkkJQ64GQaJjPbsJzgRrO0fk7mn-gsnIPU99iu85OPZHP4oDFhlm8tITzKd6UkySUcu8N_ZP09CsxYu7I_3NZoKHPy5v6OUj3pk7IDCAmngvk3aPUy_kBSex41uI4BOgK9IgiRocJDGLfJd1PJmdMiZZ2lq3fgM8LgA70hHiLzuSTH1UoSInrf_CyeMA'
}

data = {
    "properties": {
        "ipConfigurations": [
            {
                "name": "ipconfig1",
                "properties": {
                    "publicIPAddress": {
                        "id": "/subscriptions/0ae17f0e-d317-4a45-915a-5029e257e1ca/resourceGroups/lab4/providers/Microsoft.Network/publicIPAddresses/ip4"
                    },
                    "subnet": {
                        "id": "/subscriptions/0ae17f0e-d317-4a45-915a-5029e257e1ca/resourceGroups/lab4/providers/Microsoft.Network/virtualNetworks/net4/subnets/snet4"
                    }
                }
            }
        ]
    },
    "location": "westeurope"
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
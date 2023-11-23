import requests
import json

url = "https://management.azure.com/subscriptions/0ae17f0e-d317-4a45-915a-5029e257e1ca/resourceGroups/lab4/providers/Microsoft.Compute/virtualMachines/vm4?api-version=2023-07-01"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE3MDA3NTU1NTgsIm5iZiI6MTcwMDc1NTU1OCwiZXhwIjoxNzAwNzU5NjI1LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBa1BsTXpuMkRsOXdRSFYyN2MraU1hOTdZalhUQ1BPc0VtenJNOHJGUnVWUXczWTJvRUR5MkpzRDdwclhlZDBPZnRRc1hBNVJaMlNWUVJra3M5Zkluc1d6UlNGK1BCTmZ2T2J0RGJNSE02K3c9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiTmpva3UiLCJnaXZlbl9uYW1lIjoiTWljaGFlbCIsImdyb3VwcyI6WyI4MTA4YzUwMy1kNjU2LTQyY2YtOGVlNC04OTQ0YWVmMGZhZGUiLCI5N2FmODEyZC05NmU5LTRmMDEtOGExMS03NTgwMzM3NjIxN2EiLCI4N2Y2MDAzZC05NDcwLTQzOGYtYmZlZi04MTNiMzdmYzJiNjgiLCI4MzhhMjg5YS04NGE0LTRjYTgtYWVlYy1iMzFlYzFkNzFkNGEiLCI0ZGMwM2I5Zi0xYjZjLTQ0MTUtYWMwNS04MjQyNzEzYzc1MjAiLCI1YWQ3ZDZiNC1hZGFmLTRiOWQtOTU3Zi0wZjNiNjE0YmVlNjAiLCI4YWMxNTRkZC1kNDVmLTRjNDYtOTRlNS1iYjc4ZmVmYTNhZWYiLCI4YzgxODZlYS00MmE0LTQ0YWYtOGE3OC1hZTkxNDAxMWU2YjQiLCJkMmE2YThlZi00ZDI2LTRkOTUtYmQxMS1hYTFlYzYxOWY4MTgiLCJhYmQ0OWRmZC1jZWZiLTRjMzYtYWQ2Ny0yNWZkOWZmZDMzN2YiXSwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTQ3LjI1Mi4xOS45MCIsIm5hbWUiOiJDMjEzMTQxODYgTWljaGFlbCBOam9rdSIsIm9pZCI6IjAyMjkwZjk3LTNlMTctNGRiNC04YTVlLWI3YzZiMjI0NmJmOSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MDIyOTg4NDktMTczNDcwNTEzMS0zMTIwMDI0MDAxLTQzOTI4IiwicHVpZCI6IjEwMDMyMDAxODMxRUNEQ0EiLCJyaCI6IjAuQVRFQXl4ZGpka2pwWDA2TTdOcThqaV9WMmtaSWYza0F1dGRQdWtQYXdmajJNQk14QU5vLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6IjJHUFZibHV1Q3Y2eWhRcER4ck9pal9SWlJFbXhEbmFBR29YV1lWcEZ5bmciLCJ0aWQiOiI3NjYzMTdjYi1lOTQ4LTRlNWYtOGNlYy1kYWJjOGUyZmQ1ZGEiLCJ1bmlxdWVfbmFtZSI6IkMyMTMxNDE4NkBteXR1ZHVibGluLmllIiwidXBuIjoiQzIxMzE0MTg2QG15dHVkdWJsaW4uaWUiLCJ1dGkiOiJENUxHMk0wY3MwdWo2bXRSUXNFNEFRIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NhZSI6IjEiLCJ4bXNfdGNkdCI6MTUyNTMzODk0MX0.X1zQAugfs1mIejIFrxQSewTWe2o98jP7j-xO95Z20G3pK50N5jQl8RUibEoWpGWPOHNTISmOvTvE49Q2Z_ZN9IlxBBMWgrcdLfeocquPd_PuHNUIAmWxrOYvTYfPJHoe4MPslptZwLAE4TRAp2qJgHzMrnGw0uBj3_oqazv5To8FiFYzSCIcuisdnk7iQTOEvJsJc6-tLIwhh2_dJX3g5xY4xSU7bM4nGxDon92uetjKGCTWSSgcTuYb8EJVEWe1yYwGgyoXGXaSA1nR7mExeCyXFpRw1Y-FPgwNAf_r8lD42elVUNLzflNQe9YEz4URCopv8HYXxWMLJFaEJhlqbQ'
}

data ={
    "id": "/subscriptions/0ae17f0e-d317-4a45-915a-5029e257e1ca/resourceGroups/lab4/providers/Microsoft.Compute/virtualMachines/vm4",
    "type": "Microsoft.Compute/virtualMachines",
    "properties": {
      "osProfile": {
        "adminUsername": "paul",
        "secrets": [
         
        ],
        "computerName": "vm4",
        "linuxConfiguration": {
          "ssh": {
            "publicKeys": [
              {
                "path": "/home/paul/.ssh/authorized_keys",
                "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsxP2gmr2VhefmSeB07WtVpOP3IquuVmGgx23jjW7i hA+rJjsUnEA/ uf5a9Qr5tvA3fDlaADTKOn8A54j2KVut1My4soro4YL5ziyiIYjzcn9CCI7EUscB41f1vNQqGuhvJot2 UB4mKRLDgJgtCUzM5jm5Su32yJQa1Zybl9uxyU/ BFnK3JFiynoMl30ADbZYBz6owc4+yFJDy46l0SiAiOJRKlPQmrH10YMnWQyiFrON07b2RJRyPr80 QXt9t+ynWGwJeO5nv1WQZirNVuzze1yWCQtQ8L3ySFSj9LA3Xw2n34NEWUvK6PMGmJf1+Fnx jVzC6KxExKkglXXfcv8N9 paul@paul "
              }
            ]
          },
          "disablePasswordAuthentication": True
        }
      },
      "networkProfile": {
        "networkInterfaces": [
          {
            "id": "/subscriptions/0ae17f0e-d317-4a45-915a-5029e257e1ca/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/nic4",
            "properties": {
              "primary": True
            }
          }
        ]
      },
      "storageProfile": {
        "imageReference": {
          "sku": "16.04-LTS",
          "publisher": "Canonical",
          "version": "latest",
          "offer": "UbuntuServer"
        },
        "dataDisks": [
         
        ]
      },
      "hardwareProfile": {
        "vmSize": "Standard_D1_v2"
      },
      "provisioningState": "Creating"
    },
    "name": "vm4",
    "location": "westeurope"
  }

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
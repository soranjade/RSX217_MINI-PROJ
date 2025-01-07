import requests
import json

url = "http://localhost:8181/onos/v1/flows?appId=dijto"

payload = json.dumps({
  "flows": [
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": True,
      "deviceId": "of:00000000000000e1",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "3"
          }
        ],
        "deferred": []
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": 1
          },
          {
            "type": "ETH_SRC",
            "mac": "00:00:00:00:00:01"
          },
          {
            "type": "ETH_DST",
            "mac": "00:00:00:00:00:03"
          }
        ]
      }
    },
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": True,
      "deviceId": "of:00000000000000c1",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "4"
          }
        ],
        "deferred": []
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": 3
          },
          {
            "type": "ETH_SRC",
            "mac": "00:00:00:00:00:01"
          },
          {
            "type": "ETH_DST",
            "mac": "00:00:00:00:00:03"
          }
        ]
      }
    },
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": True,
      "deviceId": "of:00000000000000e2",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "1"
          }
        ],
        "deferred": []
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": 3
          },
          {
            "type": "ETH_SRC",
            "mac": "00:00:00:00:00:01"
          },
          {
            "type": "ETH_DST",
            "mac": "00:00:00:00:00:03"
          }
        ]
      }
    },
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": True,
      "deviceId": "of:00000000000000e2",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "3"
          }
        ],
        "deferred": []
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": 1
          },
          {
            "type": "ETH_DST",
            "mac": "00:00:00:00:00:01"
          },
          {
            "type": "ETH_SRC",
            "mac": "00:00:00:00:00:03"
          }
        ]
      }
    },
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": True,
      "deviceId": "of:00000000000000c1",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "3"
          }
        ],
        "deferred": []
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": 4
          },
          {
            "type": "ETH_DST",
            "mac": "00:00:00:00:00:01"
          },
          {
            "type": "ETH_SRC",
            "mac": "00:00:00:00:00:03"
          }
        ]
      }
    },
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": True,
      "deviceId": "of:00000000000000e1",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "1"
          }
        ],
        "deferred": []
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": 3
          },
          {
            "type": "ETH_DST",
            "mac": "00:00:00:00:00:01"
          },
          {
            "type": "ETH_SRC",
            "mac": "00:00:00:00:00:03"
          }
        ]
      }
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic a2FyYWY6a2FyYWY='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# oneapp_proxyserver

Very(very) basic initial implementaion of the Proxy Server.
proxy_server.py: Python file that handles requests coming over ws and publishes them to 0mq pub/sub. Also, subscribes for messages from middleware and sends them to the UI client.
sub.py: mock implementation of middleware
ws_client.py: mock implementation of UI 

Requires: python3.6

Steps:
1. python3.6 sub.py
2. python3.6 proxy_server.py
3. python3.6 ws_client.py

Current Implementation:
1. When the ws_client is started, a JSON string is pushed to the websoclet. 
2. Proxy server gets the request and publishes it to a 0mq pub
3. a 0mq subscriber (sub.py) listens to incoming messages and creates a mock JSON string response object.
4. Proxy Server receives this message and sends it to the UI (ws_client) over websockets

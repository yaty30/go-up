import websocket
import json
import pandas as pd

assets = ['BTCUSDT']
assets = [sym.lower() + '@kline_1m' for sym in assets]
assets = "/".join(assets)

def on_message(ws, message):
    message = json.loads(message)
    manipulation(message)

def manipulation(source):
    # Extract the relevant data
    kline = source['data']['k']
    close_price = kline['c']
    evt_time = pd.to_datetime(kline['t'], unit='ms')
    
    # Create DataFrame
    df = pd.DataFrame([[close_price]], columns=[source['data']['s']], index=[evt_time])
    df.index.name = 'timestamp'
    df = df.astype(float)
    
    print(df)

socket = "wss://stream.binance.com:9443/stream?streams=" + assets
ws = websocket.WebSocketApp(socket, on_message=on_message)
ws.run_forever(sslopt={"cert_reqs": 0})
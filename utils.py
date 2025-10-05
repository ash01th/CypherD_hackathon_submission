import requests
import json

def get_eth_for_usd(usd_amount: float):
    """Queries the Skip API to get the ETH equivalent for a given USD amount."""
    api_url = "https://api.skip.build/v2/fungible/msgs_direct"
    
    payload = {
      "source_asset_denom": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
      "source_asset_chain_id": "1",
      "dest_asset_denom": "ethereum-native",
      "dest_asset_chain_id": "1",
      "amount_in": str(int(usd_amount * 10**6)), # USDC has 6 decimals
      "chain_ids_to_addresses": {"1": "0x742d35Cc6634C0532925a3b8D4C9db96c728b0B4"},
      "slippage_tolerance_percent": "1",
      "smart_swap_options": {"evm_swaps": True},
      "allow_unsafe": False
    }
    
    #headers = {"accept": "application/json", "content-type": "application/json"}

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        data = response.json()
        # The amount is located inside the 'route' object in the response
        route_info = data.get("route", {})
        amount_out_wei = int(route_info.get("amount_out", 0))
        
        # Convert from wei (10^18) to ETH
        return amount_out_wei / 10**18 if amount_out_wei > 0 else None
        
    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Response Parsing Error: {e}")
        
    return None



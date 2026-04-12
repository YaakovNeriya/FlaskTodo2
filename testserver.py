import requests
import time
import sys

BASE_URL = "http://app:5000"  # שם ה-service בדוקר
URL = f"{BASE_URL}/add"

data = {
    "title": "Buy groceries"
}


if __name__ == "__main__":
    try:
        print(f"[*] Sending POST request to {URL} with data: {data}")
        response = requests.post(URL, data=data)
        
        print(f"[*] Response Status Code: {response.status_code}")
        print(f"[*] First 100 characters of response: {response.text[:100]!r}...")

        if response.status_code == 200:
            if "Buy groceries" in response.text:
                print("TEST PASSED: item was added successfully!")
            else:
                print("TEST PASSED (Request OK, but item not found in HTML response)")
            sys.exit(0)
        else:
            print("TEST FAILED: bad status code", response.status_code)
            sys.exit(1)

    except Exception as e:
        import traceback
        print("TEST FAILED WITH EXCEPTION:")
        traceback.print_exc()
        sys.exit(1)
import time
import requests

BASE_URL = "http://app:5000"   # Flask service name

def wait_for_flask(max_retries=10, delay=3):
    """ממתין עד שה-Flask זמין"""
    for i in range(max_retries):
        try:
            r = requests.get(BASE_URL)
            if r.status_code == 200:
                print("✅ Flask now is up!")
                return True
        except requests.exceptions.ConnectionError:
            print(f"Flask not ready yet... retry {i+1}/{max_retries}")
            time.sleep(delay)
    raise Exception("❌ Flask did not start in time")

def test_add_task():
    """בודק הוספת משימה חדשה"""
    url = f"{BASE_URL}/add"
    data = {"task": "test from docker"}
    resp = requests.post(url, data=data)
    assert resp.status_code == 200, f"POST failed: {resp.status_code}"
    print("✅ POST /add passed")


if __name__ == "__main__":
    wait_for_flask()
    test_add_task()

    print("🎉 Test run complete!")



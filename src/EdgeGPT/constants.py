import socket
import uuid

take_ip_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
take_ip_socket.connect(("8.8.8.8", 80))
FORWARDED_IP: str = take_ip_socket.getsockname()[0]
take_ip_socket.close()

DELIMITER = "\x1e"
# Generate random IP between range 13.104.0.0/14
# FORWARDED_IP = f"1.0.0.{random.randint(0, 255)}"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82"

HEADERS = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "accept-encoding": "gzip, deflate, br, zsdch",
    "content-type": "application/json",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"114.0.1823.82"',
    "sec-ch-ua-full-version-list": '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.82"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"14.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-ms-gec-version": "1-114.0.1823.82",
    "x-ms-client-request-id": str(uuid.uuid4()),
    "x-ms-useragent": "azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.10.3 OS/Windows",
    "referer": "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx",
    "referrer-policy": "origin-when-cross-origin",
    "x-forwarded-for": FORWARDED_IP,
}

HEADERS_INIT_CONVER = {
    "authority": "www.bing.com",
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"114.0.1823.82"',
    "sec-ch-ua-full-version-list": '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.82"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"14.0.0"',
    "upgrade-insecure-requests": "1",
    "user-agent": USER_AGENT,
    "x-edge-shopping-flag": "1",
    "x-forwarded-for": FORWARDED_IP,
}

KBLOB_HEADERS = {
    "accept": "image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "multipart/form-data",
    "referer": "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": USER_AGENT,
    "x-edge-shopping-flag": "1",
    "x-forwarded-for": FORWARDED_IP,
}

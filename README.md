<h1 align='center'>Bypass DDos-Guard.net</h1>

<p align='center'>  Python3 requests-based DDos-Guard bypass using TLS3</p>

## Features
* Requests-based
* Proxy support
* lightweight
* Fast

## Requirements
```
pip install tls-client==0.2.1
pip install async-tls-client
```

## Usage
```python3
from DDosGuardBypasser import ddosGuard

Bypass = ddosGuard().Bypass('https://targetSite.org/')

if Bypass['Success']:
    print('Successfully bypassed DDos-Guard')
else:
    print(Bypass['message'])
```

## Async Usage
```python3
import asyncio
from DDosGuardBypasser import AioDdosGuard

async def main():
    Bypass = await AioDdosGuard().Bypass('https://targetSite.org/')

    if Bypass['Success']:
        print('Successfully bypassed DDos-Guard')
        # You can now use the session for other requests
        # session = Bypass['Session']
        # response = await session.get('https://targetSite.org/protected-page')
        # print(response.text)
    else:
        print(Bypass['message'])

if __name__ == '__main__':
    asyncio.run(main())
```

import asyncio
from DDosGuardBypasser import AioDdosGuard

async def main():
    Bypass = await AioDdosGuard().Bypass('https://doxbin.org/')

    if Bypass['Success']:
        print('Successfully bypassed DDos-Guard')
        # You can now use the session for other requests
        # session = Bypass['Session']
        # response = await session.get('https://doxbin.org/some-page')
        # print(response.text)
    else:
        print(Bypass['message'])

if __name__ == '__main__':
    asyncio.run(main())
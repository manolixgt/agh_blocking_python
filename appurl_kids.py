from adguardhome import AdGuardHome
import asyncio

async def main():
    
    async with AdGuardHome("172.16.10.199") as adguard:
        version = await adguard.version()
        print("AdGuard version:", version)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
from adguardhome import AdGuardHome
import asyncio

# variable de nombre y url

nuevaLista = "pc block"
urlLista= "https://raw.githubusercontent.com/manolixgt/agh_blocking_python/main/blocklists/pc_block.txt"


async def main():
    
    async with AdGuardHome("172.16.10.199",password="lesli3,",port=80,username="admin") as adguard:
        bloquear = await adguard.filtering.add_url(nuevaLista,urlLista)
        print("Nueva lista agregada", bloquear)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
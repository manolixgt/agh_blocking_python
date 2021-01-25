from adguardhome import AdGuardHome
import asyncio

# variable de nombre y url

nuevaLista = "pc block"
urlLista= ""


async def main():
    
    async with AdGuardHome("172.16.10.199") as adguard:
        bloquear = await adguard.filtering.add_url(name = nuevaLista, url = urlLista)
        print("Nueva lista agregada", bloquear)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
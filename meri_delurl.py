from adguardhome import AdGuardHome
from keys import newpass,newuser
import asyncio

# variable de nombre y url

nuevaLista = "meri block"
urlLista= "https://raw.githubusercontent.com/manolixgt/agh_blocking_python/main/blocklists/meri_block.txt"


async def main():
    
    async with AdGuardHome("172.16.10.199",password=newpass,port=80,username=newuser) as adguard:
        bloquear = await adguard.filtering.remove_url(urlLista)
        # bloquear = await adguard.filtering.disable_url(urlLista)
        # refrescar = await adguard.filtering.refresh()
        print("Lista meri disabled", bloquear)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
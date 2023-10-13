from typing import Optional
import httpx

api_key: Optional[str] = None


async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}'

    async with httpx.AsyncClient() as client:
        resp: httpx.Response = await client.get(url)
        if resp.status_code != 200:
            raise ValidationError(status_code=resp.status_code, error=resp.text)


    data = resp.json()
    forecast = data['main']
    return forecast
